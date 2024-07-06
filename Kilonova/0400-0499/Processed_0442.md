To avoid logistical issues, the preparation committee of this year's team decided to establish the ranking of the `N` participants independent of the scores obtained in the two contest tasks.

Fortunately for you, however, there is a **mole**, whose name we won't mention, who revealed this secret to you, so you learned about the committee's malicious intentions. Moreover, the person is willing to help you uncover the ranking. However, to avoid being discovered, you decided to communicate as follows:
1. You will ask the mole a possible ranking $p_1 \\ p_2 \\ ... \\ p_N$;
2. The mole will start from the ranking you asked and transform it into the committee's ranking by swapping the positions of two participants at a time. Let's assume that the minimum number of swaps is `x`. The mole will answer your question with `x`.

Since each question asked poses a risk of the person being discovered, you want the questions asked between you to not be too many (see the **Scoring** section), but, of course, you want to eventually discover the ranking established by the committee.

# Interaction
**This problem is interactive**. The `mole.h` file defines the function with the following header:
```cpp
int ask(std::vector<int> guess)
```

**Attention! This function does not need to be implemented by you.** The grader will implement this function. The argument `guess` represents the ranking you will ask about. The function will return the minimum number of swaps `x` described above. The argument `guess` must represent a valid permutation of the numbers in the interval `[1, N]`. Otherwise, the grader will terminate the program from execution and mark the test as incorrect.

# Implementation details
You will implement the function with the following header:
```cpp
std::vector<int> find_standings(int N)
```
The `find_standings` function will be called once. `N` is the number of participants.

The function must eventually return the sought ranking. For this, within it, you can call the interaction function `ask` a limited number of times (see the **Scoring** section).

# Scoring
## Subtask 1 (7 points)
* `3 \leq N \leq 6`
* The `ask` function can be called at most `1 000` times.
## Subtask 2 (14 points)
* `3 \leq N \leq 100`
* The `ask` function can be called at most `5 000` times.
## Subtask 3 (40 points)
* `3 \leq N \leq 200`
* The `ask` function can be called at most `4 000` times.
## Subtask 4 (16 points)
* `3 \leq N \leq 200`
* The `ask` function can be called at most `2 700` times.
## Subtask 5 (15 points)
* `3 \leq N \leq 200`
* The `ask` function can be called at most `1 800` times.
## Subtask 6 (8 points)
* `3 \leq N \leq 200`
* The `ask` function can be called at most `1 600` times.

## Grader model
The grader will start by reading from the console the input data in the following format:
* line 1: `N`, representing the number of participants
* line 2: $s_0 \\ s_1 \\ ...  \\ s_{N-1}$ (separated by spaces), representing the secret ranking

For each call of the `ask` function, the grader will display the function argument, then read the answer to the question from the console.

If your program completes successfully, the grader will display:
* the message `OK [Q]`, where `Q` is the number of questions asked, if the returned solution is correct,
* the message `WA`, if the returned solution is incorrect.

# Example
* Committee : `find_standings(3)`
* Contestant : `ask({1, 2, 3})`
* Committee : `2`
* Contestant : `ask({1, 3, 2})`
* Committee : `1`
* Contestant : `ask({2, 3, 1})`
* Committee : `0`
* Contestant : `return {2, 3, 1}`
* Committee : `OK 3`
