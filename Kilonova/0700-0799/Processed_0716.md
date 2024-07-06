Two children are painting a fence consisting of $n$ planks numbered from $1$ to $n$ as follows: the first child uses a bucket of red paint to paint the planks numbered $p$, $2 \cdot p$, $3 \cdot p$, etc. The second child does the same, starting from the same end of the fence but uses a bucket of blue paint and paints every $q$-th plank. Therefore, when they finish painting, the fence will have many unpainted planks, some planks painted red, others painted blue, and some painted purple (those that have been painted with both red and blue).

# Task

Knowing the numbers $n, p$, and $q$, display:

1. How many planks remain unpainted
2. How many planks are painted red
3. How many planks are painted blue
4. How many planks are painted purple

# Input data

The first line of the input file `gardul.in` contains the value $n$, representing the number of planks of the fence. The second line of the input file contains the values $p$ and $q$, separated by a space.

# Output data

In the output file `gardul.out`, print, in order, the four required natural numbers, each on a separate line, as in the example.

# Constraints and clarifications

* $1 \leq n \leq 100 \ 000$;
* $1 \leq p, q \leq 40 \ 000$;

# Example

`gardul.in`
```
25
4 6
```

`gardul.out`
```
17
4
2
2
```

## Explanation

The example corresponds to the following situation:

|.|.|.|R|.|A|.|R|.|.|.|v|.|.|.|R|.|A|.|R|.|.|.|V|.|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

`A` – blue  
`R` – red  
`V` – purple