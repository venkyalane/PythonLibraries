import requests
import random
from faker import Faker

fake = Faker()

info = {
    "id": random.randint(1,50),
    "account_name": fake.name(),
    "bal": random.randint(4000,10000),
    "accdate": input("Enter accdate(YY-MM-DD): "),
    "email": fake.email(),
    "mobile": fake.phone_number()
}
r = requests.post('https://venkyalane.pythonanywhere.com/test2/', data= info)
print("status code: ", r.status_code)

