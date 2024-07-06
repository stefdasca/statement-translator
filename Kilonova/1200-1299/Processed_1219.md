Here is the translated problem statement. I have ensured that the formatting, mathematical values, and custom image syntax are preserved as requested.

---

A sequence of $n$ elements, natural numbers, is given. The sequence of numbers is traversed from left to right and divided into groups of one, two, or more neighboring elements that are in ascending order, so that in a group, each element positioned to the left of another neighboring element is less than or equal to it, while the first element that is not in the group (the one "after" the group) is strictly less than the last from the previous group (exception: if the n numbers are in ascending order, there is only one group). Thus, for example, the sequence consisting of the elements: $2$, $3$, $6$, $0$, $3$, $1$ is divided into three groups: the first contains the elements with values $2$, $3$, $6$, the second $0$, $3$, and the third is formed from a single element having the value $1$.

For each group, the sum of the elements from the respective group is calculated, and with these sums, a new sequence $y$ is formed. The number of elements in the sequence $y$ will be equal to the number of formed groups. For each element in the sequence $y \ i$, the control digit is determined. The control digit for a given value is calculated as follows: the sum of the digits is determined, then the sum of the digits of the obtained number, and so on, until a single digit is obtained (for example, for the number $9 \ 997$, the sum of the digits is first calculated $9+9+9+7=34$, then we continue with the number $34$ and obtain the control digit $7$, that is $3+4$). Thus, a new sequence $z$ is obtained with the control digits for the elements in the sequence $y$.

# Task

Determine the largest natural number that can be formed with all the digits that are not found in the sequence $z$, each such digit being able to appear in the new number only once. If all the digits are found in the sequence $z$, the required number will be $-1$.

# Input data

The first line of the input file `numar.in` will contain the value $n$, representing the number of elements in the initial sequence. The second line will contain the elements of the initial sequence, separated two by two by a space.

# Output data

The first line of the output file `numar.out` will contain the required number.

# Constraints and clarifications

* $1 \leq n \leq 50$;
* The numbers in the initial sequence are natural, less than or equal to $30 \ 000$.

# Example 1

`numar.in`
```
11
6 8 9 11 2 3 1 0 6 9 3
```

`numar.out`
```
98420
```

## Explanation

$y=(34,5,1,15,3)$; $z=(7,5,1,6,3)$;

$nr=98420$, because the digits $9$, $8$, $4$, $2$, $0$ are not found in the sequence $z$