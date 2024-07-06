Gigel recently studied sequences with $n$ natural number elements. For such a sequence $S$, Gigel wants to find the answers to the following questions:

$a)$ What is the minimum number of strictly increasing subsequences in which $S$ can be partitioned?
$b)$ What is the number of subarrays, modulo $20\ 011$, with a sum of elements divisible by $k$ that can be obtained from $S$?

# Task

Given a sequence $S$ with $n$ natural number elements and a natural number $k$, the task is to answer the two above questions.

# Input data

The file `calcule.in` contains the natural values $n$ and $k$ separated by a space on the first line. The next line contains the $n$ elements of the sequence $S$, natural numbers separated by a space.

# Output data

The file `calcule.out` will contain two lines, with the first line containing a natural number representing the answer to question $a)$, and the second line containing a natural number representing the answer to question $b)$. **To receive partial scores, each line must contain a number!**

# Constraints and clarifications

* $1 < n < 100\ 000$
* $S$ has elements less than or equal to $20\ 000$.
* $k < 50\ 000$, $k < n$
* A **subsequence** of the sequence $S$ is obtained by selecting elements from $S$ **in the order** they are in $S$, but **not necessarily** from consecutive positions, whereas a **subarray** of the sequence $S$ is obtained by selecting elements in the order they are in $S$, but **necessarily** from consecutive positions. Sequences or subsequences with a single element are also allowed.
* For $50\%$ of the tests $k < 10\ 000$
* For a correct answer to a single task, $50\%$ of the score is given.
* Several subsequences of $S$ form a **partition** if the union of the elements of the subsequences can be rearranged to obtain exactly $S$.
* $x$ modulo $y$ represents the remainder of the division of $x$ by $y$.

# Example

`calcule.in`
```
10 3
5 3 8 6 9 6 2 7 9 6
```

`calcule.out`
```
4 
23
```

## Explanation

$a)$ A partition with the minimum number (4) of increasing subsequences is the following:

$5 \ 6 \ 7 \ 9$  
$3 \ 6 \ 9$  
$8$  
$2 \ 6$

$b)$ There are $23$ subarrays with a sum divisible by $3$. Here are two of them:

$3$  
$6 \ 2 \ 7$