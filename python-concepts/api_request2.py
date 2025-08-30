import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/2")
assert response.ok
print("Get Request: ", response.json())

response = requests.post("https://jsonplaceholder.typicode.com/posts", data={"name":"Wasim Shaikh", "course":"api automation"} )
assert response.ok
print("Post Request: ", response.json())

response = requests.put("https://jsonplaceholder.typicode.com/posts/2", data={"name":"Wasim Shaikh", "request":"learning api automation through requests library"})
assert response.ok
print("Put Request: ", response.json())

response = requests.patch("https://jsonplaceholder.typicode.com/posts/2", data={"name":"wasim", "body": "randomData"})
assert response.ok
print("Patch Request: ", response.json())

response = requests.delete("https://jsonplaceholder.typicode.com/posts/2")
assert response.ok
print("Delete Request: ", response.json())

"""
response

Get Request:     {'userId': 1, 'id': 2, 'title': 'qui est esse', 'body': 'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla'}
Post Request:    {'name': 'Wasim Shaikh', 'course': 'api automation', 'id': 101}
Put Request:     {'name': 'Wasim Shaikh', 'request': 'learning api automation through requests library', 'id': 2}
Patch Request:   {'userId': 1, 'id': 2, 'title': 'qui est esse', 'body': 'randomData', 'name': 'wasim'}
Delete Request:  {}

"""