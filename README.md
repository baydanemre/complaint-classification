# Complaint Classification System

This project is a web application designed to classify customer complaints for a banking company. The system leverages a React-based frontend and a Python-based backend to provide seamless complaint classification using OpenAI's GPT API.

## Project Structure

The project directory is organized as follows:

```
complaint-classification
├── backend
│   ├── __pycache__
│   ├── .env
│   ├── .env.example
│   ├── requirements.txt
│   ├── app.py
│   └── deleteCollection.py
├── frontend
│   ├── node_modules
│   ├── public
│   └── src
│       ├── assets
│       ├── components
│       ├── redux
│       ├── App.css
│       ├── App.jsx
│       ├── index.css
│       └── main.jsx
├── .gitignore
├── package-lock.json
├── package.json
├── vite.config.js
└── README.md
```

## Application Preview

![Application Screenshot](frontend/src/assets/application_ss.png)

### Backend
- **`app.py`**: The main Flask application that handles API requests.
- **`deleteCollection.py`**: A script for managing database collections.
- **`.env`**: Environment variables for sensitive configuration (not included in version control).
- **`.env.example`**: Example environment variables for development setup.

### Frontend
- **`src/assets`**: Contains static assets such as images.
- **`src/components`**: Reusable React components.
- **`src/redux`**: State management using Redux.
- **`App.jsx`**: Main application entry point.
- **`App.css`**: Application-specific styling.
- **`index.css`**: Global styles.
- **`main.jsx`**: React app bootstrap file.

## Features

- Complaint classification using OpenAI's GPT API.
- Intuitive and responsive user interface built with React.
- Backend API for handling user inputs and GPT API integration.
- Environment variable support for secure configuration.

## Prerequisites

Ensure you have the following installed:

- Node.js (v14 or later)
- Python (v3.10 or later)
- pip
- Virtual environment tool (e.g., `venv` or `virtualenv`)

## Installation

### Backend Setup
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file based on `.env.example` and configure the required variables.
5. Run the backend server:
   ```bash
   uvicorn app:app --reload
   ```

### Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

## Usage

1. Start the backend server.
2. Start the frontend development server.
3. Access the application in your web browser at `http://localhost:3000` (or the port specified in your `vite.config.js`).

## Environment Variables

The `.env` file in the `backend` folder should contain:

```env
OPENAI-API-KEY = your_api_key
MONGO_CLIENT = mongodb+srv://username:password@cluster_name.ijzcq.mongodb.net
```

## Technologies Used

- **Frontend**: React, Redux, Vite
- **Backend**: Flask, Python
- **Database**: MongoDB (or your chosen database)
- **API**: OpenAI GPT API

## Contributing

Contributions are welcome! Please fork this repository and create a pull request with your changes.
