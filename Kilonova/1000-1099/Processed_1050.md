```markdown
We define the strength of an element in an array as the value obtained by considering the number of digits it has in common with each of the other elements in the array and summing these values. For example, in the array ($12131, 1243, 15141$) the element $12131$ has a strength of $6$, because $12131$ has in common with $1243$ three digits ($1, 2$ and $3$), and with $15141$ it has in common three digits (the $3$ digits $1$).

Given an array with $n$ natural numbers, sort the elements of the array in ascending order of their strength, and those elements that have the same strength should appear in reverse order from how they initially appeared in the array.

# Input data

The input file `forta.in` contains on the first line $n$, the number of elements in the array, and on the second line $n$ natural numbers separated by a space, representing the elements of the array.

# Output data

The output file `forta.out` will contain on the first line, separated by a space, the elements of the array in the required order.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000$
* $\text{the elements of the array are natural numbers} \leq 10^{18})$
* For tests worth $30$ points, the elements of the array will have distinct strengths

# Example

`forta.in`
```
4
123 121 12314 1234
```

`forta.out`
```
121 123 1234 12314
```
```