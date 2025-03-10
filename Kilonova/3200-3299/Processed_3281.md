
~[Joker1.png|align=center|width=30%]
$$
\text{The abilities described below for this Joker are not canonical.}
$$

You are playing a game with **J**ok**e**_r_. He has given you a number $N$ ($5 \le N \leq 1 \ 000$), and he mentioned that he has two hidden numbers $L$ and $R$ ($0 \leq L \leq R \leq N - 1$). The goal of the game is to find these numbers. You have determined that to achieve this goal, you can ask him questions of the following form:

> I give you an array of $N$ numbers $a_0, a_1, \dots, a_{N - 1}$. Tell me what is the minimum of the numbers $a_L, a_{L + 1}, \dots, a_R$.

However, there is a problem: In **J**ok**e**_r_'s native language, there is no word for minimum; rather, he understood the word _extreme_. Thus, he will answer each question with either the **maximum** or **minimum** of the segment $[L, R]$ from the array you have given him. Moreover, he might respond with the maximum or minimum just to confuse you further.

**J**ok**e**_r_ acknowledges that this game is probably too difficult to win on your own. Therefore, he considers any pair of numbers $(L', R')$ a _correct_ answer, as long as it satisfies:

> $|L - L'| + |R - R'| \le 1$, where $|a|$ denotes the absolute value of number $a$.

# Task

In light of this information, you must do everything possible to find an answer that meets **J**ok**e**_r_'s correctness criterion with the minimum number of questions.

# Interaction

Participants have access to the following functions to interact with **J**ok**e**_r_:
* The following function receives an array of numbers $a_0, a_1, \dots, a_{N-1}$ and returns either the **minimum** or **maximum** on the segment $[L, R]$ of the given array, chosen arbitrarily by **J**ok**e**_r_:
```cpp
int query(std::vector<int> a);
```
* Participants must call this function to provide the final answer with the presumed correct pair $(L, R)$ that they have deduced:
```cpp
void answer(int L, int R);
```

Participants are required to implement only the `solve` function, which is called to resolve the game. You do not need to implement the `main` function. The source code should begin with
```cpp
#include "joker.h"
```
and implement only the function `solve(int N);`
**Important:** All of the participant's code should be written in `solutie.cpp`. There, participants can define global variables and their own functions to facilitate solving the problem.

# Attached Files

Participants have access to the following files:
* `joker.h` - the header that defines the interaction functions (`query` and `answer`) required for implementation.
* `sample_submission.cpp` - a simple implementation example which executes a query and always answers with $L = R = 0$.
* `Lgrader.cpp` - a testing grader for participants, not used officially, which can help them verify the code.

## Using Lgrader in Code::Blocks

To use `Lgrader.cpp` in Code::Blocks:

1. Create a new project.
2. Add a file named `solutie.cpp` (select `File > New > Empty File`) where you will write the solution code.
3. Add an empty file named `joker.h` and copy the content from the attached `joker.h`.
4. Copy the content from `Lgrader.cpp` into `main.cpp` to simulate running the solution.

After this setup, write the implementation of the `solve` function in `solutie.cpp`. To test the configuration, you can initially copy the code from `sample_submission.cpp` into `solutie.cpp`. Then, press F9 or select **Build and Run** to compile and run the program.

When running, the program will read the values $N$, $L$, and $R$, and it will simulate the interaction between `Lgrader` and the participant's solution, displaying the answers to the queries made through `query` and validating the final answer provided through `answer`.

# Interaction Example

Consider $N = 5$ and the hidden values $L = 1$, $R = 3$. The segment $[L, R] = [1, 3]$ corresponds to the subarray $\{3, 8, 1\}$ from the input array. The grader will call the function `solve(5)`.

From inside the `solve` function, if the participant calls:
```cpp
int query({5, 3, 8, 1, 6});
```

The output will be either `1` (**minimum**) or `8` (**maximum**) on the segment $[L, R] = [1, 3]$, chosen arbitrarily by **J**ok**e**_r_.

If the participant calls:
```cpp
answer(1, 3);
```

The output will be:
```
Correct
```

The participant will receive a score calculated according to the evaluation formula from the **Grading** section.

# Grading

Let $Q_{participant}$ be the number of queries used by your solution and $Q_{optim}$ the minimum number of queries. Let $x = \frac{Q_{participant} - Q_{optim}}{Q_{optim}}$. 

**Attention!**, you cannot make more than $10\,000$ queries per test.

The score received on a test is
$$
0.2 + \frac{0.2}{e^{2x} + 1} + \frac{0.7}{1 + x}
$$
