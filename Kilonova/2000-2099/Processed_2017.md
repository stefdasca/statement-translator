> "Memories don't live like people do. They always 'member you"

Two arrays $A$ and $B$, both with $N$ elements, are given, along with the definition of the following function:
```cpp
long long f(int A[], int B[], int n){
    long long sum = 0;
    for(int i = 1; i \leq n; i++)
        for(int j = i+1; j \leq n; j++)
            if(B[i] == B[j]) sum += __gcd(A[i], A[j]);
    return sum;
}
```
Gya-chan, being very eager to open her gifts, wakes up in the middle of the night hoping to find them already under the tree. Great surprise when, on her way to the tree, she meets none other than the beloved Santa Claus. Upset that he was caught, he decides to give the girl a challenge.

# Task

Santa Claus asks the girl $Q$ questions of the form $(a, b)$, and the girl must say what the return value of the function $f$ would be if $B_a$ is replaced with $b$. Santa's updates are permanent, meaning that after each operation, the changes made to the array $B$ will persist.

# Input data

The first line contains two numbers, $N$, representing the number of elements in the two arrays, and $Q$, the number of questions. The next two lines each contain $N$ numbers, the first line containing the elements of array $A$, and the second the elements of array $B$. The last $Q$ lines contain the questions asked by Santa Claus.

# Output data

$Q + 1$ lines will be printed, the first designating the initial value of the function, and the next $Q$ lines containing the answers after each modification.

# Constraints and clarifications

* $1 \leq N, Q \leq 2 \cdot 10^5$
* $1 \leq A_i \leq 3 \cdot 10^5$, $1 \leq i \leq N$
* $1 \leq B_i \leq N$ after each operation
* Bahoi wants to mess up the problem, but it is completely forbidden!!! The number of distinct elements of array $B$ is $\leq BULAN$. ~~NO~~ You receive 5 points if you guess the value of $BULAN$  
| # | Points | Constraints | 
| - | ----- | ------------ |
| 1 | 13 | $1 \leq N \leq 10$ |
| 2 | 12 | $1 \leq A_i \leq 100$, $1 \leq i \leq N$|
| 3 | 19 | $1 \leq N \leq 1\ 000$ |
| 4 | 25 | $1 \leq N \leq 10^5$|
| 5 | 31 | No additional constraints |

# Example 1

`stdin`
```
3 2
2 3 2 
2 2 1 
3 2
2 1
```

`stdout`
```
1
4
2
```

## Explanation

Before the first modification, the return value of the function $f$ will be $\gcd(2,3) = 1$.
After the first modification, the return value will be $\gcd(2,2) + \gcd(2,3) + \gcd(2,3) = 2 + 1 + 1 = 4$.

# Example 2

`stdin`
```
10 4
1 10 9 2 3 10 9 9 1 8 
2 2 2 4 2 1 3 1 1 2 
5 4
4 1
6 3
8 3
```

`stdout`
```
16
11
14
11
19
