b'Se consideră un tablou bidimensional de dimensiuni date $m$ (numărul de linii) și $n$ (numărul de coloane), ale cărei elemente sunt cifre ale sistemului de numerație zecimal. Cu elementele unei linii se construiește un număr scris în cea mai mică bază posibilă, utilizând toate cifrele de pe linia respectivă, luate de la stânga la dreapta. Se spune că acest număr se atașează liniei respective. După această regulă se atașează numere fiecărei linii, numere care se transformă apoi în baza $10$. Se identifică cel mai mare număr scris în baza $10$ dintre numerele atașate fiecărei linii și linia pe care se află; dacă sunt mai multe linii pe care se află cel mai mare număr, se alege cea cu indicele cel mai mic (cea mai de sus). Să notăm indicele acestei linii cu $p$. De pe linia $p$ se identifică, dacă există, coloana cu indicele cel mai mic (cea mai din stânga) pe care se află o cifră pară. Să notăm indicele acestei coloane cu $q$. Dacă există o astfel de coloană, atunci se elimină din tablou linia $p$ și coloana $q$. Prin eliminare, numărul de linii și numărul de coloane ale tabloului scad cu $1$, astfel, dacă, de exemplu, s-ar elimina linia $3$, atunci linia $4$ va deveni linia $3$, linia $5$ va deveni linia $4$, $\\dots$, linia $m$ va deveni linia $m - 1$, iar dacă, de exemplu, s-ar elimina coloana $4$, atunci coloana $5$ va deveni coloana $4$, coloana $6$ va deveni coloana $5$, $\\dots$, coloana $n$ va deveni coloana $n - 1$. S-a obținut astfel un nou tablou bidimensional, în care liniile se consideră având indicii $1, 2, \\dots$, ș.a.m.d., iar coloanele indicii $1$, $2$, $\\dots$, ș.a.m.d. Dacă pe linia $p$ nu se poate găsi o cifră pară, tabloul nu se modifică.
Se reia procedeul de mai sus pentru noul tablou, începând cu atașarea numerelor pentru noile linii, identificarea celui mai mare număr în baza $10$, identificarea liniei $p$ și coloanei $q$ (dacă există) și apoi eliminarea liniei $p$ și coloanei $q$, dacă este cazul. Procedeul se oprește fie când nu se mai identifică pe linia $p$ o cifră pară, fie când cel puțin una dintre dimensiunile tabloului (numărul de linii sau numărul de coloane) a ajuns la valoarea $1$.

# Task

Given the bidimensional table with $m$ rows and $n$ columns, determine:
1. Display the minimum bases that were chosen for each number attached to each row of the initial table.
2. Display the largest number written in base $10$ among the numbers attached to the initial table.
3. Display the number of rows and the number of columns for the final table, as well as the final table.

# Input data

The input file `tablou.in` will contain:
* The first line of the file contains the natural number $m$ which represents the number of rows and the natural number $n$ which represents the number of columns of the initial table, numbers separated by a space.
* On the following $m$ lines there are $n$ numbers, each separated two by two by a space.

# Output data

The output file `tablou.out` will contain:
* On the first line, $m$ numbers will be displayed, each separated two by two by a space, representing the bases according to task $a)$.
* On the second line, the number required according to task $b)$ will be printed.
* On the third line, the number of rows and the number of columns for the final table, numbers separated by a space (let these be $x$ and $y$).
* On the following $x$ lines, there will be $y$ numbers each separated two by two by a space.

# Constraints and clarifications

* $2 \leq m, n \leq 10$.
* The largest number attached to a row, written in base $10$ is $2 \\ 000 \\ 000 \\ 000$. The smallest base in which a number attached to a row can be written is base $2$ and the largest is $10$.
* Partial scores are awarded: task $1$, $20\%$ of the score, task $2$, $20\%, of the score, task $3$, $60\%$ of the score.

# Example

`tablou.in`
```
4 4
1 0 1 1
2 0 1 2
1 3 1 3
3 0 0 0
```

`tablou.out`
```
2 3 4 4
192
2 2
1 1
1 3
```

## Explanation

The numbers attached to the rows are: $1011$ in base $2$, $2012$ in base $3$, $1313$ in base $4$, $3000$ in base $4$. Their values in base $10$ are: $11, 59, 119, 192$. The largest is $192$ and is on row $4$. The first even element on row $4$ is in the second column. Therefore, row $4$ and column $2$ will be eliminated. The remaining table has $3$ rows and $3$ columns and its values are:

$$
\begin{array} {|r|r|r|r|}
\hline
1 & 1 & 1 \\
\hline
2 & 1 & 2 \\
\hline
1 & 1 & 3 \\
\hline
\end{array}
$$

The process is then repeated.
The numbers attached to the rows of the new table are: $111$ in base $2$, $212$ in base $3$, $113$ in base $4$. Their values in base $10$ are: $7$, $23$, $23$. The largest is $23$, and the first equal to $23$ is on row $2$. The first even element on row $2$ is in the first column. Therefore, row $2$ and column $1$ will be eliminated. The remaining table has $2$ rows and $2$ columns and its values are:

$$
\begin{array} {|r|r|r|r|}
\hline
1 & 1 \\
\hline
1 & 3 \\
\hline
\end{array}
$$

The process is then repeated.
The numbers attached to the rows are: $11$ in base $2$, $13$ in base $4$. Their values in base $10$ are: $3$, $7$. The largest is $7$ and is on row $2$. On this row, there is no even element, so the process ends.
'