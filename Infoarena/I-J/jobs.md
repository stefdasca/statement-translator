## Jobs

## Task

In a factory, there are $2$ activities that need to be carried out. The first activity consists of $S_1$ consecutive identical steps, and the second activity consists of $S_2$ consecutive identical steps. In the factory, there are $N$ people working. Each person can perform any step of either of the $2$ activities. For each person $K$, the times $T_{1,K}$ and $T_{2,K}$ are known, which represent the time required for that person to perform a step of the first and second activity, respectively. Each step of either of the $2$ activities must be performed by exactly one person. A person can perform multiple steps from both activities but only one step at any given moment. The execution of the $2$ activities is considered to start early in the morning after all $N$ workers have arrived at the factory (at time $0$). Once a worker has started performing one of the steps, they cannot be interrupted until they finish the step. Breaks (waiting times) can only exist before the beginning of the execution of each step of either of the $2$ activities. Consider the moment $TA_1$ when the execution of the last step of the first activity ends and the moment $TA_2$ when the execution of the last step of the second activity ends. The factory director wants to minimize the sum $TA_1 + TA_2$. Write a program that determines the minimum value for the sum $TA_1 + TA_2$.

## Input data

The first line of the input file `jobs.in` contains the number of test data sets $T$ in the file. The following lines describe the $T$ data sets. The first line of each set of data contains $3$ natural numbers separated by a space: $N \ S_1 \ S_2$, which represent the number of people working at the factory, the number of steps of the first activity, and the number of steps of the second activity, respectively. The next $N$ lines of the test data set each contain $2$ integers separated by space: $T_{1,K}$ and $T_{2,K}$ with the significance given in the statement. There will be a blank line before each test data set in the file.

## Output data

The output file `jobs.out` will contain $T$ lines, one for each set of test data in the input file. Each line $i$ will contain the minimum possible value for the sum $TA_1 + TA_2$ for the $i$-th set of test data.

## Constraints and clarifications

$1 \leq T \leq 20$  
$1 \leq N \leq 100$  
$1 \leq S_1, S_2 \leq 7$  
$1 \leq T_{1,K}, T_{2,K} \leq 1\ 000\ 000$  

## Example

`jobs.in`  
```
4

1 2 3
10 20

3 5 7
10 20
15 16
17 18

4 3 6
10 12
8 9
16 11
13 20

4 4 6
7 12
5 3
6 5
1000000 1000000
```

`jobs.out`  
```
100
162
84
41
```

## Explanation

In the first data set, the first (and only) worker performs the first $2$ steps of the first activity and finishes at time $20$ $(TA_1 = 20$). Then, starting from time $20$, he performs the $3$ steps of the second activity and finishes at time $80$ $(TA_2 = 80)$. The answer is $20 + 80 = 100$.

In the second data set, worker $#1$ performs all $5$ steps of the first activity, finishing at time $50$, and worker $#2$ performs all $7$ steps of the second activity, finishing at time $112$. The answer is $50 + 112 = 162$.

In the third data set, worker $#1$ performs all $3$ steps of the first activity, finishing at time $30$, and worker $#2$ performs all $6$ steps of the second activity, finishing at time $54$. Thus, the answer is $30 + 54 = 84$.

In the fourth data set, worker $#2$ performs all $6$ steps of the second activity, finishing at time $18$ $(TA_2 = 18)$. Starting from time $0$, worker $#3$ performs the first $3$ steps of the first activity, finishing at time $18$ (what a coincidence :) ). Then, the $4$-th step of the first activity is performed by worker $#2$, from time $18$ to time $23$ $(TA_1 = 23)$. Thus, the answer is $18 + 23 = 41$.