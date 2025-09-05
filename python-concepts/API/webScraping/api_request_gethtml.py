# sample.py
import requests

url = "https://formy-project.herokuapp.com/"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text  # full HTML content
    print(html_content)           # prints complete HTML script
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")

with open("formy_page.html", "w", encoding="utf-8") as f:
    f.write(html_content)
    