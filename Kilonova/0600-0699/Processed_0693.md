
Lensu has a very large garden and wants to water all the $N$ plants placed in a line next to his fountain. To avoid wilting by the evening, each plant $i \\ (i \in {1, 2, \dots, N})$ must receive at least $c_i$ drops of water. He doesn't want to waste time, so he asked the robotics team to help build a robot that will do all the work for him.

Although they worked a lot on the robot, its algorithm is very peculiar. From the spot it is in, our robot will water with one drop each second of idleness all the plants in the interval delimited by the nearest plant on the left with a required amount strictly less than the current plant's required amount and the nearest plant on the right with a required amount strictly greater than the current plant's required amount. If there is no such plant on the left, the robot will water up to plant $1$, and if there is no such plant on the right, the robot will water up to plant $N$.

In the morning, Lensu will give the robot $K$ data of the type:
$X_i$ - the spot where the robot will idle
$T_i$ - how long (in seconds) it will idle there

# Task

Lensu, passionate about algorithms, senses that the robot is not as efficient as he would like it to be and asks for your help to answer the following question: 

Knowing that the robot doesn't stop watering a plant once its capacity is reached, thus wasting water if it remains within its action range, what is the maximum number of plants Lensu could save from wilting if he redistributes the wasted drops to other plants?

# Input data

The first line contains the number $N$, the second line contains the $N$ required amounts for each plant, the third line contains the number $K$, representing the number of data points, and the following $K$ lines contain two numbers $X_i$ and $T_i$, with the meaning described in the statement. The numbers on the same line are separated by a space.

# Output data

The first line will contain a single number, the answer to the question.

# Constraints and clarifications

* During the transition from one spot to another, the robot does not water any plant
* $N \leq 300\ 000$
* $K \leq 150\ 000$
* $c_i \leq 1\ 000\ 000, \\ (i \in {1, 2, ..., N})$
* $T_i \leq 1\ 000\ 000, \\ (i \in {1, 2, ..., K})$
* $1 \leq X_i \leq N, \\ (i \in {1, 2, ..., K})$
* For $20$ points, $1 \leq N \leq 200$

# Observation

Due to the large input size, the following instructions should be used at the beginning of the code:

```c++
ios_base::sync_with_stdio(false);
cin.tie(nullptr);
cout.tie(nullptr);
```

# Example

`stdin`
```
10
3 2 5 1 8 0 4 10 5 3              
4
4 3
7 1
5 2
1 3
```

`stdout`
```
4
```

## Explanation

The robot will execute the first command and water the plants from position $1$ to position $5$ for $3$ seconds (since there is no plant on the left with a smaller capacity than plant $4$, it will start watering from the first plant, and the nearest plant on the right with a capacity greater than plant $4$ is plant $5$, having a capacity of $8$).
The robot will execute the second command and, analogously, following the presented algorithm, will water the plants from position $6$ to position $8$ for one second.
The robot will execute the third command and water the plants from position $4$ to position $8$ for $2$ seconds.
The robot will execute the last command and water the plants from position $1$ to position $3$ for $3$ seconds.
At the end of the operations, each plant will be watered for:
$6 \\ 6 \\ 6 \\ 5 \\ 5 \\ 3 \\ 3 \\ 3 \\ 0 \\ 0$ seconds.
It is observed that $15$ drops are wasted, which we can redistribute to save a maximum of $4$ plants.
