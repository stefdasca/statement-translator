Zăhărel has a set of $N$ colored bulbs with $K$ colors (for convenience, we will consider the colors numbered from $1$ to $K$). Each bulb is special, in the sense that it has a switch that changes its current color $c$ as follows:

* if $c = K$, the color becomes $1$
* if $c < K$, the color becomes $c+1$

Zăhărel wishes to switch certain bulbs so that they all have the same color $C$. However, his task is not that simple, as he cannot switch the bulbs directly; instead, he must use a remote control with $M$ buttons. Pressing a button affects every bulb, more precisely, for each button $i$ there are $N$ values $A_{i,1} \ A_{i,2} \ \dots A_{i,N}$ with the meaning that bulb $j$ is switched $A_{i,j}$ times when button $i$ is pressed.

# Task

Write a program that determines in how many ways Zăhărel can use the $M$ buttons so that all the bulbs have the color $C$.

# Input data

The input file `color.in` contains on the first line the natural numbers $N \ M \ K \ C$ separated by spaces. The next line will contain $N$ natural numbers separated by spaces representing the initial colors of the bulbs, in order from $1$ to $N$. The next $M$ lines will contain $N$ natural numbers $A_{i,1} \ A_{i,2} \ \dots A_{i,N}$, separated by spaces, describing button $i$.

# Output data

In the output file `color.out` write on the first line the number of ways to use the remote control so that all the bulbs have the color $C$. The result will be displayed modulo $666 \ 013$.

# Constraints and clarifications

* During the correction $10$ tests will be used. They will have the following values for $N$, $M$ and $K$:

|Test|1|2|3|4|5|6|7|8|9|10|
|-|-|-|-|-|-|-|-|-|-|-|
|N|13|64|100|150|200|128|99|150|200|200|
|M|20|64|99|101|199|169|125|150|175|200|
|K|47|9973|30011|666019|15485863|9699690|602329|28447459|149662546|160213270|

* $1 \leq C \leq K$
* $0 \leq A_{i,j} \leq 10^9$
* A button on the remote control can be pressed a number of times less than $K$

# Example

`color.in`
```
4 6 2 1
1 2 1 2
1 0 1 0
0 1 0 1
1 0 0 0 
0 1 0 0 
0 0 1 0
0 0 0 1
```

`color.out`
```
4
```

## Explanation

The $4$ possibilities are:
1) button $2$
2) buttons $4, 6$
3) buttons $1, 2, 3, 5$
4) buttons $1, 3, 4, 5, 6$