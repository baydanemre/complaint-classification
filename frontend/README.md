Backend Bağlantıları ve Akış
1. FastAPI

    FastAPI:
        Uygulamanın ana çerçevesini oluşturur.
        İki temel endpoint tanımlar:
            POST /add_complaint: Yeni şikayet ekleme.
            GET /recent_complaints: Son 5 şikayeti alma.

2. Complaint Model (Backend)

    Complaint (BaseModel):
        Backend'e gelen verilerin formatını doğrular.
        Alanlar:
            title: Şikayet başlığı.
            complaint: Şikayet açıklaması.
            type: Şikayet türü (Mobil Bankacılık, ATM Sorunları vb.).
        Kullanım:
            POST /add_complaint endpointinde kullanılır.

3. MongoDB

    Bağlantılar:
        collection.insert_one: Yeni şikayeti MongoDB'ye ekler.
        collection.find: Veritabanındaki son 5 şikayeti döndürür.

4. classify_with_gpt

    Görev:
        Şikayeti GPT ile sınıflandırır.
        Gelen complaint_text kullanılarak OpenAI'ye bir prompt gönderilir.
        GPT yanıtını döndürür (Mobile Banking, ATM Issues gibi).
    Bağlantılar:
        POST /add_complaint endpointinde çağrılır.


----------------------------------------------------------------------------------------------------------


Backend Akışı

    POST /add_complaint:
        Kullanıcıdan gelen veriler:
            title, complaint.
        Adımlar:
            classify_with_gpt ile şikayet türü belirlenir.
            MongoDB'ye eklenir (collection.insert_one).
            Veritabanı ID'si ve sınıflandırma sonucu frontend'e döner.
        Bağlantılar:
            Complaint modeli doğrulama sağlar.
            GPT çağrısı yapılır.
            MongoDB'ye veri eklenir.

    GET /recent_complaints:
        Adımlar:
            MongoDB'den son 5 şikayet çekilir (collection.find).
            JSON formatında frontend'e gönderilir.
        Bağlantılar:
            Sadece MongoDB ile etkileşim kurar.


----------------------------------------------------------------------------------------------------------


Frontend Bağlantıları ve Akış
1. Redux Store

    Dilimler (Slices):
        user_complaint_input:
            Kullanıcının formdaki girdi bilgilerini tutar.
            State:
                input_title: Şikayet başlığı.
                input_complaint: Şikayet metni.
            Reducer'lar:
                setTitle: Kullanıcı başlık girdisini günceller.
                setComplaint: Kullanıcı metin girdisini günceller.
        complaint_operations:
            Backend'deki GET ve POST işlemlerini yönetir.
            Thunk İşlemleri:
                PostComplaint: Yeni şikayeti backend'e gönderir (POST /add_complaint).
                FetchRecentComplaints: Backend'den son 5 şikayeti çeker (GET /recent_complaints).
            State:
                complaints: Son 5 şikayet.
                title, complaint, type: Son eklenen şikayet bilgileri.
        create_complaint_row:
            Redux state içinde tabloyu günceller.
            State:
                complaint_row: Frontend'deki tabloyu tutar.
            Reducer'lar:
                addNewComplaint: Kullanıcının şikayetini tabloya ekler.

2. React Bileşenleri (Components)
CreateComplaint

    Görev:
        Kullanıcıdan şikayet başlığı ve metni alır.
        Redux aracılığıyla veriyi backend'e gönderir.
        Form girdilerini sıfırlar.
        Şikayet gönderildikten sonra tabloyu günceller (FetchRecentComplaints).
    Redux Bağlantıları:
        setTitle ve setComplaint: Kullanıcı girdilerini günceller.
        PostComplaint: Şikayeti backend'e gönderir.
        FetchRecentComplaints: Backend'den son 5 şikayeti çeker.

ComplaintBox

    Görev:
        Backend'den gelen son 5 şikayeti tablo halinde gösterir.
        useEffect ile sayfa yüklendiğinde otomatik olarak FetchRecentComplaints çalıştırılır.
    Redux Bağlantıları:
        FetchRecentComplaints: Backend'den veri çeker.
        complaints: Tabloyu güncellemek için kullanılır.

UserComplaint

    Görev:
        Tek bir şikayeti ekranda gösterir.
        Parametre olarak title, complaint, type alır ve uygun formatta ekrana yazdırır.


----------------------------------------------------------------------------------------------------------


Frontend Akışı

    Kullanıcı Form Doldurur (CreateComplaint):
        Kullanıcı girdileri setTitle ve setComplaint ile Redux state'e kaydedilir.
        Kullanıcı Check butonuna bastığında:
            PostComplaint: Şikayet backend'e gönderilir.
            FetchRecentComplaints: Backend'den son 5 şikayet alınır.
            Şikayet başarılı mesajı gösterilir.

    Tablo Güncellenir (ComplaintBox):
        Backend'den gelen son 5 şikayet FetchRecentComplaints ile çekilir.
        Redux state içindeki complaints güncellenir.
        React, güncellenen state'i tabloya yansıtır.

    Tabloda Her Bir Şikayet (UserComplaint):
        Gelen complaints listesi, her bir eleman için bir UserComplaint bileşeni oluşturur.
