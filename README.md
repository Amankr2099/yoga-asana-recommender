# YogaFlow

## Introduction
YogaFlow is an AI-powered web application that provides personalized yoga asana recommendations based on user inputs. Built using **Flask, HTML, CSS**, and **Google’s Gemini API**, this application helps users find yoga poses that align with their wellness goals and even offers a scheduling feature for structured practice.

## Features
- **Personalized Yoga Recommendations** based on user input (name, age, height, weight, and goal).
- **AI-Powered Asana Selection** using Google’s Gemini API.
- **Step-by-Step Procedure** for each recommended asana.
- **High-Quality Images & Video Links** for better guidance.
- **Scheduling Feature** that generates a customized yoga routine.

## How It Works
1. **Fill Out the Form**
   - Enter your **Name**
   - Provide your **Age**
   - Input your **Height** and **Weight**
   - Select a **Target Goal**: 
     - Stress
     - Digestion
     - Flexibility
     - Mobility
     - Relaxation
     - Balance

2. **Get Your Recommendation**
   - Click **‘Get Recommendation’**.
   - The system processes your input and provides a curated list of yoga asanas.
   
3. **View Recommended Asanas**
   - Each recommended asana includes:
     - **Step-by-Step Instructions**
     - **A Reference Image**
     - **A Video Tutorial Link**

4. **Schedule Your Yoga Routine**
   - Click **‘Get Scheduling’** to send data to **Gemini API**.
   - Receive a structured yoga schedule based on your input.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/YogaFlow.git
   cd YogaFlow
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open your browser and go to `http://localhost:5000`

## Technologies Used
- **Flask** - Backend framework
- **HTML/CSS** - Frontend UI
- **Google Gemini API** - AI-powered recommendations
- **JavaScript** - Client-side interactions

## Contribution
Feel free to contribute to YogaFlow! Follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your branch and create a Pull Request.

## License

This project is proprietary and all rights are reserved. You may not copy, modify, distribute, or use this code in any manner without explicit permission from the owner.

Unauthorized use of this project is prohibited.

