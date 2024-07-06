`Ionuț tocmai a împlinit 14 ani și a primit cadou de ziua lui un set de $N$ bile de biliard numerotate de la $1$ la $N$ și un aparat de fotografiat. Bilele sunt așezate într-o ordine oarecare.

Fiind pasionat de matematică, el își imaginează un joc alcătuit din $K$ pași. El vrea ca, la finalul jocului, bilele să fie așezate într-o anumită ordine cerută de fratele său, conform regulilor jocului:
* La primul pas, Ionuț așază bilele de biliard pe masă într-o ordine oarecare și fotografiază așezarea acestora. El va avea nevoie de fotografia făcută pe toată durata jocului.
* Apoi, parcurge cei $K - 1$ pași rămași. La fiecare pas, toate bilele sunt repoziționate. Astfel, pentru a determina ce bilă trebuie pusă pe o anumită poziție $i$, cu $1 \le i \le N$, Ionuț caută în fotografie ce bilă se afla pe poziția $i$, la începutul jocului. Fie $Q$ numărul de pe acea bilă. Ionuț va pune acum pe poziția $i$ bila ce, la pasul anterior, se afla pe poziția $Q$.

# Task

Ionuț își propune să afle care sunt **toate modalitățile** posibile de așezare inițială a bilelor astfel încât, în urma parcurgerii pașilor jocului, bilele să fie așezate în ordinea dorită de fratele său. 

# Input data

The first line of the input file `bile14.in` will contain two natural numbers in this order:
* $N$ - the number of balls Ionuț has;
* $K$ - the number of steps the game will have. 

The second line of the file will contain $N$ natural numbers separated by a space, representing the order of the balls as requested by Ionuț’s brother.

# Output data

The output file `bile14.out` will contain multiple sequences, each on a separate line, displayed in lexicographical order.
Each sequence will be composed of $N$ natural numbers separated by a space.
Each of these sequences represents a possible initial arrangement of the balls which, after the steps of the game, will lead to the order desired by Ionuț’s brother.

# Constraints and clarifications

* $N \le 9$
* $2 \le K \le 10^{9}$
* There will always be at least one way to arrange the balls that will lead to the desired order.
* 10 points are offered initially.

| # | Points |      Constraints      |
|:-:|:-------:|:--------------------:|
| 1 |    20   |   $2 \le K \le 20$   |
| 2 |    70   | Without additional constraints |

# Example

`bile14.in`
```
5 3
1 2 3 5 4
```

`bile14.out`
```
1 2 3 5 4
2 3 1 5 4
3 1 2 5 4 
```

## Explanation

The three sequences obtained represent all possible ways to initially arrange the balls so that after the game, they reach the sequence given by Ionuț’s brother.

For the first two solutions from the example above, the game unfolds as follows:

~[bile14.png|align=left|width=60%]

It can be observed that for the two explained solutions, the sequence determined by the ball numbers was displayed on the line called *Initial arrangement (After Step 1)* and the initial sequence found in the input file was reached on the last line.