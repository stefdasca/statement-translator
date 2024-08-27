## Task

You are at home (either it's too hot or too cold outside) and you are reading the problem Sievelet. You wonder: in how many ways can Eratosthenes' Algorithm be wrong such that its behavior is semi-interesting? The answer seems to be "sufficient". In this problem, you will analyze how Sieve of Eratosthenes' behavior changes if instead of processing the numbers in the order ${2, 3, 4, \dots N}$, you process them in the order given by a random permutation of these numbers. Specifically, given this pseudocode:

```cpp
int countSteps(int n, vector<int> p) { 
    vector<bool> Composite(n + 1, false); 
    int steps = 0;  
    // p is a permutation of the set {2, 3, ..., n}  
    for(int index = 0; index < n - 1; ++index) { 
        if(not Composite[p[index]]) { 
            for(int multiple = 2 * p[index]; multiple <= n; multiple += p[index]) { 
                Composite[multiple] = true; 
                steps += 1; 
            } 
        } 
    }  
    return steps; 
}

int identity = countSteps(8, {2, 3, 4, 5, 6, 7, 8}); 
int misplaced_four = countSteps(8, {4, 2, 3, 5, 6, 7, 8}); 
```

identity has the value $4$, and misplaced_four has the value $5$. Given a number $N$, you wonder what is the expected average value returned by the function $countSteps(N, p)$ if the permutation $p$ is randomly and uniformly generated. If you don't know what the average value means (which would be strange since you asked the question yourself), know that it is the number obtained by calculating the arithmetic mean of all function results when you run it on all possible permutations.

## Input data

The input file `sieve.in` will contain on its first line the number $T$ representing the number of tests. The following $T$ tests contain one value $N$ each. 

## Output data

The output file `sieve.out` will contain $T$ lines, each containing a real number, representing the answer for the corresponding test. 

## Constraints and clarifications

$1 \leq T \leq 100\ 000$  
$2 \leq N \leq 100\ 000$  
An answer is considered correct if the absolute difference between it and the correct answer is less than or equal to $10^{-4}$.  

## Example

`sieve.in`
```
2
9
250
```

`sieve.out`
```
5.5
577.8554834
```