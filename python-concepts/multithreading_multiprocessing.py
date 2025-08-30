

"""
The {if __name__ == "__main__":} guard is mandatory in multiprocessing on Windows (and recommended everywhere) because:
When you create a new multiprocessing.Process, Python imports your script again in the new process.
Without the guard, the child process will run your whole script again, re-creating processes infinitely (fork bomb).
With the guard, only the code inside if __name__ == "__main__": executes in the main process, while child processes only run the target function (worker).


1. Why infinite loop happens
No guard → script body runs on every import.
When you start 3 processes:
Each child re-imports the script.
That means each child also runs the loop that starts 3 new processes.
Those children spawn more children... and it never stops → infinite process spawning.

2. What a process is
A process is an independent instance of the Python interpreter.
Unlike threads (which share memory), each process has its own memory space.
By default, each process runs on one CPU core (Python can schedule them across cores).
So if you start 3 processes and you have a 4-core CPU → Python can run them in parallel, each on its own CPU core.

3. Simplified picture
Threads: many workers inside one house (share memory).
Processes: each worker has its own house (separate memory, own CPU slot).


Multithreading → Multiple threads share the same memory space(single CPU core), run in a single process (better for I/O-bound tasks).
Multiprocessing → Multiple processes have separate memory spaces(different CPU cores), run independently (better for CPU-bound tasks).


🔹 I/O-bound tasks
Tasks spend most time waiting for input/output (network, disk, database).
CPU is mostly idle while waiting → threads shine here because they can switch while one waits.
Real examples:
Downloading files from the internet (waiting on network).
Reading/writing large files from disk.
Querying a database.
API calls (like your requests.get).

🔹 CPU-bound tasks
Tasks spend most time crunching numbers or doing heavy computation.
CPU is fully occupied → multiprocessing is better because it can spread across cores.
Real examples:
Image processing (resizing, filtering).
Video encoding/decoding.
Machine learning model training.
Complex mathematical simulations (e.g., Monte Carlo, matrix multiplications).
"""