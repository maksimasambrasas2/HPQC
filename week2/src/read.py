import time

filename = "../data/test_python.txt"

start_time = time.time()

with open(filename, "r") as f:
    contents = f.read()

end_time = time.time()

run_time = end_time - start_time
print(f"Read {len(contents)} characters from {filename}")
print(f"Internal runtime: {run_time:.6f} seconds")

