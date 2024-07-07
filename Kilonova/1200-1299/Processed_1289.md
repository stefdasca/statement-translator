
The central market square of Bacau city is circular in shape. All around the market, $n$ lanterns are mounted, numbered from $0$ to $n - 1$. Each lantern can have two states: on or off. At night, all lanterns are turned on simultaneously. Tourist Vasile T. Popescu starts walking around the market, starting from lantern $0$ to lantern $1$, then from $1$ to $2$, $\dots$, from $n - 2$ to $n - 1$, from $n - 1$ to $0$, etc., and whenever he passes by a lantern, he performs exactly one of the following operations:

- if the previous lantern ($i - 1$ if $i > 0$ or $n - 1$ if $i = 0$) is on, then he toggles the state of the current lantern (if it was on, he turns it off; if it was off, he turns it on);
- if the previous lantern is off, then the state of the current lantern remains unchanged.

# Task

Determine the minimum number of operations the tourist must perform until all the lanterns are turned on again.

# Input data

The input file `felinare.in` contains the first line with the natural number $n$, representing the number of lanterns.

# Output data

The output file `felinare.out` will contain a single line which will have a single natural number representing the minimum number of operations that need to be executed so that all lanterns are turned on again.

# Constraints and clarifications

* $2 \leq n \leq 5\ 000$
* $n$ is of the form $2 ^ k$ or $2 ^ k + 1$
* the tourist switches off at least one lantern

# Example

`felinare.in`
```
3
```

`felinare.out`
```
7
```

## Explanation

$111$ initially all lanterns are on  
$011$ after the first operation, lantern $0$ is off because lantern $2$ is on  
$011$ after the second operation, lantern $1$ remains on because lantern $0$ is off  
$010$ after the third operation, lantern $2$ is off because lantern $1$ is on  
$010$ after the fourth operation, lantern $0$ remains off because lantern $2$ is off  
$010$ after the fifth operation, lantern $1$ remains on because lantern $0$ is off  
$011$ after the sixth operation, lantern $2$ is on because lantern $1$ is on  
$111$ after the seventh operation, lantern $0$ is on because lantern $2$ is on
```

The translation has been carefully checked for possible grammar and syntax errors and corrected as necessary.
