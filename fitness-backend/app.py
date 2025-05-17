from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    duration_min = db.Column(db.Integer, nullable=False)

class CalorieEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    calories = db.Column(db.Integer, nullable=False)

with app.app_context():
    try:
        db.create_all()
        print("Database tables created")
    except Exception as e:
        print("Error making database: ",e)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return "This is a fitness tracking API"

@app.route("/calories", methods=["GET"])
def get_calories():
    calories = CalorieEntry.query.all()
    result = [
        {"id": w.id, "date": w.date, "calories":w.calories}
        for w in calories
    ]
    return jsonify(result)

@app.route("/calories", methods=["POST"])
def add_calories():
    data = request.get_json()

    required_fields = ["date", "calories"]
    if not all (field in data for field in required_fields):
        return jsonify({"error": "Missing fields in calorie data"}), 400
    
    calories = CalorieEntry(
        date = data["date"],
        caloires=data["calories"]
    )
    db.session.add(calories)
    db.session.commit()

    return jsonify({"message": "Calorie entry added", "calories": {
        "id":calories.id,
        "date":calories.date,
        "calories":calories.calories
    }}), 201

@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()
    result = [
        {"id":w.id, "date":w.date, "type":w.type, "duration_min": w.duration_min}
        for w in workouts
    ]
    return jsonify(result)

@app.route("/api/workouts", methods=["POST", 'OPTIONS'])
def add_workout():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.get_json()

    required_fields = ["date", "type", "duration_min"]
    if not all (field in data for field in required_fields):
        return jsonify({"error": "Missing fields in request"}), 400
    
    workout = Workout(
        date=data["date"],
        type=data["type"],
        duration_min = data["duration_min"]
    )
    db.session.add(workout)
    db.session.commit()

    return jsonify({"message":"Workout added", "workout": {
        "id":workout.id,
        "date":workout.date,
        "type":workout.type,
        "duration_min":workout.duration_min
    }}), 201

if __name__ == "__main__":
    app.run(debug=True)