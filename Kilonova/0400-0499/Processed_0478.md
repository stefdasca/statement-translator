We are at the National Informatics Team in Deva and, since the committee is too busy preparing the problems, the `N` contestants are bored. They have started playing the game **Bolt**, which is played according to the following rules:
* All `N` participants sit in a circle in a counterclockwise order. Participant `2` sits to the right of participant `1`, participant `3` to the right of participant `2`, and so on. Participant `1` will be to the right of participant `N`.
* A special digit `C` is chosen.
* Participant number `1` starts counting (says `1`) and the others continue counterclockwise (to the right). The counting continues with participant number `2`, and so on.
* When a participant reaches a number that is a multiple of `C` or contains the digit `C` in its base `10` representation, they must say the word "fulger" instead of that number.
* Each time the word "fulger" is said, **the order of the game reverses** (if it was going counterclockwise, it will continue clockwise and vice versa).

The first `18` moves of a game with `N = 5` participants and `C = 7` are described below (the word "fulger" is marked with the letter **F**):

| Move | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|
| **Participant** | 1 | 2 | 3 | 4 | 5 | 1 | 2 | 1 | 5 | 4 | 3 | 2 | 1 | 5 | 1 | 2 | 3 | 2 |
| **Word** | 1 | 2 | 3 | 4 | 5 | 6 | **F** | 8 | 9 | 10 | 11 | 12 | 13 | **F** | 15 | 16 | **F** | 18 |

Each time someone makes a mistake, that person must drink a glass of warm milk and *the game continues* (because as you well know, milk affects the reaction speed of the participants and makes the game more fun).

Since the `N` participants are not sufficiently hindered by the warm milk, they decide to make the game even more interesting by choosing a set `S` of distinct special digits, instead of a single digit, and applying the above rules simultaneously for all digits in `S`. For example, if `S = {3, 7}`, then the participant in turn must say the word "fulger" whenever the current number is a multiple of `3` or `7` or contains the digits `3` or `7` in its representation.

Additionally, to be even better at this game, most participants calculate in advance what numbers they are supposed to say and which of these they should say "fulger". The committee, now watching, wants to know which contestant will say a given number `K` (or its corresponding "fulger", as the case may be) and rewards anyone who can answer with points.

# Task
You will implement the function with the following signature:
```cpp
int play_bolt(int N, std::string K, std::vector<int> S)
```
The function `play_bolt` will be called exactly once during a test. `N` represents the number of participants in the game, `K` is the number the committee is interested in, represented as a `std::string` (which can be very large, as there is a lot of time to waste at the team), and `S` represents the set of special digits. It is guaranteed that `S` will contain distinct non-zero digits, in strictly ascending order.

The function must return a natural number between `1` and `N`, representing the solution to the problem. Otherwise, the grader will terminate the program and mark the test as incorrect.

# Scoring
## Subtask 1 (11 points)
* $3 \le N \le 10^5$
* $1 \le K < 10^6$
* $1 \le |S| \le 9$
## Subtask 2 (50 points)
* $3 \le N \le 10^5$
* $1 \le K < 10^{12}$
* $|S| = 1$
## Subtask 3 (20 points)
* $3 \le N \le 10^5$
* $1 \le K < 10^{2000}$
* $|S| = 1$
## Subtask 4 (19 points)
* $3 \le N \le 10^5$
* $1 \le K < 10^{2000}$
* $1 \le |S| \le 9$

# Model grader
The grader will read the input data from the console in the following format:
* line 1: `N K` (separated by a space), with the specifications from the statement
* line 2: `M`, representing the number of elements in the set `S`
* line 3: `M` distinct digits between `1` and `9`, representing the set `S`

The grader will display your answer on the console, on a single line, as an integer in base `10`.

# Examples
`stdin`
```
5 10
1
7
```
`stdout`
```
4
```

`stdin`
```
5 14
1
7
```
`stdout`
```
5
```

`stdin`
```
9 1031214
1
1
```
`stdout`
```
9
```

`stdin`
```
21 410209
3
3 8 9
```
`stdout`
```
12
```

`stdin`
```
17 610305
1
7
```
`stdout`
```
9
```

`stdin`
```
17 820756190090
1
7
```
`stdout`
```
11
```

Explanation
---
Examples 1 and 2 are described in the statement. In example 3, the game will alternate between contestants `1` and `9`, because each will say "fulger" (the game proves to be quite monotonous for the other 7 contestants).

In the other cases, you will have to take our word for it.

