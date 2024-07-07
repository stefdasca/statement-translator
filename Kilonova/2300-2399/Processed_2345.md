
# Statement

Given a triplet $(x, y, z)$ where $x, y, z \in \{1, 2, ..., n\}$.
To find the triplet, we can ask questions in the form:
`ask(a, b, c)`
with the meaning: "Is the triplet $(x, y, z)$ equal to the triplet $(a, b, c)$?" (where $a, b, c \in \{1, 2, ..., n\}$).
The answer to such a question is $1$ if at least two values from the set $\{x - a, y - b, z - c\}$ are zero, otherwise $0$.

# Task

Determine the triplet $(x, y, z)$ without exceeding a specified maximum number of questions.

# Interaction Protocol

Your program will not read or write any files. Instead, it must implement the function
```cpp
std::vector<int> solve(int n, int m);
```
which will receive as parameters $n$ - with the significance above and $m$ - the maximum number of allowed queries. The function will return a vector containing the requested triplet. Inside the function, you can call the function
```cpp
int ask(int a, int b, int c);
```

# Constraints and clarifications
* The function will be called at most 5 times within a test.
* $1 \leq n \leq 500$
* The maximum number of queries $m$ is $O(n^2)$, with a subunitary constant.
* The order of values in the triplet matters $((1,1,2) \neq (1,2,1))$.
* You must include the file `treinr.h`

# Scoring
The score for a test will be zero if:
* The runtime limit is exceeded
* The interaction protocol is not followed
* The answer is incorrect for at least one data set
* The maximum number of allowed questions $m$ is exceeded.
