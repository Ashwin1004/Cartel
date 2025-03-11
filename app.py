from flask import Flask, request, jsonify, render_template
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate(r"C:\Users\ASHWIN\OneDrive\Desktop\DBMS PROJECT\carteldbms-firebase-adminsdk-fbsvc-c0394d0682.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# HTML Page for Frontend
@app.route('/')
def index():
    return render_template('index.html')  # Frontend interface

# API Endpoint to Fetch Data
@app.route('/query', methods=['POST'])
def query_data():
    try:
        # Get query from frontend
        user_query = request.form.get('query')

        # Example: Extract conditions from SQL-like query
        if "WHERE" in user_query:
            condition = user_query.split("WHERE")[1].strip()
        else:
            condition = ""

        # Firestore Query Logic
        data = []
        docs = db.collection("vehicles").stream()
        for doc in docs:
            record = doc.to_dict()

            # Example Condition: vehicle_id = '1234'
            if condition:
                key, value = condition.split("=")
                key, value = key.strip(), value.strip().strip("'")
                if str(record.get(key)) == value:
                    data.append(record)
            else:
                data.append(record)

        return jsonify({"result": data})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

