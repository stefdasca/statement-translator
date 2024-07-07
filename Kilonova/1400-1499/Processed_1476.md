
I have a cable with $N$ LEDs (numbered from $1$ to $N$) placed equidistantly. Initially, some LEDs are on, and others are off.

The LEDs are interconnected so that touching any LED changes both its state and the state of its neighboring LEDs. Thus, if the LED $i$ ($2 \leq i \leq N-1$) is touched, the states of LEDs $i-1$, $i$, and $i+1$ change. If the LED $1$ is touched, the states of LEDs $1$ and $2$ change, and if the LED $N$ is touched, the states of LEDs $N-1$ and $N$ change.

I want to change the state of the LEDs so that they match a cable with $N$ LEDs that my friend Ionuț has (two cables match if, for any $i=1 \dots N$, the states of the LEDs at position $i$ are identical).

# Task

Knowing how Ionuț's cable looks like, help me determine the minimum number of touches on some LEDs so that my cable looks like Ionuț's cable.

# Input data

The input file `leduri.in` contains on the first line the natural number $N$. The second line contains $N$ binary digits separated by a space, representing the states of the LEDs on my cable. The digit at position $i$ is 0 if the LED $i$ is off, and 1 if the LED $i$ is on ($i=1 \dots N$). The third line contains $N$ binary digits separated by a space, representing the states of the LEDs on Ionuț's cable.

# Output data

The output file `leduri.out` will contain on the first line a single natural number representing the minimum number of touches on some LEDs so that my cable looks like Ionuț's cable.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* It is guaranteed that for all tests there is a solution.

# Example

`leduri.in`
```
4
1 0 1 0
0 1 1 1
```

`leduri.out`
```
2
```

## Explanation

A possible solution is:
1. Touch the second LED first: $1 0 1 0 \rightarrow 0 1 0 0$;
2. Touch the last LED: $0 1 0 0 \rightarrow 0 1 1 1$.
```
