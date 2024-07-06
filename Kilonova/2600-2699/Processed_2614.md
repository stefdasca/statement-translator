Magician Marcel, from the land "closer to here, but farther beyond", has come to the king's palace to perform his astonishing magic show... mathematics.

He has hidden a sequence of $N$ natural numbers in his magic hat, and the king has to guess the chosen sequence. Marcel allows him to ask questions, specifically the king can ask what the sum of a continuous subarray of the sequence is. Formally, the king can find the sum $S = a_l + a_{l+1} + \ldots + a_{r-1} + a_r$ for any $1 \leq l < r \leq N$. But Marcel is demanding and asks the king to use at most $N$ such questions.

# Task

Help the king determine the sequence hidden by magician Marcel by writing a program.

# Interaction Protocol

The contestant's program must implement the function with the following signature:
```cpp
std::vector<int> solve(int N);
```
The function receives as parameter the number of elements in the sequence and must return a vector of exact dimension **$N + 1$**, the $N$ elements being **indexed from 1**.
The program will include the header `magie.h` which will contain the definition of the following function:
```cpp
int query(int left, int right);
```
The function will receive as parameters the left and right ends of the subarray for which the sum is to be found. If the interval is invalid (*left* or *right* are indices outside the array or the strict condition is not met), the program will stop its execution, and the verdict will be wrong answer.

# Constraints and clarifications

* $3 \leq N \leq 10\ 000$
* $1 \leq a_i \leq 10\ 000 \ \forall \ i, \ 1 \leq i \leq N$
* The interactor is **not** adaptive. The sequence of numbers is fixed from the start of the program's execution.
* During the contest, the interaction was performed through `stdin/stdout`.
* The scores for groups have been modified from those in the contest.

|#| Score | Constraints|
|-|-------|------------|
|1|8|$N = 3$, $1 \leq a_i \leq 25 \ \forall \ i, \ 1 \leq i \leq N$|
|2|4|$N = 5$, $1 \leq a_i \leq 25 \ \forall \ i, \ 1 \leq i \leq N$|
|3|24|All values in the sequence are equal|
|4|64|No other constraints|

# Example of interaction

We have $N = 6$
* The call `query(1,5)` returns 20.
* The call `query(5,6)` returns 30.
* The program returns the array $\{1, \ 3, \ 4, \ 2, \ 10, \ 20\}$.

