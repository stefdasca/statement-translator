> Mini-Burac together with Elephant Marcici are causing havoc in the city...

# Task

You are given a word consisting of $N$ letters from the Latin alphabet and $Q$ intervals that represent subarrays of this word.  
The word is called **magic** only if every subarray among the $Q$ has all letters, which are **visible**, distinct.  
Initially, all letters are **visible**.  
However, at every moment of time $i$ ($1 \le i \le N$), the $P_i$-th letter is covered, and hence is no longer **visible**. It is guaranteed that $P$ is a permutation of the numbers from $1$ to $N$.  
Find out after which moment of time the word becomes **magic** (possibly $0$, meaning the string was magic before any letters started to be covered).

# Input data

The input file `magice.in` contains:
1. On the first line, a word of $N$ Latin letters.
2. On the second line, the number of intervals $Q$.
3. The next $Q$ lines contain pairs of the form $L_i \: R_i$ ($1 \le L \le R \le N$), representing the subarrays mentioned in the task.
4. On the last line, there are $N$ numbers representing the permutation $P$.

# Output data

The output file `magice.out` will contain a single number between $0$ and $N$, representing the moment of time when the given word becomes **magic**.

# Constraints and clarifications

* $N, Q \le 10^5$
* For 14 points, $N, Q \le 500$
* For another 21 points, $N, Q \le 3000$
* For another 14 points, the given word will consist only of the letter `a`

# Example 1

`magice.in`
```
aaaaa
2
1 2
4 5
2 4 1 5 3
```

`magice.out`
```
2
```

# Example 2

`magice.in`
```
abbabaab
3
1 3
4 7
3 5
6 3 5 1 4 2 7 8
```

`magice.out`
```
5
```

## Explanation

Evolution of the word (starting from time moment 0)
abbab#ab  
ab#ab#ab  
ab#a##ab  
#b#a##ab  
#b####ab  
######ab  
#######b  
########  

# Example 3

`magice.in`
```
abcd
1
1 4
1 2 3 4
```

`magice.out`
```
0
