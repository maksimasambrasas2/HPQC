import sys
import time

if len(sys.argv) != 2:
    print("Usage: python3 write_file.py <num_lines>")
    sys.exit(1)

num_lines = int(sys.argv[1])
filename = "../data/test_python.txt"

start_time = time.time()

with open(filename, "w") as f:
    for i in range(num_lines):
        f.write(f"This is line {i}\n")

end_time = time.time()

run_time = end_time - start_time
print(f"Wrote {num_lines} lines to {filename}")
print(f"Internal runtime: {run_time:.6f} seconds")
