# Mult

Two children (whose identities will not be disclosed to protect their privacy) ended up playing with a sheet of paper on which a number with $N$ digits was written. The first child, out of boredom, announces that he has found $X$ ways to obtain a multiple of a number $K$ from the number on the paper by deleting one, more, or no digits from it. The second child claims that there are $Y$ ways and thus, the two children started arguing all day.

## Task

Find the number of ways to obtain a multiple of $K$ from the initial number if the only allowed operation is the deletion of one digit so that the two children reconcile.

## Input data

The first line of the `mult.in` file contains two integers $N$ and $K$ with the meanings outlined above. The next line contains $N$ digits separated by space, which represents the number on the paper.

## Output data

The `mult.out` file will contain the number the two children are trying to find out.

## Constraints

1 $\leq$ $N$ $\leq$ 2500 

3 $\leq$ $K$ $\leq$ 500 

A number is considered correctly written even if it has the first digit 0.

## Example

`mult.in` 

```
5 3
5 4 7 0 3
```

`mult.out` 

```
11
```

## Explanation

The multiples that can be obtained are: $0$, $3$, $03$, $54$, $57$, $540$, $543$, $570$, $573$, $5403$, $5703$