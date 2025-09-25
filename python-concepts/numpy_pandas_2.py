import pandas as pd

d = {
"id": 12,
"email": "rachel.howell@reqres.in",
"first_name": "Rachel",
"last_name": "Howell",
"avatar": "https://reqres.in/img/faces/12-image.jpg"
}
data = {"Name": ["Ali", "Sara", "John"], "Age": [25, 30, 28]}

df = pd.DataFrame(data)
print(df["Age"])   # 27.666...