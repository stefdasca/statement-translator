## Task

All children dream at some point of an ideal career from their point of view. Didn't you always want to work at the City Hall Archive? Probably not, but for the purposes of this problem, we will assume this. More specifically, your function at the City Hall is to maintain the genealogical tree of the city and answer citizens' unnecessary questions. Thus, your actions in a day are divided into two types: 0 Record that citizen $Y$ has a new child, and their name is $X$. 1 Tell citizen $X$ who is their $Y$-th ancestor. We don't know why they don't ask their own parents or why they don't use their time more productively, but that's not your problem! Initially, the only citizen in the city is citizen 1, and it is guaranteed that all other citizens will be their descendants. Each child will have a single parent, and the total number of citizens at the end of the day will be $N$. The total number of requests, regardless of their type, will be $M$. 

## Input data

The input file `citylog.in` will contain on its first line two numbers, $N$ and $M$. The next $M$ lines will be of the form $TIP \ A \ B$, where $TIP$ denotes the type of question, and $A$ and $B$ are the numbers with which you will obtain the requests, as follows: $X = A \ \text{xor} \ current$ $Y = B \ \text{xor} \ current$ The variable $current$ represents the value of the last response to a type 1 request. Initially, $current = 0$. 

## Output data

The output file `citylog.out` will contain the answers to type 1 requests. If citizen $X$ does not have a $Y$-th ancestor, the answer will be 0.

## Constraints and clarifications

1 $\leq N \leq 10^{5}$

1 $\leq M \leq 10^{6}$

Due to weather conditions endured by the evaluator, City Hall Infoarena suggests using stream reading for this problem.

## Example

`citylog.in`

```
5 10
0 2 1
0 3 2
1 1 1
0 1 2
3 0
5 0
1 5 0
0 4 2
1 4 2
1 4 0
1 6 7
1 1 3
```

`citylog.out`

```
1
1
2
1
```