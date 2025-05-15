from flask import Flask, jsonify, request

app = Flask(__name__)

workout_entries = []
calorie_entries = []

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return "This is a fitness tracking API"

@app.route("/calories", methods=["GET"])
def get_calories():
    return jsonify(calorie_entries)

@app.route("/calories", methods=["POST"])
def add_calories():
    data = request.get_json()

    required_fields = ["date", "calories"]
    if not all (field in data for field in required_fields):
        return jsonify({"error": "Missing fields in calorie data"}), 400
    calorie_entries.append(data)
    return jsonify({"message": "Calorie entry added", "calories": data}), 201

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