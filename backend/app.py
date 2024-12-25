from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
import openai
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# API anahtarını al
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI API Key
openai.api_key = api_key
# FastAPI uygulaması
app = FastAPI()

# CORS Ayarları
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB bağlantısı
try:

    client = MongoClient(os.getenv("MONGO_CLIENT"))
    db = client["user_complaints"]
    collection = db["complaints"]
    print("MongoDB bağlantısı başarılı:", db.list_collection_names())
except Exception as e:
    print("MongoDB bağlantı hatası:", e)


# Şikayet modeli
class Complaint(BaseModel):
    title: str
    complaint: str
    type: str = None

# OpenAI ile sınıflandırma
def classify_with_gpt(complaint_text):
    prompt = f"""
    Classify the complaint into one of the following categories and return only the **category name in Turkish**:
    - Shopping Loan: Loans taken for purchases from stores or e-commerce websites.
    - Gold: Transactions related to buying/selling gold, gold accounts, or gold prices.
    - Vehicle Loan: Loans used for vehicle purchases and related issues.
    - Bank Card: Issues related to bank cards provided by Denizbank.
    - Individual Pension: Transactions related to individual pension accounts, contributions, and state support.
    - Black Card: Issues related to Denizbank's special card, Black Card.
    - Bonus Business: Complaints related to bonus-featured commercial credit cards.
    - Bonus Credit Card: Issues related to Denizbank Bonus credit cards, such as fees and limits.
    - Debt Consolidation Loan: Issues related to loans taken to consolidate existing debts.
    - Check: Complaints about check transactions, check collection, or check accounts.
    - Digital Loan: Issues related to loans taken via internet or mobile banking.
    - Dollar: Complaints about dollar transactions, dollar accounts, or exchange rates.
    - Dollar Exchange Rate: Issues related to fluctuations in the dollar exchange rate.
    - Foreign Exchange: Buying/selling foreign currencies and foreign exchange accounts.
    - Foreign Exchange Rate: Issues related to changes in foreign exchange rates.
    - EFT: Complaints about electronic fund transfer transactions.
    - Education Loan: Issues related to loans taken for educational expenses.
    - Retirement Loan: Complaints about loans provided to retirees.
    - Retirement Promotion: Promotions for retirees and related issues.
    - Euro: Complaints about euro transactions, euro accounts, or exchange rates.
    - Interest-Free Loan: Interest-free loan products and related transactions.
    - FAST: Issues related to FAST system instant money transfers.
    - Bill Payment: Complaints about bill payment transactions.
    - Fund: Investment funds and related transactions.
    - Gold Card: Issues related to Denizbank's Gold Card.
    - Silver: Buying/selling silver and silver accounts.
    - Money Transfer: Issues related to money transfer transactions.
    - Account Opening: Complaints about opening new accounts.
    - Account Closure: Issues related to closing existing accounts.
    - HGS: Complaints about the Fast Pass System (HGS).
    - Stock: Complaints related to stock trading and transactions.
    - Personal Loan: Complaints about personal loans taken for individual needs.
    - Business Card: Issues related to cards designed for businesses.
    - Safe Deposit Box: Complaints about safe deposit box services.
    - SME Loan: Loans provided to small and medium enterprises (SMEs).
    - Housing Loan: Complaints related to loans taken for house purchases.
    - Credit: General credit products and related transactions.
    - Credit Card: Complaints about Denizbank credit cards, such as fees and limits.
    - Overdraft Account: Issues related to overdraft accounts.
    - Rescuer Account: Complaints about Denizbank's Rescuer Account product.
    - Courier: Complaints about delays or issues with the delivery of bank products.
    - Salary: Complaints about salary accounts, payments, and related transactions.
    - Savings Account: Issues related to savings accounts.
    - MoneyGram: Complaints about MoneyGram services.
    - Motor Vehicle Tax Payment: Complaints about motor vehicle tax payment transactions.
    - Cash Advance: Issues related to cash advance transactions.
    - Net Card: Complaints about Denizbank's Net Card product.
    - NFC: Complaints about NFC payment transactions.
    - Number Update: Issues related to updating phone numbers.
    - Automatic Payment: Complaints about automatic payment orders.
    - Cash Withdrawal: Issues related to withdrawing money from banks or ATMs.
    - Cash Deposit: Complaints about depositing money into banks or ATMs.
    - Platinum: Issues related to Denizbank's Platinum card.
    - POS: Complaints about POS devices and related transactions.
    - Promotion: Complaints about general promotions offered by the bank.
    - Virtual Card: Issues related to creating or using virtual cards.
    - Insurance: Complaints about insurance products and related transactions.
    - SIM Card Block: Issues related to SIM card blocks and transactions.
    - Swift: Complaints about Swift transactions.
    - Password: Issues related to password transactions and updates.
    - Installment Cash Advance: Complaints about installment cash advance transactions.
    - Agricultural Loan: Loans provided to the agricultural sector.
    - Producer Card: Issues related to cards designed for producers.
    - Time Deposit Account: Complaints about time deposit accounts.
    - Transfer: Issues related to transfer transactions between accounts.
    - Investment Account: Complaints about investment accounts and related transactions.
    Complaint: {complaint_text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Şikayet ekleme endpoint'i
@app.post("/add_complaint/")
async def add_complaint(complaint: Complaint):
    category = classify_with_gpt(complaint.complaint)  # Şikayet sınıflandırılır
    new_complaint = {
        "title": complaint.title,
        "complaint": complaint.complaint,
        "type": category,
    }
    result = collection.insert_one(new_complaint)  # MongoDB'ye ekleme
    return {
        "message": "Complaint added successfully",
        "id": str(result.inserted_id),
        "title": complaint.title,
        "complaint": complaint.complaint,
        "type": category,
    }

# Son 5 şikayeti alma endpoint'i
@app.get("/recent_complaints/")
async def get_recent_complaints():
    complaints = list(
        collection.find({}, {"_id": 0})
        .sort("_id", -1)
        .limit(5)
    )
    print(collection.find_one())
    return {"complaints": complaints}
