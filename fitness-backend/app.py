from flask import Flask, jsonify, request

app = Flask(__name__)

workout_entries = []

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return "This is a fitness tracking API"

@app.route("/calories")
def calories():
    calorie_data = [
        {"date": "2025-05-13", "calories":2200},
        {"date": "2025-05-14", "calories":2000},
        {"date": "2025-05-15", "calories":2100},
    ]
    return jsonify(calorie_data)

@app.route("/workouts", methods=["GET"])
def get_workouts():
    return jsonify(workout_entries)

@app.route("/workouts", methods=["POST"])
def add_workout():
    data = request.get_json()

    required_fields = ["date", "type", "duration_min"]
    if not all (field in data for field in required_fields):
        return jsonify({"error": "Missing fields in request"}), 400
    
    workout_entries.append(data)
    return jsonify({"message":"Workout added", "workout": data}), 201

if __name__ == "__main__":
    app.run(debug=True)