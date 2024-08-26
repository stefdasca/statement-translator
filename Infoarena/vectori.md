## and a space before the specified Romanian keywords mentioned here: Task, Input data, Output data, Constraints, Example, Examples, Explanation, Explanations

# Arrays

Greg keeps explaining to Birkhoff that he is much smarter than him$\dots$ Birkhoff is fed up with Greg's arrogant remarks and, in order to get rid of him, proposes the following game to settle the matter once and for all: Each of them chooses a very difficult problem that they know how to solve and gives it to the other - the first one to correctly solve the problem proposed by the other will prove that he is the smartest! But Birkhoff is wiser: he needs peace from Greg in the next few hours because he has a very important mission to prepare. Knowing that he doesn't intend to solve the problem proposed by Greg, you have decided to help Birkhoff by solving it for him: There are $M$ relationships about $N$ non-zero arrays in the plane, distinct from each other. Such a relationship between arrays states that by multiplying each of the $N$ arrays by $-1$, $0$, or $1$ and adding the results, one obtains the zero array. It is also known that for each of the $M$ relationships there is an array that in that relationship is multiplied by $1$ and in the other $M - 1$ relationships by $0$. Given $10$ additional relationships, determine for each whether they can be deduced from the $M$ relationships or not.

## Input data

The input file `vectori.in` contains on the first line two natural numbers: $N$ and $M$. The following $M$ lines contain the $M$ relationships, one per line, coded as follows: the line of a relationship contains $N$ numbers ($-1$, $0$, or $1$), representing the coefficients by which the $N$ arrays are multiplied. The next $10$ lines contain the additional relationships.

## Output data

The output file `vectori.out` will contain a line with $10$ numbers ($0$ or $1$), representing the truth values of the $10$ additional relationships: $0$ for a false relationship and $1$ for a true relationship.

## Constraints

$5 \leq N \leq 1\ 000$

$1 \leq M \leq N - 2$

The coefficients that appear in the additional relationships are integers between $-1\ 000$ and $1\ 000$ inclusive.

## Example

`vectori.in`
```
5 2
1 1 0 0 1
0 0 1 1 -1
1 1 1 1 0
1 1 1 1 0
1 1 1 1 0
1 1 1 1 0
1 1 1 1 0
1 1 1 1 0
1 1 1 1 0
1 1 1 1 0
```

`vectori.out`
```
1 1 1 1 1 0 0 0 0 1
```

## Explanation

The two given relationships state that $v_1 + v_2 + v_5 = 0$ and $v_3 + v_4 - v_5 = 0$. Adding them together, we obtain the first 5 additional relationships: $v_1 + v_2 + v_3 + v_4 = 0$. Multiplying the first relationship by $2$ we obtain the last additional relationship: $2 * v_1 + 2 * v_2 + 2 * v_5 = 0$. The additional relationships $6 - 9$ cannot be obtained from the given ones.