## Task

On the occasion of winter holidays, Flamanzila thinks it would be a good time to steal some pigs to satiate his hunger. Therefore, he finds $N$ pigs in Ionel's yard. Each pig has a tag of a specific color with the number of kilograms of the pig inscribed on it. To ensure Ionel doesn't notice the pigs are missing, Flamanzila will never steal two pigs consecutively that have the same tag color. Each time he comes to steal, Flamanzila will steal the fattest pig he can find in Ionel's yard, respecting the above condition. Determine the maximum total weight that Flamanzila can steal knowing the total number of pigs, $N$, and the number of colors used for the tags, $K$.

## Input data

The input file `placute.in` will contain the natural numbers $N$ and $K$ on the first line. On the next $N$ lines, there will be 2 natural numbers $g[i]$ and $c[i]$, representing the data for pig $i$ - its weight and the color of its tag.

## Output data

The output file `placute.out` will contain a single natural number, representing the maximum total weight Flamanzila can steal.

## Constraints and clarifications

$1 \leq N \leq 100000$

$1 \leq K \leq 1000$

$1 \leq g[i] \leq 1000000$

$1 \leq c[i] \leq K$

Ionel does not have 2 pigs with the same weight.

## Example

`placute.in`

```
5 3 
5 1 
4 3 
1 2 
2 2 
3 2
```

`placute.out`

```
12
```