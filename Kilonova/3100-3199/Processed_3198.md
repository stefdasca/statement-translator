
# Task

School starts on Monday, and you, like any diligent student, want to impress your classmates with the things you've learned during the holiday by being active on [RoAlgo](https://discord.gg/roalgo). You want to convince them to be active on the server as well. Today, after the round on Olympforces where you achieved a very good result, you want to show your classmates one of the problems that appeared there.

Thus, given a number $n$, the only thing you need to do is display the smallest number with $n$ digits that has the property that none of its prefixes is a divisor of the displayed number. The number itself is not considered a prefix.

For example, if $n = 3$ and $x = 321$, then the required property is not satisfied, because $3$ is a divisor of $321$. Also, $29$ is not a valid answer because it has $2$ digits, not $3$ as required by the problem.

An example of a valid number is $951$; $951$ is neither a multiple of $9$ nor $95$. However, it is not the smallest 3-digit number that satisfies this property.

Our hero solved the problem in 2 minutes; now it's your turn to show him that he's not the only one who can do this.

# Input data

The first line will contain $n$, the length of the required number.

# Output data

The first line will contain the required single integer, the result.

# Constraints and clarifications

* $2 \leq n \leq 100$;
* For test cases worth $30$ points, $n \leq 9$.
* For test cases worth another $20$ points, $n \leq 18$.

# Example

`stdin`
```
2
```

`stdout`
```
21
```
