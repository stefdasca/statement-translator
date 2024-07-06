Iliuță and Pandele learned arithmetic operations with natural numbers at school. Thus, the two brothers practice these operations using a board. Iliuță says a natural number $X$, and Pandele writes the result of multiplying all natural numbers from $1$ to $X$ on the board. Just for fun, Iliuță erases the digits that are equal to $0$ from the end of the number written by Pandele.

To forgive him, Pandele says a natural number $Y$ and asks Iliuță to determine a natural number $Z$ which is the largest divisor of $Y$ having an odd number of divisors.

# Task

Given the numbers mentioned by the children, write a program that solves the following tasks:
1. Display the last $K$ digits of the product calculated by Pandele, after erasing the digits equal to $0$ from the end of the product;
2. Display the natural number $Z$ with the aforementioned significance and the number of its divisors.

# Input data

The file `copii.in` contains on the first line the number $C$, which represents the task number and can only have the values $1$ or $2$. For the first task, the file contains on the second line the number $X$, and on the third line the number $K$. For the second task, the file contains on the second line the number $Y$.

# Output data

For task $1$, the first line of the file `copii.out` will contain the $K$ requested digits, without spaces, in order from left to right.
For task $2$, the first line will contain, in this order, the number $Z$ determined and the number of its divisors. The numbers will be separated by a space.

# Constraints and clarifications

* $1 \leq X \leq 10^6$;
* $1 \leq Y \leq 10^{12}$;
* $1 \leq K \leq 9$;
* The remaining number after erasing the zeros from the end of the product has at least $K$ digits;
* Solving the first task yields $40$ points;
* Solving the second task yields $60$ points.

# Example 1

`copii.in`
```
1
12
3
```

`copii.out`
```
016
```

## Explanation

The product $1 \cdot 2 \cdot 3  \cdot 4  \cdot 5 \cdot 6 \cdot 7 \cdot 8 \cdot 9 \cdot 10 \cdot 11 \cdot 12 = 4790\underline{016}00$.
After erasing the zeros from the end of the product, the last $3$ digits are $016$.


# Example 2

`copii.in`
```
2
14641
```

`copii.out`
```
14641 5
```

## Explanation

The largest divisor of $14641$ that has an odd number of divisors is $14641$ itself.

# Example 3

`copii.in`
```
1
723432
9
```

`copii.out`
```
813433856
```

## Explanation

After erasing the zeros from the end of the product, the last $9$ digits are $813433856$.

# Example 4

`copii.in`
```
2
573194962208
```

`copii.out`
```
286597481104 105
```

## Explanation

The largest divisor with an odd number of divisors is $286597481104$ which has $105$ divisors.