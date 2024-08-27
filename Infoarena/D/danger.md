# Danger

At elementary school number $2016$, there are exactly $N$ classes made up of $M$ children. Since the $N$ classes do not interact much throughout the year, the school principal decided to reorganize the children into $M$ classes, each made up of $N$ children, in such a way that there are no $2$ children who were initially in the same class, and after reorganization find themselves still in the same class. Furthermore, the principal knows the risk that each child adds to a class. The risk of a class is given by the maximum of the sum of the risks of any two children in that class. Thus, if a class has $3$ children with risks $1$, $2$, and $3$, the risk of that class is $5 = 2 + 3$. The principal asks you to tell him how to reorganize the children so that the highest risk of a class is minimized, and in return, he promises $100$ points.

## Task

## Input data

The input file `danger.in` will contain on the first line $2$ numbers $N$ and $M$ representing the initial number of classes and the initial number of children in each class, respectively. The next $N$ lines will contain $M$ natural numbers each representing the risks of the children. Each row of these $N$ will contain the risks of the children from a single class.

## Output data

The output file `danger.out` should contain $M$ lines, and each of these $M$ lines should contain $N$ numbers, representing the risks of the children in each class after reorganization. The $j$-th value on row $i$ will represent the risk of a child who was initially in class $j$.

## Constraints and clarifications

$$2 \leq N$$
$$M$$
$$N * M \leq 100 \ 000$$
$$1 \leq \text{the risk of a child} \leq 1 \ 000 \ 000 \ 000$$
Any correct solution that minimizes the highest risk of the classes is correct.

For tests worth $5$ points

$$N$$
$$M \leq 4$$

For tests worth another $5$ points

$$N \leq 2$$

For tests worth another $20$ points

$$N \leq 3$$

For tests worth $80$ points

$$N * M \leq 15 \ 000$

## Example

`danger.in`
```
3 3
1 2 3
3 1 2
2 1 3
```

`danger.out`
```
1 3 2
2 1 3
3 2 1
```

`danger.in`
```
5 8
3 3 1 3 5 3 8 3
```

`danger.out`
```
5 3 1 3 8 3
```

## Explanation

For the first test, $3$ new classes were formed:
- from the first child of the first class, the third child of the second class, and the third child of the third class
- from the second child of the first class, the first child of the second class, and the second child of the third class
- from the third child of the first class, the second child of the second class, and the first child of the third class

For the second example, another correct solution is:
```
5 3 1
3 8 3
```
but the following is not correct since there is no child in the first class with a risk of $3$:
```
3 5 3
1 3 8
```
Neither is the next solution correct since there are no $2$ children with a risk of $1$ in the first class before reorganization:
```
5 3 1
3 1 3
```