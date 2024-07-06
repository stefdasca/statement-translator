Lui Scortzy îi plac foarte mult bilele și puterile lui \(3\), astfel și-a organizat colecția de bile în cutii, după următoarea regulă: în prima cutie a pus o bilă, în a doua cutie \(3\) bile, în a treia cutie \(9\) bile, apoi \(27, 81, 243 \ldots\) și așa mai departe. Privind linia lungă de cutii Scortzy și-a pus întrebarea: *Ce număr de bile poate obține folosind bilele din cutii, fără a le scoate din cutie?*

Pentru a răspunde întrebării a început să formeze numerele: \(0\) (nici o cutie), \(1\) (cutia \(1\)), \(3\) (cutia \(2\)), \(4\) (cutiile \(1\) și \(2\)), \(9\) (cutia \(3\)) \ldots și așa mai departe, obținând șirul lui Scortzy, primii termeni ai acestui șir fiind: \(0, 1, 3, 4, 9, 10, 12, 13, 27, 28, 30, 31, 36, 37\).

Plăcându-i noul șir obținut Scortzy dorește să rezolve următoarele probleme:

# Task

1. Reading a natural number \(n\) determine how many boxes have fewer than \(n\) balls in them;
2. Reading a natural number \(n\) followed by \(n\) natural values \(x_1, x_2, \ldots, x_n\) determine how many balls are in each of the boxes used to obtain the \(x_i\)-th number in Scortzy's sequence.

# Input data

The first line of the `puteri3.in` file contains the natural numbers \(c\) and \(n\), separated by a space. If \(c=2\) then on the next \(n\) lines there will be \(n\) natural values \(x_1, x_2, \ldots, x_n\), one per line, representing the positions in Scortzy's sequence.

# Output data

If \(c=1\) then the `puteri3.out` file will contain a single number which represents the solution for task \(1\), and if \(c=2\) then the `puteri3.out` file will contain on each of its \(n\) lines one or more numbers. On the \(i\)-th line of the `puteri3.out` file there will be one or more numbers, separated by a space, in ascending order, representing the number of balls in each box used to obtain the number at position \(x_i\) in Scortzy's sequence.

# Constraints and clarifications
* \(C \in \{1, 2\}\);
* \(1 \leq x_1, x_2, \ldots, x_n \leq 10^{18}\);
* For \(c = 1, 1 \leq n \leq 10^{18}\);
* For \(c = 2, 1 \leq n \leq 1\ 000\), the number of balls in a box does not have more than \(80\) digits.

| # | Points | Constraints |
| - | - | ------------ |
| 1 | 20 | \( c = 1 \) |
| 2 | 30 | \( c = 2 \), \(1 \leq x_1, x_2, \ldots, x_n \leq 1\ 000\) |
| 3 | 35 | \( c = 2 \), the number of balls in a box is not greater than \(10^{18}\) |
| 4 | 15 | \( c = 2 \), no additional constraints |

# Example 1

`puteri3.in`
```
1 100
```

`puteri3.out`
```
5
```

## Explanation

The boxes with \(1\), \(3\), \(9\), \(27\) and \(81\) balls have fewer than \(100\) balls in them.

# Example 2

`puteri3.in`
```
2 3
4
14
9
```

`puteri3.out`
```
1 3
1 9 27
27
```

## Explanation

The first terms of Scortzy's sequence are: \(0, 1, 3, 4, 9, 10, 12, 13, 27, 28, 30, 31, 36, 37\).
The term at position \(4\) has the value \(4\) and is obtained from the sum \(1+3\).
The term at position \(14\) has the value \(37\) and is obtained from the sum \(1+9+27\).
The term at position \(9\) has the value \(27\) and is obtained using the box containing \(27\) balls.