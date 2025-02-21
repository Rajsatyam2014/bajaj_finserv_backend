from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.get_json()
        if not data or "data" not in data:
            return jsonify({"is_success": False, "message": "Invalid input"}), 400
        
        user_id = "Raj_Satyam_07082003"  
        email = "22BCS15256@cuchd.in"
        roll_number = "22BCS15256"

        numbers = [x for x in data["data"] if x.isdigit()]
        alphabets = [x for x in data["data"] if x.isalpha()]
        highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []

        return jsonify({
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }), 200
    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
