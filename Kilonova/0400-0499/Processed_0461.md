Vlad wants to learn as much as possible about the modulo operation and its results. At the same time, he would like to compute some factorials. Because the value of the factorial of a number can be large, he wants to calculate the factorial of several numbers, modulo a certain value. Thus, he reads an integer $n$ from the keyboard and wants to determine the number $n!\\ \\%\\ MOD$, where $MOD = 10^9 + 7$. Help him correctly calculate this value!

# Task
Correct the program written by Vlad. It is available [here](modulo.cpp) or in the “Attachments� section on the side.

# Input data
$n$ — the number whose factorial modulo $MOD$ is desired to be calculated. This number is an integer in the range $[1, 100\\ 000]$.

# Output data
$val$ — the value $n!\\ \\%\\ MOD$.

# Example
`stdin`
```
5
```

`stdout`
```
120
```

## Explanation
$5! = 120$ and $120\\ \\% MOD\\ = 120$ since $120$ is a number smaller than $MOD$ ($10^9 + 7$).