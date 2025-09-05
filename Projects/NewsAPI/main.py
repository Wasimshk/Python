from http.client import responses

import requests

query = input("What type of news are you interested?\n")
apikey = "2da3fbe9656949d58170f0252b93dfed"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-30&sortBy=publishedAt&apiKey={apikey}"

response = requests.get(url)
articals = response.json()["articles"]

# for artical in articals:
for index, artical in enumerate(articals):
    print(f"{index+1} title - {artical["title"]}\nurl - {artical["url"]}")
    print("\n***********************************************************************************************\n")