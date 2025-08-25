from flask import Flask, render_template, request

app = Flask(__name__)

# Simple AI logic for workout recommendations
def ai_workout_recommendation(goal, fitness_level):
    if goal == "lose_weight":
        if fitness_level == "beginner":
            return ["20-min Cardio", "Bodyweight squats", "Jumping Jacks", "Plank (30 sec)"]
        elif fitness_level == "intermediate":
            return ["HIIT Circuit", "Burpees", "Mountain Climbers", "Pushups"]
        else:
            return ["Running (5km)", "Box jumps", "Weighted Lunges", "Pull-ups"]
    elif goal == "build_muscle":
        if fitness_level == "beginner":
            return ["Pushups", "Squats", "Lunges", "Dumbbell rows"]
        elif fitness_level == "intermediate":
            return ["Bench Press", "Deadlifts", "Pull-ups", "Plank (1 min)"]
        else:
            return ["Weighted Squats", "Clean & Press", "Barbell Rows", "Chin-ups"]
    else:
        return ["Yoga Flow", "Stretching", "Walking", "Meditation"]

@app.route("/", methods=["GET", "POST"])
def index():
    recommended_workouts = None
    if request.method == "POST":
        goal = request.form.get("goal")
        level = request.form.get("fitness_level")
        recommended_workouts = ai_workout_recommendation(goal, level)
    return render_template("index.html", workouts=recommended_workouts)

if __name__ == "__main__":
    app.run(debug=True)