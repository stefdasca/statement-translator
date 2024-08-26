# Crystals

To join the shamanic cult of the ancient healers, aspirants must pass a test with multiple trials prepared by the Great Shamaness Bulbuka. The aspirant is shown three types of crystals with a unique property: if any two crystals of different types are combined, they will irreversibly transform into a single crystal of the third type (for example, given crystals of types $x$, $y$, and $z$, if $x$ and $z$ are adjacent, they transform into $y$). The test consists of $P$ trials that must be completed in sequence. In each trial, the aspirant is given a string of crystals of the three types, arranged in a special and well-thought-out order. The aspirant must use the disclosed property to determine the minimum number of crystals that can be achieved in the given string. They can transform any two adjacent crystals of different types, replacing them in the string with the newly obtained crystal.

## Task

Write a program to solve all the trials of Bulbuka's test.

## Input Data

The first line of the `cristale.in` file contains three different characters separated by a space, representing the three types of crystals. The second line contains the number $P$ of trials that make up the test. Each of the following $P$ lines contains: $n$—the number of crystals in the string followed by a space, then a sequence of $n$ characters representing the crystals in the given order.

## Output Data

The `cristale.out` file will contain on each of the $P$ lines a number, representing the minimum number of crystals that the respective string can be reduced to.

## Constraints and clarifications

$1 \leq P \leq 1000$  
the number of crystals in a string is nonzero and will not exceed $100$  
the strings are linear

## Example

`cristale.in`
```
a b c
3
3 cab
4 bcab
5 ccccc
```

`cristale.out`
```
2
1
5
```

## Explanation

$cab \rightarrow bb$ or $cc$  
$bcab \rightarrow aab \rightarrow ac \rightarrow b$  
$ccccc$ can no longer be reduced