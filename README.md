# 📱 App Management API

Welcome to the **App Management API**! This Flask-based API allows you to manage applications with CRUD operations using MySQL as the database.

## 🚀 Features
- Add, update, delete, and retrieve app details
- Uses MySQL for data storage
- RESTful API with JSON responses
- Simple and easy to deploy

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/app-management-api.git
   ```
2. Navigate to the project directory:
   ```bash
   cd app-management-api
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up MySQL database and update credentials in `app.py`.
6. Run the Flask application:
   ```bash
   python app.py
   ```

## 🌐 API Endpoints

### ➕ Add an App
`POST /add-app`
#### Request Body:
```json
{
  "app_name": "Example App",
  "version": "1.0.0",
  "description": "This is an example app."
}
```
#### Response:
```json
{
  "message": "App added successfully!",
  "app_id": 1
}
```

### 📥 Get an App by ID
`GET /get-app/{id}`
#### Response:
```json
{
  "id": 1,
  "app_name": "Example App",
  "version": "1.0.0",
  "description": "This is an example app."
}
```

### 📋 Get All Apps
`GET /get-all-apps`
#### Response:
```json
[
  {
    "id": 1,
    "app_name": "Example App",
    "version": "1.0.0",
    "description": "This is an example app."
  }
]
```

### ✏️ Update an App
`PUT /update-app/{id}`
#### Request Body:
```json
{
  "app_name": "Updated App",
  "version": "2.0.0",
  "description": "Updated description."
}
```
#### Response:
```json
{
  "message": "App updated successfully!"
}
```

### ❌ Delete an App
`DELETE /delete-app/{id}`
#### Response:
```json
{
  "message": "App deleted successfully!"
}
```

