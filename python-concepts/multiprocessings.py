import requests
import multiprocessing


def worker(num):
    print(f"Process {num}: Starting")
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{num}")
    assert response.ok
    print("Get Request:", response.json())
    print(f"Process {num}: Finishing")

# this guard is mandetory in multiprocess
if __name__ == "__main__":
    processes = []
    for i in range(1, 6):
        process = multiprocessing.Process(target=worker, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()  # Wait for all processes to finish

    print("All processes completed.")


"""


"""