import threading
import time

# simple example
# def worker(num):
#     print(f"Thread {num}: Starting")
#     time.sleep(2)  # Simulate some work
#     print(f"Thread {num}: Finishing")
#
#
# threads = []
# for i in range(3):
#     thread = threading.Thread(target=worker, args=(i,))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()  # Wait for all threads to finish
#
# print("All threads completed.")
# ////////////////////////////////////////////////////////////////
import requests
# example with API requests

def worker(num):
    print(f"Thread {num}: Starting")
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{num}")
    assert response.ok
    print("Get Request: ", response.json())
    print(f"Thread {num}: Finishing")


threads = []
for i in range(1, 6):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()  # Wait for all threads to finish

print("All threads completed.")

# /////////////////////////////////////////////////////////

users_list = [{"name": "Wasim Shaikh", "course": "api automation"}, {"name": "Almas Shaikh", "course": "api automation"}, {"name": "Irshad Shaikh", "course": "api automation"}, {"name": "Wajid Shaikh", "course": "api automation"}, {"name": "Azim Shaikh", "course": "api automation"}]

def worker(num):
    print(f"Thread {num}: Starting")
    response = requests.post("https://jsonplaceholder.typicode.com/posts",
                             data=users_list[num-1])
    assert response.ok
    print("Post Request: ", response.json())
    print(f"Thread {num}: Finishing")


threads = []
for i in range(1, 6):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()  # Wait for all threads to finish

print("All threads completed.")


