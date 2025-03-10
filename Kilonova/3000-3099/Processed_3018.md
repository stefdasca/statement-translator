Este anul 2019, dar Zmeul-Cel-Rău și Făt-Frumos continuă să lupte. Zmeul l-a capturat pe Făt-Frumos și l-a închis într-una dintre camerele bârlogului său. Un bârlog de zmeu are forma unei matrice bidimensionale, cu camere aranjate în $n$ linii și $m$ coloane. Vom numerota liniile de la $1$ la $n$ și coloanele de la $1$ la $m$, astfel încât fiecare cameră poate fi identificată prin numărul liniei și al coloanei pe care se află.

Orice cameră are patru pereți și câte o ușă pe fiecare perete, prin care poate comunica cu camerele vecine. Mai exact, camera de pe linia $i$ și coloana $j$ poate comunica cu camerele $(i-1,j)$, $(i,j+1)$, $(i+1,j)$, $(i,j-1)$ (desigur, dacă acestea există). Fiecare cameră are asociat un cod. Ușile din orice cameră se pot deschide cu o cartelă magnetică. Dacă codul camerei este o subsecvență a cuvântului memorat pe cartela magnetică, atunci ușile din camera respectivă se vor deschide folosind cartela. Ileana Cosânzeana a reușit să-i trimită lui Făt-Frumos o cartelă magnetică.

# Task

Write a program that solves the following two tasks:

1. Determine the number of rooms that Făt-Frumos could reach using the card received from Ileana Cosânzeana;
2. Determine the minimum number of rooms Făt-Frumos must pass through to exit the dragon's lair (i.e., he can open the door of a room through which he reaches the outside of the lair).

# Input data

The input file `barlog.in` contains on the first line the task $c$ that needs to be solved ($1$ or $2$). The second line contains two natural numbers $n \\ m$, representing the number of lines and the number of columns of the matrix that represents the dragon's lair. On the next $n$ lines, there are $m$ words, representing the access codes of the rooms in the dragon's lair. The last line contains two natural numbers and a word $lin \\ col \\ cuv$, representing the line and the column of the room where Făt-Frumos was locked, as well as the word written on the magnetic card received by Făt-Frumos from Ileana Cosânzeana. The values on the same line are separated by spaces.

# Output data

The output file `barlog.out` will contain a single line on which a natural number will be written, determined according to task $c$.

# Constraints and clarifications

* $2 \leq n, m \leq 100$;
* The room codes and the word on the card are non-empty words, consisting of a maximum of $20$ lowercase letters of the English alphabet.
* In the test data, Făt-Frumos will always be able to exit the dragon's lair.
* Word $a$ is a subsequence of word $b$ if the letters in $a$ appear in $b$ in the same order. For example, `arma` is a subsequence of the word `marama`, but not of the word `tamara`.
* For tests worth $40\%$ of the score, the task is $1$.

# Example 1

`barlog.in`
```
1
5 4
ana are mere bune
dana cere pere multe
cra ana vrea pere
dar dan nu are
sunt bune pe care
3 2 caravana
```

`barlog.out`
```
7
```

# Example 2

`barlog.in`
```
2
5 4
ana are mere bune
dana cere pere multe
cra ana vrea pere
dar dan nu are
sunt bune pe care
3 2 caravana
```

`barlog.out`
```
2
```

## Explanations

The rooms Făt-Frumos can enter are: $(3,2), (3,3), (2,2), (3,1), (4,2), (2,1), (4,1)$.
He can exit the lair through room $(3,1)$.