# App Management API

This project is a Flask-based REST API for managing applications, utilizing MySQL for data storage. It provides endpoints to create, retrieve, update, and delete app details.

## Features
- Add new applications with version and description
- Retrieve app details by ID
- Get a list of all applications
- Update existing app details
- Delete an app

## Technologies Used
- Python
- Flask
- MySQL

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/app-management-api.git
   cd app-management-api
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up MySQL database:
   - Ensure MySQL is running
   - Create a database `app_db`
   - Update the database configuration in `app.py` if necessary

## Running the Application
```bash
python app.py
```
The application runs on `http://127.0.0.1:5000/`

## API Endpoints

### 1. Add App
- **URL:** `/add-app`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "app_name": "MyApp",
    "version": "1.0",
    "description": "A sample app"
  }
  ```
- **Response:**
  ```json
  {
    "message": "App added successfully!",
    "app_id": 1
  }
  ```

### 2. Get App by ID
- **URL:** `/get-app/{id}`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "id": 1,
    "app_name": "MyApp",
    "version": "1.0",
    "description": "A sample app"
  }
  ```

### 3. Get All Apps
- **URL:** `/get-all-apps`
- **Method:** `GET`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "app_name": "MyApp",
      "version": "1.0",
      "description": "A sample app"
    }
  ]
  ```

### 4. Update App
- **URL:** `/update-app/{id}`
- **Method:** `PUT`
- **Request Body:**
  ```json
  {
    "app_name": "UpdatedApp",
    "version": "2.0",
    "description": "Updated description"
  }
  ```

### 5. Delete App
- **URL:** `/delete-app/{id}`
- **Method:** `DELETE`
- **Response:**
  ```json
  {
    "message": "App deleted successfully!"
  }
  ```

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues or pull requests to improve the project.

