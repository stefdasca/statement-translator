## Task

The vampires from Twilight were not satisfied with the massive number of avid fans. So they attacked the organizing members of the Freshmen Ball at the Faculty of Mathematics and Computer Science of the University of Bucharest. The transformation began with a single individual. Then this individual transformed at most two other individuals in turn, since each vampire has two transformations at their disposal. Thus, each transformed individual continued to transform others until all members of the Mathematics and Computer Science Students Association became vampires. This scenario can be represented as a binary tree, where the root is the first transformed individual, and the children of a node are exactly the members they transformed. The problem the vampires are facing is that they've made a mess during these transformations, and they need to clean up. They know only two ways to clean up: 1) if it's $X$'s turn to clean up, $X$ will ask the first transformed to clean up, if they exist, then $X$ cleans up, and afterward, they will ask the second transformed, if they exist. 2) if it's $X$'s turn to clean up, $X$ will clean up first, and then they will ask the first transformed, if they exist, to clean up, and afterward the second transformed, if they exist. Given the two cleanup orders, you need to determine who transformed whom.

## Input data

The input file `curatenie.in` contains the following:
- The first line contains $N$, the number of transformed members.
- The next two lines contain the two orders: the second line contains the order of type 1 and the third line contains the order of type 2.

## Output data

The output file `curatenie.out` contains $N$ lines, where line $i$ contains 2 numbers, representing the two individuals transformed by member $i$. If one of them does not exist, print 0 for that respective individual.

## Constraints and clarifications

1 $\leq$ $N$ $\leq$ 500\ 000  

The numbers in the input file range between 1 and $N$.  

Note that an individual might choose not to transform anyone or use only the first or only the second transformation, depending on the order.

## Example

`curatenie.in`
```
4
1 4 2 3
3 1 2 4
```

`curatenie.out`
```
2 4
0 2
4 0
1 0
0 0
```

`curatenie.in`
```
7
4 2 5 1 3 7 6
1 2 4 5 3 6 7
```

`curatenie.out`
```
2 3
4 5
0 6
0 7
0 0
0 0
0 0
```