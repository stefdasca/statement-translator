I'm here to help translate the provided competitive programming problem statement from Romanian to English while maintaining the specified formatting and structure.

---

I was mocked twice...

After many days of trying and convincing, Maria finally agreed to play with Buzdi. Being quite smart, they managed to invent a new game called `restriction`. Buzdi brought an array $A$ of $N$ integers, and Maria brought an array $B$ of $N$ natural numbers. After that, they defined the `restriction` operation on a number $A_i \\ (1 \\leq i \\leq N)$ as follows:
1) Decompose $A_i$ into prime factors. Let this be $f_1^{e_1} \\cdot f_2^{e_2} \\cdot ... \\cdot f_K^{e_K}$.
2) Each exponent changes its value if its current value is greater than $B_i$. Formally, $e_j = \\min(e_j, B_i)$ for each $1 \\leq j \\leq K$.

For example, if $A_i = 360 = 2^3 \\cdot 3^2 \\cdot 5^1$ and $B_i = 1$, then, after applying the `restriction` operation, $A_i = 30 = 2^1 \\cdot 3^1 \\cdot 5^1$. 
Similarly, if $A_i = -360 = -2^3 \\cdot 3^2 \\cdot 5^1$ and $B_i = 1$, then, after applying the `restriction` operation, $A_i = -30 = -2^1 \\cdot 3^1 \\cdot 5^1$.
By convention, after applying the `restriction` operation to the numbers $1$, $-1$, or $0$, they do not change their value.

# Task
1) Buzdi challenges Maria to solve the following task: What is the maximum value in the array $A$ before and after applying the `restriction` operation to all numbers in the array $A$?
2) Maria challenges Buzdi to solve the following task: What is the minimum number of numbers to which we need to apply the `restriction` operation so that the sum of any subarray in the newly obtained array $A$ is less than or equal to $S$?

They both need to solve the task given by the other to not be mocked for their problem-solving abilities. Your goal is to solve them to help both of them.

# Input data

The first line contains a natural number $G$, representing the test group to which the test belongs. The next line contains two natural numbers, $C$ and $N$, where $C$ represents the task that needs to be solved. The next line contains $N$ integers, separated by space, representing the numbers of array $A$. The next line contains $N$ natural numbers, separated by space, representing the numbers of array $B$. If $C = 2$, then the next line contains the integer $S$.

# Output data

If $C = 1$, then on the first line, there will be two integers, separated by a space, representing the solution to task $1$. If $C = 2$, then on the first line, there will be an integer, representing the solution to task $2$.

# Constraints and clarifications

* **Attention! This problem had some incorrect tests during the official contest. The sum of the scores of the incorrect tests was redistributed equally over all other tests, and the leaderboard was recalculated. Fortunately, it was not affected. These tests were later modified so that correct solutions would earn the appropriate score. We apologize!**
* $1 \\leq N \\leq 2 \\cdot 10^5$.
* $-10^6 \\leq A_i \\leq 10^6$, for each $1 \\leq i \\leq N$.
* $0 \\leq B_i \\leq 20$, for each $1 \\leq i \\leq N$.
* $-10^{18} \\leq S \\leq 10^{18}$.
* A subarray of an array $A$ represents a succession of numbers on consecutive positions in the array $A$.
* It is guaranteed that for $C = 2$, there exists a solution.
- For fast input and output, it is recommended to use these lines of code at the beginning of the `main` function:  
```cpp
ios::sync_with_stdio(false);  
cin.tie(NULL);  
cout.tie(NULL);  
```  
* The test groups are as follows:
| G | Points | Constraints |
| ---- | ---- | ---- |
| 0 | 0 | Examples |
| 1 | 8 | $C = 1$ and $A_i$ is a prime number for each $1 \\leq i \\leq N$ |
| 2 | 30 | $C = 1$ and $1 \\leq N \\leq 2\,000$ |
| 3 | 10 | $C = 1$ |
| 4 | 3 | $C = 2$ and $B_i = 20$ for each $1 \\leq i \\leq N$ |
| 5 | 22 | $C = 2$ and $1 \\leq N \\leq 2\,000$ |
| 6 | 27 | $C = 2$ |

# Example 1

`stdin`
```
0
1
6
12 8 36 100 -1 60
1 1 2 1 0 1
```

`stdout`
```
100 36
```

## Explanation

Let $R$ be the array obtained after applying the `restriction` operation to all the numbers in the array $A$. Then, $R$ = $[6, 2, 36, 10, -1, 30]$.
We observe that the maximum value in the array $A$ is $100$, and the maximum value in the array $R$ is $36$.

# Example 2

`stdin`
```
0
2
6
12 8 36 100 -1000 60
1 1 2 1 0 1
60
```

`stdout`
```
2
```

## Explanation

It is sufficient to apply the `restriction` operation to the numbers $8$ and $100$. Thus, it can be demonstrated that the sum of any subarray in the newly obtained array is less than or equal to $60$.

---