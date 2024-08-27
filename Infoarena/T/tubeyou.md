# Tubeyou

After watching a particular video $x$ on YouTube (with a duration of $durata[x]$ seconds), the next recommended video starts after $K$ seconds, which is the video $next[x]$. However, you are not on YouTube but on a site with a poorly implemented recommendation system.

## Task

There are $Q$ operations that need to be processed in order:

- **Update video watching**: A number $x$ is given, the index of a video you watch. Now, every video $y$ that had $x$ as the next recommendation ($next[y] == x$), changes its recommendation to the video recommended for $x$ ($next[y]$ becomes $next[x]$).

- **Query**: Marcel asks you a purely statistical question: Two numbers $a$ and $b$ are given. You open videos $a$ and $b$ simultaneously in two tabs. Marcel asks in how much time a video will start in one tab that has already started in the other tab. In particular, if $a == b$, the answer is $0$. The question is statistical and the execution of the action is purely hypothetical, meaning the updates corresponding to watching the videos do not occur (the array $next[i]$ does not change neither during nor after the query).

## Input data

The input file `tubeyou.in` contains the number $N$ of videos, the number $K$ of seconds between the end of one video and the start of the next, and the number $Q$ of operations on the first line, separated by a space. The next line contains the $N$ numbers, $next[i]$, separated by a space. The following line contains $N$ numbers, $durata[i]$, separated by a space.

On the next $Q$ lines, more numbers will be found, starting with the number $t$, which can be $0$ or $1$. 
- If $t$ is $0$, a single number $x$ follows, and an update operation with parameter $x$ is performed.
- If $t$ is $1$, two numbers $a$ and $b$ follow, and a query operation with parameters $a$ and $b$ is performed.

## Output data

The output file `tubeyou.out` will contain several lines. On each line will be the answer for each query, in the order they appear in the input. If the answer to the question is infinite, the number $10^{18}$ will be displayed, as in the example.

## Constraints and clarifications

$1 \leq next[i], a, b, x \leq N$ 

$0 \leq K \leq 10^9$ 

$1 \leq durata[i] \leq 10^9$ 

$1 \leq N, Q \leq 250\,000$ 

For $10$ points, $1 \leq N, Q \leq 1\,000$  
- feedback test 1

For another $45$ points, $1 \leq N, Q \leq 50\,000$  
- feedback tests 3, 7, 10

The rest of the feedback tests are part of the largest tests

## Example

`tubeyou.in`  
```
32 0 54 
3 14 20 23 4 4 4 2 8 8 10 10 12 19 25 25 27 17 24 24 23 15 14 2 22 17 16 17 22 15 31 31 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 7 1 9 14 1 21 13 1 12 9 1 20 8 1 5 6 1 23 19 1 6 11 1 10 3 1 2 4 1 11 13 1 21 5 1 24 14 1 29 30 1 18 26 1 28 16 1 16 30 1 27 22 1 28 29 1 30 25 1 15 17 1 31 31 1 31 32 1 32 10 0 4 0 24 0 14 0 27 0 31 0 32 1 7 1 1 14 9 1 13 21 1 9 12 1 8 20 1 6 5 1 19 23 1 11 6 1 3 10 1 4 2 1 13 11 1 5 21 1 14 24 1 30 29 1 26 18 1 16 28 1 30 16 1 22 27 1 29 28 1 25 30 1 17 15 1 31 31 1 32 31 1 10 32 5 3 5 2 2 1 2 4 3 2 2 2 2 1 3 2 2 4 2 3 0 1 1000000000000000000 3 2 4 2 1 1 1 3 2 2 2 1 2 2 1 2 2 2 3 2 2 0 1 1000000000000000000
```

`tubeyou.out`
```
0
0
0
0
15
...
```