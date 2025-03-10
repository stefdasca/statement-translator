After too many vacations in Dubai, Dorel has ended up with no money left in his piggy bank. As a result, Dorel has become a courier at the company CC (Costel Couriering). Dorel has always been special, so he doesn't want to be a courier like all the others, delivering packages by car, but instead he wants to use an airplane to deliver them directly to the clients' doorsteps. Because he had no money left, he bought the cheapest (worst) airplane he could find. The airplane has a major downside: if Dorel wants to deliver a package to house number $i$, he will automatically also deliver to houses $i+1, i+2, ..., i+K-1$, for a fixed $K$. A delivery to houses $i, i+1, i+2, ..., i+K-1$ is called a trip $(i \leq N-K+1)$.

# Task

Dorel’s boss (Costel) has a new mission for him: he has to deliver packages to $N$ houses (numbered from $1$ to $N$). The house with number $i$ expects $a_i$ packages. The boss is very strict, so each house must receive exactly $a_i$ packages, otherwise Dorel will be fired (and he won't be able to go on vacations to Dubai anymore)!

Dorel’s friend, Mirel, hearing about his mission, asks him $Q$ questions in the form of ***"Can you complete your mission with an airplane with this $K$ ?"***. Not knowing how to answer these questions, Dorel hired you to help him (if you succeed, you'll be able to go on vacation to Dubai with him!).

# Input data

The first line contains three integers, $T$, $N$ and $Q$ (the number of tests, the number of houses, and the number of questions from Mirel, respectively).
Each of the following $Q$ lines contains $K$, specific to each question from Mirel.
The next $T$ lines contain $a_1, ..., a_N$ (the number of packages expected by each house for a specific test).

# Output data

You will print $T$ lines, each containing the answer for the corresponding test.
The first number on each line will be $M$, the number of answers to Mirel's questions that are **YES**. Following that, you will print $M$ numbers, the indices of the questions for which the answer is **YES**, in increasing order.

# Constraints and clarifications

* $1 \leq T \leq 30$;
* $1 \leq N \leq 10^4$;
* $1 \leq Q \leq 10^6$;
* $1 \leq K \leq N$;
* $0 \leq a_i \leq 10^9$;
* $N$, $Q$ and Mirel's questions are the same for all tests in an input;
* For fast input and output, it's recommended to use these lines of code at the beginning of the `main` function:
```cpp
ios::sync_with_stdio(false);
cin.tie(NULL);
cout.tie(NULL);
```

| # | Points | Constraints |
| - |:-------:|:----------:|
| 1 | 10      |    $Q \leq 10$, $N \leq 20$ and $a_i \leq 1 \ 000$   |
| 2 | 20      |    $Q \leq 10$ and $N \leq 1 \ 000$  |
| 3 | 30      |    $Q \leq 100$  |
| 4 | 20      |    $Q \leq 10^4$  |
| 5 | 20      |    No additional constraints  |

# Example

`stdin`
```
2 4 3
2
3
4
1 3 3 2
10 10 10 10
```

`stdout`
```
1 2
2 1 3
```

## Explanation

For the first test, the answer to the first and last question is **NO**.
For the second question, $K = 3$. One possible solution is to deliver first to houses $1, 2, 3$, then twice to houses $2, 3, 4$. Thus, we have delivered the exact number of packages to all houses, so the answer to this question is **YES**.

For the second test, the questions for which the answer is **YES** are the first and the third.