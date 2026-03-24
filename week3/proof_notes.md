# Notes on proof.c

## Overview

`proof.c` is an MPI program that uses multiple processes to calculate partial results and combine them into one final answer.

The program works like this:
- process 0 is the **root**
- all other processes are **clients**
- each client multiplies its rank by the numerical input argument
- each client sends its result to the root
- the root receives all client results and adds them together
- the root prints the combined result

---

## Function-by-function breakdown

## main()

The `main()` function controls the overall structure of the program.

### What it does
1. Declares an error-handling variable called `ierror`
2. Reads and checks the command-line argument using `check_args()`
3. Starts the MPI environment with `MPI_Init()`
4. Declares and initialises:
   - `my_rank` = the rank of the current process
   - `uni_size` = the total number of MPI processes
5. Uses:
   - `MPI_Comm_rank()` to get the rank
   - `MPI_Comm_size()` to get the total number of processes
6. Checks that the communicator size is valid using `check_uni_size()`
7. Chooses the correct task for the process using `check_task()`
8. Ends the MPI environment using `MPI_Finalize()`

### Simple pseudocode
```text
main:
- set up variables
- read numerical input
- start MPI
- get rank and total number of processes
- check communicator size
- choose task based on rank
- end MPI
