from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import json

TRANSACTIONS_FILE = 'transactions.json'

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

# In-memory simulation (replace with DB for production)
# Load at startup
if os.path.exists(TRANSACTIONS_FILE):
    with open(TRANSACTIONS_FILE) as f:
        try:
            transactions = json.load(f)
        except json.JSONDecodeError:
            transactions = []
else:
    transactions = []
categories = []

# --- API Endpoints --- #

# Add category
@app.route('/add_category', methods=['POST'])
def add_category():
    data = request.json
    categories.append(data)
    return jsonify({'success': True, 'categories': categories})

# List categories
@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify({'categories': categories})

# Add transaction (extended!)
@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    data = request.form.to_dict()
    print("FORM DATA:", data)
    file = request.files.get('bill_image')
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        data['img_url'] = f"/uploads/{filename}"

    # Parse extra fields
    data['storeName'] = data.get('storeName', "")
    data['billNo'] = data.get('billNo', "")

    # Parse items JSON if present
    items_raw = data.get('items', '[]')
    try:
        data['items'] = json.loads(items_raw)
    except Exception:
        data['items'] = []

    tx_id = data.get('id')
    # ... handle file, parse items, etc ...
    if not any(t.get('id') == tx_id for t in transactions):
        transactions.append(data)
        with open(TRANSACTIONS_FILE, 'w') as f:
            json.dump(transactions, f)
        print("Added", data)
    else:
        print("Duplicate transaction, not adding:", tx_id)
        
    with open(TRANSACTIONS_FILE, 'w') as f:
        json.dump(transactions, f)
    print("TRANSACTIONS LIST:", transactions)
    return jsonify({'success': True, 'transactions': transactions})

# List transactions
@app.route('/transactions', methods=['GET'])
def get_transactions():
    return jsonify({'transactions': transactions})

# Serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# --- Utility (Init uploads folder if needed) --- #
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/ping')
def ping():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
