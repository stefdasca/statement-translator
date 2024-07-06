```markdown
# Task

Andrei has an army of $x$ soldiers. It is known that this army will have to survive $n$ events.

An event can be of two types:

1) Andrei's army receives $k$ people. This event is coded with a non-negative number equal to $k$.
2) Andrei's army will battle against an army consisting of $k$ people. This event is coded with a negative number equal to $-k$. Andrei's army will only be able to defeat this enemy army if the number of soldiers in Andrei's army is **strictly** greater than $k$, thereby losing $k$ people. Otherwise, the army will disband.

Andrei now wants to know how many days his army can withstand.

If at any point the army no longer has people, the war will be considered lost.
(if the army was lost on day $i$, then the answer is $i-1$).

# Input data

The first line will contain two numbers $n$ and $x$.

The second line will contain $n$ numbers, representing the array $v$.

# Output data

The first line will contain a single integer, the sum of the two numbers.

# Constraints and clarifications

* $1 \leq n \leq 10^5$
* $1 \leq x \leq 10^4$
* $-10^4 \leq v_i \leq 10^4$

# Example 1

`stdin`
```
5 10
-2 -7 3 -4 1
```

`stdout`
```
3
```

## Explanation

For the first example, the army will be defeated after the fourth day, so it resisted for three days.

# Example 2

`stdin`
```
5 1
2 3 4 5 -6
```

`stdout`
```
5
```

## Explanation

For the second example, the army will be able to withstand the $n$ days.
```

