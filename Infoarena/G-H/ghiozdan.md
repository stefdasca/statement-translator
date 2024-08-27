## Backpack

The tests for this problem are not well-constructed enough to correctly distinguish inefficient or incorrect solutions. Click here if you want to help us improve the quality of the tests for this problem! Zaharel, Nargy, and Fumeanu want to go to the mountains on vacation. For this, they bought the most spacious backpack they could find, which has a capacity of $G$ grams. They also made a list with $N$ items that they want to take with them. Not all the items fit in the backpack, and since they decided not to complicate themselves, they want to fill the backpack as much as possible (of course not exceeding $G$ grams in total), but with a minimum number of items.

## Input data

The first line of the input file `ghiozdan.in` will contain the natural numbers $N$ and $G$ separated by spaces. The next $N$ lines will each contain a natural number, representing the weights of the $N$ items.

## Output data

The first line of the output file `ghiozdan.out` will contain two natural numbers $G_{max}$ and $N_{min}$ signifying that the backpack can be filled with items totaling $G_{max}$ weight ($G_{max} \leq G$), and the minimum number of items to achieve this weight is $N_{min}$. The following $N_{min}$ lines will contain natural numbers representing the weights of the items in the backpack. The sum of these numbers must be $G_{max}$.

## Constraints and clarifications

$1 \leq N \leq 20\,000$ 

$0 \leq G \leq 75\,000$ 

The weights of the $N$ items are natural numbers between 1 and 200

For a test, 60\% of the score will be awarded for correctly determining the numbers $G_{max}$ and $N_{min}$, and an additional 40\% if a set of items that can be put in the backpack is determined.

## Examples

`ghiozdan.in`
```
5 9
2
2
2
2
4
```

`ghiozdan.out`
```
8 3
2
2
4
```

`ghiozdan.in`
```
6 24
19
7
7
7
7
2
```

`ghiozdan.out`
```
23 4
2
7
7
7
```