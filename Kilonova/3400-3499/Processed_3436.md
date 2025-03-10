# Task

Before leaving for your vacation, you wrote down on a piece of paper a sequence of $N$ **positive natural** numbers: $a_1, a_2, \\dots, a_N$. These represent the password for your ***BITCOIN*** wallet, which is valued at approximately $10^9$ **USD**.

When you returned, you realized that you couldn't find the paper anymore. However, not all hope is lost, because you remember the number $N$ and you can still find the numbers $X$ and $Y$, which you are sure belong to the password. You've decided to write down all the properties of the password that you are certain about on your notebook:
1. The sequence contains exactly $N$ numbers;
2. The numbers $X$ and $Y$ are part of the password, and $X \\lt Y$;
3. The numbers in the password are positive natural numbers less than or equal to $10^9 \\ (1 \\leq a_i \\leq 10^9)$;
4. The elements of the sequence are in **strictly increasing order**, and the difference between two numbers at consecutive positions is **constant** $(a_2-a_1=a_3-a_2=...=a_{N}-a_{N-1})$;
5. The maximum element of the password (the last element) must be **minimal**.

Your goal is to find the lost password and recover your **money**!

# Input data

The first line contains the number $T$ (the ordinal number of the test group to which the test belongs).
The following line contains three natural numbers: $N, X, Y$, with the significance explained in the statement.

# Output data

The first line will contain $N$ natural numbers, the **found password**. (the numbers must be displayed **in the order they appear in the password**).

# Constraints and clarifications

* $0 \\leq T \\leq 6$;
* $2 \\leq N \\leq 100 \\ 000$;
* $1 \\leq X \\lt Y \\leq 10^9$;
* $1 \\leq a_i \\leq 10^9$;
* In case there are multiple solutions that fulfill all the conditions in the problem statement, **any** can be displayed;
* It is guaranteed that there exists at least one sequence that fulfills all the conditions;
* If the displayed sequence fulfills all the conditions, you will receive 100% of the test score, but if it only fulfills the first 4 conditions, the score percentage will be calculated according to the formula: $\\frac {0.75}{1 + \\frac{SC - SO}{D}}$ ($SC = $ last contestant’s element, $SO = $ last optimal element, $D = $ difference between 2 consecutive elements in the contestant's sequence), otherwise, you will receive 0 points on that test;
* For fast input and output, it is recommended to use these lines of code at the start of your `main` function:
```cpp
ios::sync_with_stdio(false);  
cin.tie(NULL);  
cout.tie(NULL);  
```

| # | Score | Constraints |
| - |:-----:|:-----------:|
| 0 | 0     |    Examples  |
| 1 | 10    |    $a_1 = X$, $a_N = Y$ and $N = Y-X+1$ |
| 2 | 10    |    $a_1 = X$ and $a_N = Y$   |
| 3 | 20    |    $X = 1$  |
| 4 | 20    |    $Y-X = $ prime number |
| 5 | 20    |    $1 \\leq X \\lt Y \\leq 10^6$  |
| 6 | 20    |    No additional constraints |

# Example

`stdin`
```
0
4 10 20
```

`stdout`
```
5 10 15 20
```

## Explanation

The first line contains the number $T = 0$, because this is an example.
The possible sequences that satisfy the first 4 conditions are:
* $10, 20, 30, 40;$
* $5, 10, 15, 20;$
* $10, 15, 20, 25;$

Among them, the one with the smallest last element is the second sequence. Thus, the password is the sequence $5, 10, 15, 20$.