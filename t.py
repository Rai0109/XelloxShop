import requests
import random
import string
import time
url = "http://10.2.1.80:8002/api/register"

def random_username():
    return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def random_password():
    return ''.join(random.choices(string.digits, k=8))

for i in range(10000):
    data = {
        "username": random_username(),
        "password": random_password(),
        "referral_code": ""
    }

    res = requests.post(url, json=data).json()
    print(f"{i+1} | {data['username']} | {data['password']} -> {res}")

    try:
        res = requests.post(url, json=data).json()
        print(f"✅ {data['username']} | {data['password']} -> {res}")
    except Exception as e:
        print("❌ Lỗi:", e)
    time.sleep(0)