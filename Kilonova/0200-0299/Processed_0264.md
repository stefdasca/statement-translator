# Translation

The Romanian Intelligence Service (SRI) has tracked down a notorious and dangerous terrorist organization that is headquartered within our country's borders. By employing the most skilled and well-trained spies and officers, SRI managed to identify the main computer of the terrorist organization. If they succeed in accessing the information from this computer, SRI will be able to arrest all members of the organization and ensure (continuing) world peace. The only problem is cracking the access code. All that is known about this code is that it is represented by a permutation of length `N`. SRI specialists have tried various methods to discover the code, but all they managed to obtain is a program that, given a permutation of length `N` as a parameter, specifies the number of positions where this permutation and the access code match. Unfortunately, the chiefs do not believe in the usefulness of this program.

# Task
Write a program that, using the helper program (represented as a module), determines the access code to the terrorists' computer.

# Interaction Protocol

You need to implement the following function, where `N` is the length of the permutation.

```cpp
std::vector<int> solve(int N)
```
\
Your program will not read data from any input file. It will only call the function 

```cpp
int check(std::vector<int> p) 
```
\
to which, each time, a permutation `p` of length `N` indexed from `0`, with elements between `1` and `N` will be transmitted as a parameter. This function will return the number of positions where the permutation transmitted as a parameter matches the permutation to be discovered. If `p` is not a valid permutation, `check` will return `-1`; otherwise, a number between `0` and `n`. Your program must, after a finite number of calls to the `check` function, discover the sought permutation. The complexity of the function will be considered `O(n)`.

Finally, the function will return a permutation of length `N`, indexed from `0`, with elements between `1` and `N` representing the solution to the problem.

# Constraints and clarifications
* `5 \ \leq N \ \leq 650`
* The file "check.h" must be included
* The problem has been modified

## Subtask 1 (10 points)
* `5 \ \leq N \ \leq 10`
## Subtask 2 (50 points)
* `5 \ \leq N \ \leq 500`
## Subtask 3 (40 points)
* `5 \ \leq N \ \leq 650`

# Example
```
5
2 1 3 4 5
```

A possible series of calls to the `check` function is as follows:
* The `check` function is called with the permutation `(1 2 3 4 5)` and returns the value `3`
* The `check` function is called with the permutation `(3 2 1 4 5)` and returns the value `2`
* The `check` function is called with the permutation `(2 1 3 4 5)` and returns the value `5`

Finally, `solve` will return the permutation `(2 1 3 4 5)`