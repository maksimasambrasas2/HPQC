# HPQC
=======
Topic 2: Performance and Parallelism
How to Run
Compile C programs

gcc src/write.c -o bin_write
gcc src/read.c -o bin_read

Run programs

Python:
python3 src/write.py 1000
python3 src/read.py

C:
./bin_write 1000
./bin_read

To measure execution time:
time python3 src/write.py 1000
time ./bin_write 1000



## Results

| Program | Operation | Input | Internal Time (s) | Real Time (s) |
|--------|----------|-------|------------------|--------------|
| Python | repeat_adder | 1000,10 | N/A | 0.034 |
| Python | repeat_adder | 100000,10 | N/A | 0.035 |
| C | repeat_adder | 1000,10 | N/A | ~0.004 |
| C | repeat_adder | 100000,10 | N/A | ~0.004 |
| Python | write file | 100 lines | 0.00022 | 0.028 |
| Python | write file | 1000 lines | 0.00046 | 0.03 |
| C | write file | 100 lines | 0.000038 | ~0.004 |
| C | write file | 1000 lines | 0.00023 | ~0.004 |
| Python | read file | 100 lines | 0.00013 | 0.028 |
| C | read file | 100 lines | 0.0001 | ~0.004 |



Conclusion

The performance of C and Python programs was compared using both the Linux time command and internal timing methods.

For small programs, there was little visible difference in runtime because the execution times were very short. However, for repeated calculations such as the repeat_adder program, runtime depends mainly on the number of loop iterations. One input affects performance much more than the other because it controls how many times the loop runs.

Overall, C programs were consistently faster than Python programs. This is because C is a compiled language, while Python is interpreted and has extra overhead when running. This difference is especially noticeable in file operations, where Python takes longer due to interpreter startup time.

The internal timing results showed that writing and reading files takes longer as the number of lines increases, although the increase is small for the file sizes used. File input/output also involves system-level operations, which contributes to runtime.

In conclusion:

C is faster than Python for most operations
runtime increases with input size, especially in loops
file operations add extra overhead
internal timing measures specific parts of code, while the time command measures total runtime
>>>>>>> 51a86b7b775b8ff8f28130ded1e20c54a148b420
