import requests
from datetime import datetime

APP_ID = "61e5cddd"
API_KEY = "f15d99b0196f843304284ccfd823c277"

SHETTY_ENDPOINT = "https://api.sheety.co/4093dca52dbbedbc2e8f1851bdde66aa/copyOfMyWorkouts/workouts"
SHETTY_API = "4093dca52dbbedbc2e8f1851bdde66aa"

nutrix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

GENDER = input("Enter your Gender:")
WEIGHT_KG = input("Enter your Weight:")
HEIGHT_CM = input("Enter your Height:")
AGE = input("Enter your Age:")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}



# Adding the data to google sheets
tdy = datetime.now()
tdy_now = tdy.strftime("%d/%m/%G")
time_now = tdy.strftime("%X")


response = requests.post(exercise_endpoint, json=parameters, headers=headers)

result = response.json()

for exercise in result["exercises"]:
    data = {
        "workout": {
            "date": tdy_now,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
responses = requests.post(url=SHETTY_ENDPOINT, json=data)
print(responses.text)