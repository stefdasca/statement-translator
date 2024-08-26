# Klsecv

The elf, due to excessive water consumption, fell asleep and had a frightening nightmare. He found himself in a classroom. Moreover, on the sheet in front of him, it was written “National Baccalaureate Exam – Romanian Language and Literature”. Frightened, he reads the first task. Given a poetic text formed of $N$ small characters of the English alphabet, it is required to comment on a figure of speech of length $L$. The poetic text is so meticulously composed that any sequence of length $L$ is a figure of speech. The elf wants to make a remarkable impression on the evaluation committee, so he wonders what the $K$-th most beautiful figure of speech would be. The grading system states clearly: “The stylistic splendor of the figures of speech is given by the order of the lexicographic sorting”. Confident in your skills, he asks you to find the starting position of a figure of speech for $Q$ configurations of type $L$ $K$. In case the same figure of speech appears in multiple positions, any one of them can be displayed.

## Task

## Input data

The first line of the input file contains $T$, the number of tests. The first line of each test contains the poetic text, followed by the next line containing an integer $Q$, the number of questions referring to the given string. Then follow $Q$ lines of the form $L$ $K$.

## Output data

The output file will contain the answers to all the questions of the form $L$ $K$, one per line.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N,Q \leq 20\ 000$

$1 \leq L \leq N$

$1 \leq K \leq N-L+1$

The string is indexed starting with position $1$

Note! Identical sequences can appear several times in the sorted order.

## Example

```
klsecv.in
```
```
3
mlcpet
2
3 3
3 4
agmconcursvaloare
3
6 2
4 5
2 13
spiromaniiftw
1
7 4
1 4
12 2
```
```
klsecv.out
```
```
3
6
9
5
```

## Explanation

The figures in the first text in sorted order are "cpe", "lcp", "mlc", "pet". The elf knows that "mlc" is a genuine euphemism, but the grading system thinks differently.