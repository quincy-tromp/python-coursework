import requests
from datetime import datetime
import os


GENDER = "male"
WEIGHT_KG = 74 
HEIGHT_CM = 174
AGE = 28

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]

TOKEN = os.environ["TOKEN"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "age": AGE,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%H:%M:%S")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
            
        }
    }

    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer QjNvr$$hTD6l9gqNq7@F@Stu1"
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=header)

    