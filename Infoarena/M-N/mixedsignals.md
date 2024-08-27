## Task

Hoping to decipher mixed signals, Petrică has decided that he wants to understand once and for all how people socialize, so he enrolled in the Semi-circle of Anonymous Dopats. Here he found people sitting in a square, numbered from $1$ to $N$, identifying 3 types of people:
- people who always tell the truth, trusting the rest of the group
- people who always lie, always speaking falsely
- mute people, who only listen to the discussions

Being a semicircle of sociable people, there are at most $N-1$ mute people, and each person knows about any other person what type of person they are. Wanting to integrate into the group, our protagonist has decided to find out what type of person each is by asking the following questions: Petrică asks $x$ what $y$ would say if $y$ were asked what $z$ would say $\dots$ if $z$ were asked what $w$ says, where $x$, $y$, $z$, $w$ are different people in the group. For example:
- For $k = 1$, Petrică asks $x$ if $w$ is lying or not
- For $k = 2$, Petrică asks $x$ what $y$ would say if $y$ were asked if $w$ is lying or not

If any of the persons $x$, $y$, $z$, $\dots$, $w$ is mute, then Petrică will receive no response. Petrică finds out through his intuition what type of person $x$ is (he can only use his intuition no more than 5 times in one situation).

## Interaction

For each test case, several situations need to be processed. The first line will contain a natural number $T$, representing the number of situations. For each situation, the first line contains a natural number $N$, representing the number of people. Your program should ask questions by writing to the standard output:
- "1 $x$ $y$ $w$" representing a type 1 question
- "2 $x$ $y$ $z$ $w$" representing a type 2 question
- "0 $x$ $y$ $z$ $w$" representing the answer

For each type 1 or type 2 question, the interactor will respond in standard input with:
- "0" if $x$ says that $y$ says that $\dots$ always tells the truth or tells the truth (in the case of a type 2 question)
- "1" if $x$ says that $y$ says that $\dots$ always lies or lies (in the case of a type 2 question)
- "2" if among $x$, $y$, $z$, $\dots$, $w$ there is any mute person or $x$ is mute (in the case of a type 2 question).

If after any question, the answer is $2$, the question is invalid, and the program must terminate immediately. For each situation, the operation "0 $x$ $y$ $z$ $w$" will be called exactly once. Reading and displaying will be done with standard input/output. After each operation, you must display a newline character ('\n' or endl). Attempting to open any file may lead to an error in the execution of your program. Do not forget to flush the output buffer, with `cout.flush()` or `fflush(stdout)`.

## Constraints

$1 \leq T \leq 20$

$5 \leq N \leq 300$

There will always be at least $3$ people who are not mute.

At most half of the people are mute.

For a situation, the type 2 question can be called at most $5$ times.

## Scoring

The tests respect the following:

| Test number | Limit $N$ | Contains mute people | Maximum score |
|-------------|------------|-----------|---------------|
| 1           | 15         | NO        | 10            |
| 2           | 100        | NO        | 20            |
| 3           | 300        | NO        | 30            |
| 4           | 20         | YES       | 10            |
| 5           | 100        | YES       | 10            |
| 6           | 300        | YES       | 20            |

For tests that do not contain mute people, scoring is as follows, depending on the number of type 1 and type 2 questions (denoted by $Q$):
- $Q \leq N$, 100% of the score for that test
- $N < Q \leq N + 5$, 80% of the score for that test
- $N + 5 < Q \leq 2 * N + 10$, 60% of the score for that test
- $2 * N + 10 < Q$, 20% of the score for that test

For tests that contain mute people, scoring is as follows, depending on the number of type 1 and type 2 questions (denoted by $Q$):
- $Q \leq N + 15$, 100% of the score for that test
- $N + 15 < Q \leq 2 * N + 10$, 60% of the score for that test
- $2 * N + 10 < Q$, 20% of the score for that test

Using a type 2 question only grants half the score of the test.

## Example

standard input

```
1
4
2 1 0
0
‎1 2 1
2 1 2 1
3 2 1 3
2 1 2 4
0 0
```

standard output

```
1 2 1
2 1 2 1
2 1 2 4
0 0
```

## Explanation

From the first question, either $1$ or $2$ are mute. From the second question, $1$ says that $3$ is lying. From the third question, $1$ is telling the truth. From the fourth question, $4$ is telling the truth. It can be demonstrated that the only valid solution is when:
- $1$ tells the truth
- $2$ is mute
- $3$ is lying
- $4$ tells the truth