# AI Chat System - REST API Implementation

This project provides a REST API for an AI-powered chat system developed using Django. The system allows users to register, log in, interact with an AI chatbot, and manage their token balance. Each interaction with the chatbot deducts tokens from the user's account.

## Key Features

1. **User Registration**  
   Allows users to create a new account with a unique username and password. Upon successful registration, the user is credited with 4000 tokens.

2. **User Login**  
   Users can log in by providing their username and password. A unique authentication token is returned upon successful login, which is required for further API interactions.

3. **Chat with AI**  
   Users can interact with the AI-powered chatbot by sending messages. Each question asked deducts 100 tokens from the user's account. The AI will return a response to the user's query.

4. **Token Balance**  
   Users can view their current token balance by providing their authentication token. The balance reflects the remaining tokens after interactions with the chatbot.

## API Endpoints

### 1. User Registration
- **URL**: `/api/register/`  
- **Method**: `POST`  
- **Request Body**: 
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**: 
  ```json
  {
    "message": "User created successfully",
    "tokens": 4000
  }
  ```

### 2. User Login
- **URL**: `/api/login/`  
- **Method**: `POST`  
- **Request Body**: 
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**: 
  ```json
  {
    "token": "authentication_token"
  }
  ```

### 3. Chat with AI
- **URL**: `/api/chat/`  
- **Method**: `POST`  
- **Request Body**: 
  ```json
  {
    "message": "string",
    "token": "authentication_token"
  }
  ```
- **Response**: 
  ```json
  {
    "response": "AI-generated response",
    "tokens_deducted": 100
  }
  ```

### 4. Check Token Balance
- **URL**: `/api/token_balance/`  
- **Method**: `GET`  
- **Headers**: 
  - `Authorization: Bearer authentication_token`
- **Response**: 
  ```json
  {
    "tokens": "remaining_token_balance"
  }
  ```

## Installation Instructions

### Prerequisites
- Python 3.8 or higher
- Django 3.x or higher
- Django REST Framework

### Steps to Set Up Locally

1. **Clone the Repository**  
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/ai-chat-system.git
   cd ai-chat-system
   ```

2. **Create a Virtual Environment**  
   Set up a virtual environment for the project:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**  
   Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations**  
   Set up the database by applying migrations:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**  
   Run the development server:
   ```bash
   python manage.py runserver
   ```

   The server will be available at `http://127.0.0.1:8000/`. You can use an API testing tool like Postman to interact with the endpoints.

## Sample Requests

### 1. User Registration
```bash
POST /api/register/
Content-Type: application/json
{
  "username": "jane_doe",
  "password": "strongpassword"
}
```

### 2. User Login
```bash
POST /api/login/
Content-Type: application/json
{
  "username": "jane_doe",
  "password": "strongpassword"
}
```

### 3. Chat with AI
```bash
POST /api/chat/
Content-Type: application/json
Authorization: Bearer <authentication_token>
{
  "message": "How is the weather today?"
}
```

### 4. Check Token Balance
```bash
GET /api/token_balance/
Authorization: Bearer <authentication_token>
```

## Challenges Faced
- Handling user authentication and ensuring token validity during each API request.
- Managing token balance and deducting tokens accurately for each chatbot interaction.

---
