Cosmin was getting bored during the Romanian language and literature class when the teacher told the students that in the work "Povestea lui Harap-Alb" there is a mischievous character. At that moment, Cosmin remembered a tricky problem he didn't know how to solve. However, if you help him solve the problem, he will send you a mischievous elf by mail, who has a violin and a bow. Thus, Cosmin will understand how to solve the problem, and you will enjoy harmonious music.

# Task

Two numbers, $N$ and $X$, followed by an array $A$ of $N$ non-zero natural numbers, indexed from $1$ to $N$, are given. A new array $B$ will be constructed where each number $b_i$ ($1 \leq i \leq N$) takes the greatest value of the greatest common divisor that $a_i$ has with another number from the array $A$. Determine the number of subarrays in the array $B$ that have the bitwise OR sum greater than or equal to the number $X$.

A subarray from the array $B$ is a sequence of elements from different, consecutive positions.

The bitwise OR sum of a subarray $v_1, v_2, \dots, v_k$ is defined as $v_1 \vert v_2 \vert \dots \vert v_k$, where $\vert$ signifies the [bitwise OR operator](https://en.wikipedia.org/wiki/Bitwise_operation#OR).

# Input data

The first line will contain the natural numbers $N$ and $X$, and the second line will contain the $N$ natural numbers of the array $A$. The numbers on the same line are separated by a space.

# Output data

Print a single number representing the number of subarrays with the required property.

# Constraints and clarifications

* $2 \leq N \leq 1 \ 000 \ 000$;
* $1 \leq X \leq 1 \ 000 \ 000$;
* $1 \leq a_i \leq 1 \ 000 \ 000$.

|#|Score|Constraints|
|-|-|--------|
|1|22|$2 \leq N \leq 1 \ 000$|
|2|31|$2 \leq N \leq 100 \ 000$|
|3|47|No other additional constraints|

## Note
Due to the very large input data, the following instructions will be used at the beginning of the `main()` function in the C++ program:
```c++
ios_base::sync_with_stdio(false);
cin.tie(nullptr);
cout.tie(nullptr);
```

# Example

`stdin`
```
5 3
17 2 9 12 2
```

`stdout`
```
12
```

## Explanation

After each number $b_i$ ($1 \leq i \leq N$) takes the greatest value of the greatest common divisor that $a_i$ has with another number from the array $A$, the array $B$ has the values $1, 2, 3, 3, 2$. In this new array there are $12$ subarrays that have the bitwise OR sum greater than or equal to $3$.