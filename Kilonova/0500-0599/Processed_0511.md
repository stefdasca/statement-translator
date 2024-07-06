## Irina and Mihaela's Chocolate

Irina and Mihaela are sisters. One day, their mother brought them $N$ chocolate bars, numbered from $1$ to $N$, arranged in this order on a shelf. Each chocolate bar has a known weight (the number of grams it weighs). The **total amount** of chocolate consumed by a girl is equal to the sum of the weights of all the chocolate bars consumed by her. To consume chocolate, the girls must adhere to the following rules:

* The total amount of chocolate consumed by Irina must be greater than or equal to the total amount of chocolate consumed by her sister;
* The difference between the total amount of chocolate consumed by Irina and the total amount of chocolate consumed by Mihaela must be as small as possible;
* Each girl must consume at least one chocolate bar;
* Each girl eats chocolate bars from the shelf: Irina starts from the one numbered $1$ and continues, in order, from left to right, while Mihaela starts with the one numbered $N$ and continues, in order, from right to left;
* Each girl can stop eating chocolate bars at any point, with the remaining bars either left on the shelf or consumed by the other girl if she reaches them;
* Each chocolate bar is either completely consumed by one of the girls or remains on the shelf, but the girls CANNOT skip any chocolate bar.

## Task
Determine and display:
1. The most frequent weight in the initially placed sequence of chocolate bars, and if there are multiple weights that appear the same maximum number of times, choose the smallest one;
2. The minimum difference between the total amount of chocolate consumed by Irina and the total amount of chocolate consumed by Mihaela.

## Input data

The first line of the file `ciocolata.in` contains the number $C$, representing the task to be solved ($1$ or $2$), followed by the number $N$, with the meaning given in the statement, and the second line contains $N$ natural numbers, representing the weights of the $N$ chocolate bars, in the order of their numbering. The numbers on the same line of the file are separated by a space.

## Output data

The first line of the output file `ciocolata.out` will contain a single number representing either the weight determined in task $1$ (if $C = 1$) or the minimum difference determined in task $2$ (if $C = 2$).

## Constraints and clarifications

* $C \in \{1, 2\}$;
* $1 \leq N \leq 100 \ 000$;
* The weight of each chocolate bar is a non-zero natural number less than or equal to $10 \ 000$;
* It is guaranteed that there is always a solution.
* For $30$ points, $C = 1$;
* For $5$ points, $C = 2$ and $N = 2$;
* For $10$ points, $C = 2$ and $1 \leq N \leq 100$;
* For $25$ points, $C = 2$ and $1 \leq N \leq 1 \ 000$;
* For $30$ points, $C = 2$ and there are no additional constraints.

## Example 1

`ciocolata.in`
```
1 6
1 4 3 3 5 4
```

`ciocolata.out`
```
3
```

### Explanation

$C = 1$, $N = 6$, and the most frequent weights of chocolate among the $6$ are $3$ and $4$, each appearing twice. The weight $3$ will be chosen.

## Example 2

`ciocolata.in`
```
2 5
14 4 25 2 9
```

`ciocolata.out`
```
3
```

### Explanation

$C = 2$, $N = 5$, and Irina consumed the first chocolate bar (a total of $14$ grams), while Mihaela consumed the last two chocolate bars (a total of $11$ grams). Thus, the weight difference is $3$ grams.

## Example 3

`ciocolata.in`
```
2 11
3 7 3 12 4 9 4 2 6 5 17
```

`ciocolata.out`
```
1
```

### Explanation

$C = 2$, $N = 11$, Irina will consume the first five chocolate bars (a total of $29$ grams), while Mihaela consumes the last three chocolate bars (a total of $28$ grams).