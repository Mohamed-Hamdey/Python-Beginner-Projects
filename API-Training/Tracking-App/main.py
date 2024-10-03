import requests
from datetime import datetime


GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 160
AGE = 18

APP_ID = "b41bd1a4"
API_KEY = "be1cfccab7cba7d458b0d2362628fc3f	"




exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": "Basic bW9oYW1lZGhhbWR5OmJuVnNiRHB1ZFd4cw=="
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
sheet_endpoint = "https://api.sheety.co/ce3b48cc8b53b6223b0b48aa009dd66f/myWorkouts/workouts"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

header = {

}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    requests.get("https://httpbin.org/basic-auth/user/pass", auth=("mohamedhamdy", "bnVsbDpudWxs"))
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,headers=headers)
    print(sheet_response.text)







