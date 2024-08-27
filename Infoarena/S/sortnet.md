Sortnet

A sorting network consists of $N$ data lines, numbered from 1 to $N$, connected by comparators. Each data line carries numeric values; initially, $N$ arbitrary values are introduced into the network, and the network is expected to output a permutation of these numbers. A perfect sorting network will output the values in ascending order. Comparators are placed between two data lines to arrange the two values in ascending order. A comparator can connect any two lines, $A$ and $B$, with $A < B$; such a comparator is symbolically denoted as $< A , B >$ or graphically represented by a vertical segment between the two data lines. The graphical notation uniquely determines the comparator. Imagine a segment connecting lines 1 and 3; this represents the comparator $< 1 , 3 >$, as $< 3 , 1 >$ cannot be a comparator (see the definition above). In this problem, the number of data lines will always be even. A sorting cycle consists of $N/2$ comparators, such that each line is connected to exactly one comparator. A complete sorting network of depth $M$ is a sorting network consisting of $M$ sorting cycles. An example is worth a 1000 words: The network in the figure has 4 data lines and 2 sorting cycles. It can be observed that this sorting network is not perfect. Although it correctly sorts the data in the figure (the sequence $7, 8, 7, 3$), it will not correctly sort the sequence $1, 3, 2, 9$.

## Task

It can be demonstrated that if a network correctly sorts any input consisting only of the numbers 0 and 1, it will correctly sort any sequence of numbers. Thus, we can say that the better a network is, the more correctly it sorts inputs formed from the numbers 0 and 1. There are $2^N$ such inputs; write a program that determines how many of these possible inputs are correctly sorted by a given network (by correctly sorted, we mean that all zeros appear before all ones in the output).

## Input data

The input file `sortnet.in` will contain $N$ and $M$ integers on the first line, representing the number of data lines, and the number of sorting cycles, respectively. Each of the following $M$ lines represents $N/2$ comparators, in the format $< A , B >$, with $A$ and $B$ integers between 1 and $N$, $A < B$. No number will repeat in the description of a sorting cycle (each line is connected to exactly one comparator in each cycle).

## Output data

The output file `sortnet.out` will contain the number of inputs formed only from the numbers 0 and 1, that are correctly sorted by the given network.

## Constraints and clarifications

2 $\leq N \leq 20$ and $N$ even

0 $\leq M \leq 32$

## Example

`sortnet.in`
```
4 2
<1,3> <2,4>
<3,4> <1,2>
```

`sortnet.out`
```
14
```

## Explanation

The example corresponds to the figure; the two sequences formed from the digits 0 and 1 that are not correctly sorted are $0, 1, 0, 1$ and $1, 0, 1, 0$.