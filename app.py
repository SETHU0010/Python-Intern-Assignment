from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Database Configuration Function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="app_db"
    )

# Create Table If Not Exists
def create_table():
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS apps (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    app_name VARCHAR(255) NOT NULL,
                    version VARCHAR(50),
                    description TEXT
                )
            ''')
            conn.commit()

create_table()

# Serve Frontend
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint to Add App
@app.route('/add-app', methods=['POST'])
def add_app():
    try:
        data = request.json
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                query = "INSERT INTO apps (app_name, version, description) VALUES (%s, %s, %s)"
                cursor.execute(query, (data['app_name'], data['version'], data['description']))
                conn.commit()
                return jsonify({"message": "App added successfully!", "app_id": cursor.lastrowid}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to Retrieve App by ID
@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM apps WHERE id = %s", (id,))
                app_data = cursor.fetchone()
                if app_data:
                    return jsonify({"id": app_data[0], "app_name": app_data[1], "version": app_data[2], "description": app_data[3]}), 200
                else:
                    return jsonify({"message": "App not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to Retrieve All Apps
@app.route('/get-all-apps', methods=['GET'])
def get_all_apps():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM apps")
                apps = cursor.fetchall()
                app_list = [{"id": row[0], "app_name": row[1], "version": row[2], "description": row[3]} for row in apps]
                return jsonify(app_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to Update App by ID
@app.route('/update-app/<int:id>', methods=['PUT'])
def update_app(id):
    try:
        data = request.json
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                # Check if app exists
                cursor.execute("SELECT * FROM apps WHERE id = %s", (id,))
                if not cursor.fetchone():
                    return jsonify({"message": "App not found"}), 404
                
                # Update the app details
                query = "UPDATE apps SET app_name = %s, version = %s, description = %s WHERE id = %s"
                cursor.execute(query, (data['app_name'], data['version'], data['description'], id))
                conn.commit()
                
                return jsonify({"message": "App updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to Delete an App by ID
@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM apps WHERE id = %s", (id,))
                if not cursor.fetchone():
                    return jsonify({"message": "App not found"}), 404
                
                cursor.execute("DELETE FROM apps WHERE id = %s", (id,))
                conn.commit()
                return jsonify({"message": "App deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
