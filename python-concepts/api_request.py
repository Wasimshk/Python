import requests
import json

response = requests.get('https://api.github.com/users/Wasimshk')

print(response.text)

with open("getrequest.txt", "w") as writer:
    dict = response.json()
    writer.write(f"{dict}")

# login
login_creds = {
    "userEmail": "wasimahmad4210@gmail.com",
    "userPassword": "Automation@4210"
}

response = requests.post("https://rahulshettyacademy.com/api/ecom/auth/login", data=login_creds)

response_json = response.json()
token = response_json["token"]
print(token)


# create order
create_order_payload={
    "orders": [
        {
            "country": "India",
            "productOrderedId": "68a961719320a140fe1ca57c"
        }
    ]
}

create_order_response = requests.post("https://rahulshettyacademy.com/api/ecom/order/create-order", data=create_order_payload, headers={"Authorization": f"{token}"})
response_json = create_order_response.json()
# orderID = response_json["productOrderId"]
print(response_json)









