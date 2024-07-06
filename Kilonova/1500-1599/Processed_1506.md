~[peste.png|align=right]
Bear: Hello, cousin! How much fish do you have? Give me some, for I'm craving it!

Fox: Put your craving on hold. If you want fish, go dip your tail in the pond and you'll have something to eat.

Bear: Teach me, please, cousin, for I don't know how to catch fish.

Fox: Oh, cousin! Don’t you know that necessity teaches you things you never imagined? Go this evening to the pond and put your tail in the water. Stay still, without moving, until dawn. In the meantime, take this paper on which I have written $N$ natural numbers and by morning you must proceed as follows:

* Remove exactly two adjacent digits from each number written on the paper, so that the remaining digits form, from left to right, the largest possible number (for example, from the number $77196$, remove the digits $7$ and $1$ to obtain the largest possible number $796$).
* All the $N$ numbers obtained in the previous step, you concatenate them in any order you prefer. Looking from left to right at the digits of the concatenated numbers, you observe that a new number $X$ is formed. Be careful how you proceed because by morning, the amount of fish you catch will be proportional to the value of $X$.

Help the bear catch as much fish as possible.

# Task

Write a program that reads $N$ natural numbers and determines:

1. The maximum number of removals performed with the same two adjacent digits.
2. The largest natural number $X$ determined in such a way that the bear catches as much fish as possible.

# Input data

The input file `peste.in` contains:

- The first line contains the natural number $P$ which can be $1$ or $2$ and represents the task number.
- The second line contains a natural number $N$ as described in the text, and the following $N$ lines contain the $N$ numbers written on the paper given by the fox to the bear, one natural number per line of the file.

# Output data

The output file `peste.out` contains a single natural number determined according to the task requirements.

# Constraints and clarifications

* $1 \leq N \leq 100$, each of the $N$ numbers has at least $3$ and at most $18$ digits;
* Correct solving of task $1$ yields $40$ points, and correct solving of task $2$ yields $60$ points;
* For the case $P = 2$, there will be tests worth $25$ points where the $N$ natural numbers have values less than ${10}^9$ and other tests worth $10$ points where the $N$ numbers in the input file are less than ${10}^9$ and have the same number of digits.

# Example 1

`peste.in`
```
1
4
1791
802
777
77196
```

`peste.out`
```
2
```

## Explanation

We'll solve task $1$ and there are four numbers in the file which we proceed with as follows:

* From $1791$ we remove the digits $1$ and $7$ and the resulting number is $91$
* From $802$ we remove the digits $0$ and $2$ and the resulting number is $8$
* From $777$ we remove the digits $7$ and $7$ and the resulting number is $7$
* From $77196$ we remove $7$ and $1$ and the resulting number is $796$

There have been two removals with the same two adjacent digits: $1$ and $7$.

# Example 2

`peste.in`
```
2
4
1791
802
777
77196
```

`peste.out`
```
9187967
```

## Explanation

With the same four numbers from the previous example, we will solve task $2$.

After the removals, we obtain the numbers: $91, 8, 7, 796$. The largest possible number, obtained by concatenating these numbers, is $9187967$.