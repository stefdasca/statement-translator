## Task

Hey, look, you're on the committee again. You don't like being on the committee. It's stressful, and people direct insults at you; the insults become hashtags, and the complaints become memes. What a life. The entire committee agrees that every year there needs to be a 100% classic problem. You don't even remember what your opinion on this was. The fact is that you were given the task of creating the tests for the next problem: <You are given an array of $N$ numbers and $M$ queries of the form "what is the maximum value in the subarray $[x, y]$? ". Answer the queries with an RMQ.> The work for preparing this problem was parallelized (more like paralyzed, am I right?) in the following way: one person constructs the sequence of numbers. Another person decides the number of queries and their answers. And you effectively choose the queries for which these answers are obtained. Intelligent, isn't it? Since you don't want the most unhappy brutes to enter, you want the sum of the lengths of the queries you propose to be as large as possible. Additionally, since there are people out there who memoize for this kind of problem, you want all the queries to be distinct.

## Input data

The input file `queries.in` will contain on its first line the number $T$, representing the number of tests. The structure of a test is as follows:
the first line contains the numbers $N$ and $M$, representing the number of numbers in the array, respectively the number of queries you will create.
Next comes a line with $N$ numbers, representing the values in the array.
Then follows a line of $M$ numbers, representing the answers that these queries should produce.

## Output data

The output file `queries.out` will contain $T$ lines, each containing a single integer, representing the maximum possible total length of queries that meet the input conditions. In case such a set of queries does not exist, you will print $-1$ and treat your colleagues with even less respect.

## Constraints and clarifications

$1 \leq T \leq 10$  
$1 \leq N, M \leq 10^5$  
$1 \leq$ values in array $\leq 10^9$

## Example

`queries.in`
```
2
5 3
1 2 5 2 1
5 5 5
5 3
4 5 3 2 5
5 5 5
```

`queries.out`
```
13
-1
```