from flask import Flask, render_template, request, jsonify, redirect, url_for
import google.generativeai as genai
import os
import random
from dotenv import load_dotenv
import json
with open('static/asans.json') as f:
    asans_data = json.load(f)

app = Flask(__name__)

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))


def get_schedule(name,age, weight, height, goal, asans):
    # Generate the prompt based on the user's data
    prompt = f"""
    Based on the following information:
    Name: {name}
    Age: {age}
    Weight: {weight}
    Height: {height}
    Goal: {goal}
    Asanas: {', '.join(asans)}

    Please generate a personalized yoga schedule with the asans given to you in a html table and some additinal tips as
    `
    <table border="1">
        <thead>
          <tr>
            <th>Asans</th>
            <th>Reps</th>
            <th>Timings</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Asan name</td>
            <td>reps ... </td>
            <td>timings ...</td>
          </tr>
         ...
        </tbody>
      </table>
      
      <p>
        Additinal tips...
      </p>
      `
    """

    # Generate the content using the AI model
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    
    return response.text  # Assuming the AI model's response contains the text content

@app.route("/generate-schedule", methods=["POST"])
def generate_schedule():
    # Get the data from the request
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    weight = data.get('weight')
    height = data.get('height')
    goal = data.get('goal')
    asans = data.get('asans')

    # Call the function to get the schedule
    schedule = get_schedule(name,age, weight, height, goal, asans)

    # Return the generated schedule as JSON
    return jsonify({'schedule': schedule})

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        # Get the form data
        name = request.form.get("name")
        age = int(request.form.get("age"))
        weight = float(request.form.get("weight"))
        height = int(request.form.get("height"))
        goal = request.form.get("goal")

        # Find matching asans based on the goal
        matching_asans = [asan for asan in asans_data if goal.lower() in [g.lower() for g in asan["goals"]]]
        
        # Ensure there are at least 1 and up to 4 asans selected
        selected_asans = random.sample(matching_asans, k=min(4, max(1, len(matching_asans))))

        # After the "loading", render the result page with selected asans
        return render_template("result.html", asans=selected_asans , name=name, age=age,weight=weight,height=height,goal=goal)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
