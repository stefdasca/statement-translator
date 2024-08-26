## Task

NOTICE: For this problem, the maximum score will be considered as $200$. 
`bool binary_search(int n, int p[], int target){`
$$\text{int left = 1, right = n; }$$
$$\text{while(left < right){ }$$
$$\text{int mid = (left + right) / 2; }$$
$$\text{if(p[mid] == target) return true; }$$
$$\text{else if(p[mid] < target) left = mid + 1; }$$
$$\text{else right = mid - 1; }$$
$$\text{ }}$$
$$\text{if(p[left] == target) return true; }$$
$$\text{ else return false; }$$
$$\text{}}$$
It is well known that if $p$ is sorted, then the code returns `true` if and only if `target` appears in $p$. On the other hand, this might not happen if $p$ is not sorted. You are given a natural number $n$ and a sequence $b$ $_1$ ,$\dots$, $b$ $_n$ ∈ { `true` , `false` } . It is guaranteed that there exists a natural number $k$ such that $n$ = $2^k$ − $1$ . You need to generate a permutation $p$ of the elements ${$1$, $\dots$, $n$}$ that meets certain conditions. Let $S(p)$ be the number of indices $i$ ∈ {$1$,$\dots$, $n$} for which `binary_search(n, p, $i$)` does not return $b$ $_i$ . You need to choose $p$ such that $S(p)$

is small (as detailed in the section "## Constraints and clarifications").

(Note: A permutation of the set ${$1$, $\dots$, $n$}$ is a sequence of $n$ natural numbers that contains each natural number from $1$ to $n$ exactly once.)

## Input data

The input file `binsearch.in` contains the first line which contains $T$ , the number of tests. The tests follow. The first line of a test contains the natural number $n$ . The second line contains a string of $n$ characters containing only '0' and '1' characters. These characters are not separated by spaces. If the $i$ -th character is '1' , then $b$ $_i$ = `true` , and if it is '0' , then $b$ $_i$ = `false` .

## Output data

The output file `binsearch.out` will contain for each test a line that contains a permutation $p$. 

## Constraints

Let $S$ be the sum of all values of $n$ in a single file.
1 $\leq N \leq 100000$  
1 $\leq T \leq 7000$  
There exists a natural number $k$ such that $n$ = $2^k$ − $1$  
If $S(p) \leq 1$ for all tests in a subtask, then $100$% of the points allocated to that subtask will be awarded.   
Otherwise, if $0 \leq S(p) \leq k$ (where $2^k = n - 1$) for all tests in a subtask, then $50$% of the points allocated to that subtask will be awarded.

Additionally:   
# Scoring

## Constraints and clarifications

1  
- $3 b_i$ = `true`  
2  
- $4 b_i$ = `false`  
3  
- $16$ $1 \leq n \leq 7$  
4  
- $25$ $1 \leq n \leq 15$  
5  
- $22$ $n$ = $2^{16} - 1$ and each $b_i$ is generated uniformly at random from the set { `true` , `false` }  
6  
- $30$ No additional constraints  

## Examples

`binsearch.in`  
```
4
3
111
7
1111111
3
000
7
0000000
3
010
7
0010110
```
`binsearch.out`  
```
1 2 3
1 2 3 4 5 6 7
3 2 1
7 3 1 5 2 4 6
```

## Explanations

Example 1.

In the first two tests, we have $S(p) = 0$. In the third test, we have $S(p) = 1$. This happens because `binary_search(n, p, 2)` returns `true` , even though $b$ $_2$ = `false` . In the fourth test, we have $S(p) = 1$. This happens because `binary_search(n, p, 4)` returns `true` , even though $b$ $_4$ = `false` . 

Example 2.

We have $S(p) = 0$ for both tests.