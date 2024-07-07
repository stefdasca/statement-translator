
The SG1 team's mission consists of activating an extraterrestrial device operated with the help of a strange keyboard made up of $n$ switches, all initially in the same position (let's denote this position as $0$). It is known that exactly $k$ switches need to be set (switched to position $1$) and that the order in which the switches are activated does not matter. Additionally, with the help of some ancient documents, they found out that between any two successive set switches there must be at least $d1$ and at most $d2$ unset switches. For example, for $n=7$, $k=3$, $d1=1$, and $d2=2$, a configuration that meets the requirements is: $0100101$, while configurations $1010001$, $1100100$, $1010101$ do not meet the problem's criteria. If a combination of set switches does not activate the device, nothing special happens (such a boring episode!), and the switches automatically reset, allowing another combination attempt. It is required to determine the maximum number of distinct configurations of set switches that the SG1 team must try to activate the device.

# Task

Write a program that, for given values $n$, $k$, $d1$, and $d2$, determines the total number of possible switch configurations that meet the conditions in the description.

# Input data

In the text file `sg1.in`, on the same line, separated by spaces, the values $n$, $k$, $d1$, and $d2$ are given.

# Output data

The file `sg1.out` contains the number of configurations that meet the task requirements.

# Constraints and clarifications

* $1 \leq n \leq 100$;
* $1 \leq k \leq n$;
* $0 \leq d1 \leq d2 < n$. 

# Example 1

`sg1.in`
```
7 3 1 2
```

`sg1.out`
```
8
```

## Explanation

The $8$ configurations are:
$1010100$, $1010010$, $1001010$, $1001001$, $0101010$, $0101001$, $0100101$, $0010101$. 

# Example 2

`sg1.in`
```
5 2 0 0
```

`sg1.out`
```
4
```

## Explanation

$11000$, $01100$, $00110$, $00011$. 

# Example 3

`sg1.in`
```
14 8 1 5
```

`sg1.out`
```
0
```
