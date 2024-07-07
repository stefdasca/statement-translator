
A sequence of $1 \ 048 \ 576$ $(2^{20})$ elements, which are integers, is considered. We define the following concepts:
- a plateau as a sequence of equal elements located in consecutive positions in an array;
- the length of a plateau as the number of elements that make up the plateau.

It is known that in the given sequence, the maximum length of a plateau is $8192$ $(2^{13})$, and there is at least one plateau of this length. The placement of a plateau is determined by the smallest and largest positions among the positions of the elements that make up the plateau.

# Task

Write a program that determines the placement of a plateau of length $8192$ in the given sequence. You do not know the sequence. The placement of the plateau is determined by asking questions to the committee. A question consists of specifying two positions in the sequence, namely $p_1$ and $p_2$. The committee will give you a response representing the largest length of a plateau in the sequence between positions $p_1$ and $p_2$.

# Interaction

Your program will not read or write from/to any file and will not implement the main function. Instead, it will implement the function:
```cpp
std::pair<int, int> solve();
```
which will return a pair $(p_1, p_2)$ where $p_1$ and $p_2$ represent the positions that determine the placement of a plateau of length $8192$ in the sequence. To find details about the given sequence, you can call the function:
```cpp
int ask(int p1, int p2);
```
where $p_1$, $p_2$ represent the positions for which you make the query, and the function returns a value representing the largest length of a plateau found between positions $p_1$ and $p_2$.

# Constraints and clarifications

* The positions in the sequence are numbered from $1$ to $1 \ 048 \ 576$.
* The file `platou.h` must be included.
* It is guaranteed that you will receive a response to $20$ questions without exceeding the time limit.

# Scoring
Your program receives $0$ points on a test if:
- it uses more than $20$ queries;
- it queries with incorrect positions: positions smaller than $1$ or larger than $1 \ 048 \ 576$ or the first position is strictly greater than the second position.
- it returns an incorrect response

Otherwise, your program receives a score that depends on the number of questions as follows:
- for at most $11$ queries, it obtains $100\%$ of the score;
- for a number of queries between $12$ and $15$, it obtains $50\%$ of the score;
- for a number of queries between $16$ and $20$, it obtains $25\%$ of the score.

# Example
* Call `ask(1, 8192)`, to query the maximum length of a plateau found between positions $1$ and $8192$.
* The function returns $8192$, meaning the maximum length is $8192$.
* `solve` returns $(1, 8192)$, because we know that a plateau with a length of $8192$ is located between positions $1$ and $8192$.
