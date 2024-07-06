Vară, căldură mare. Gigel se joacă în curte udând florile. După ce a terminat, mama lui îi dă o sarcină mai grea. Gigel trebuie să umple un butoi cu apă de rezervă în caz de secetă. Dar nu oricum! El are la dispoziție un șir de găleți de diferite capacități și trebuie să le folosească doar pe acestea pentru umplerea completă a butoiului. O operație constă în umplerea completă a unei găleți de la sursa de apă și golirea ei în butoi. Desigur, o găleată se poate folosi de mai multe ori. Butoiul are capacitate de $V$ litri, Gigel are $N$ găleți de capacități $c_1, c_2, \dots, c_N$ litri, numere întregi și distincte și poate folosi o găleată de cel mult $K$ ori. Ajutați-l pe Gigel să umple butoiul.

# Task

Write a program that solves the following requirements:

1. Determine how many ways to fill the barrel exist;
2. Determine a way to fill the barrel with the minimum number of operations;
3. A subarray of exactly $P$ adjacent buckets is called lucky if by performing the operation the same number of times for each of them, we can completely fill the barrel. Determine the lucky subarray that allows using the $P$ buckets a minimum number of times for completely filling the barrel. The lucky subarray will be identified by the position of the first bucket used. If there are multiple solutions, the one with the smallest position will be displayed. The buckets in the lucky subarray can be used as many times as needed.

# Input data

The input file `butoi.in` contains: the first line contains a natural number $C$ which can have the values $1, 2$ or $3$ and represents the number of the requirement. The second line contains four natural values $V \ N \ K \ P$, separated by a space, representing in order the capacity of the barrel, the number of buckets, the maximum number of operations that can be performed with a bucket, in the case of requirements $1$ and $2$, and the last number represents the length of the lucky subarray sought in requirement $3$. The third line contains $N$ distinct natural values $c_1, c_2, \dots, c_N$, separated by a space, representing in order the capacities of the $N$ buckets in the array.

# Output data

The output file `butoi.out` will contain: for requirement $1$, the first line will contain an integer representing the number of ways to fill the barrel. For requirement $2$ the first line will contain $N$ natural values separated by a space, representing the number of uses of each bucket, and for requirement $3$ the first line will contain a natural number representing the position in the array of the first bucket in the determined lucky subarray.

# Constraints and clarifications

* $5 \leq V \leq 360\ 000$;
* For requirements $1$ and $2$ the constraints are: $1 \leq N \leq 9$; $1 \leq c_i \leq 8\ 000$; and $1 \leq K \leq 5$;
* For requirement $3$ the constraints are: $3 \leq N \leq 100\ 000$; $1 \leq c_i \leq 200\ 000$; $3 \leq P \leq 10\ 000$; and $P \leq N$
* For requirement $3$ the capacities $c_1, c_2, \dots, c_N$ of the buckets do not necessarily have to be distinct.
* For the correct resolution of the first requirement, you get $30$ points, for the correct resolution of the second requirement you get $40$ points, and for the correct resolution of the third requirement you get $30$ points.

# Example 1

`butoi.in`
```
1
90 7 1 2
30 56 70 34 60 15 5
```

`butoi.out`
```
3
```

## Explanation

The requirement is $1$. There are $3$ ways to fill the barrel using each bucket at most once, because $K = 1$. These are $30 + 60$, $56 + 34$ and $70 + 15 + 5$.

# Example 2

`butoi.in`
```
1
2020 6 5 3
17 42 200 101 51 171
```

`butoi.out`
```
19
```

## Explanation

The requirement is $1$. There are $19$ ways to fill the barrel.

# Example 3

`butoi.in`
```
2
2020 6 5 3
17 42 200 101 51 171
```

`butoi.out`
```
0 0 5 3 4 3
```

## Explanation

The requirement is $2$. The minimum number of operations is $15$. The buckets were used as follows: $0 \cdot 17 + 0 \cdot 42 + 5 \cdot 200 + 3 \cdot 101 + 4 \cdot 51 + 3 \cdot 171 = 0 + 0 + 1000 + 303 + 204 + 513 = 2020$.

# Example 4

`butoi.in`
```
3
120 7 1 3
90 12 20 8 41 80 11
```

`butoi.out`
```
2
```

## Explanation

The requirement is $3$. The lucky subarray of length $3$ determined starts at position $2$. By using each bucket in the subarray $3$ times, the barrel is filled.