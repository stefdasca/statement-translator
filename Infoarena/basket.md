# Basket

During the sports class, for the basketball test (shooting at the hoop), $N$ students line up one behind the other. They soon realized that any student who comes next in line after a shorter one is evaluated more leniently. Thus, they made an agreement: For this test, they will arrange themselves so that $M$ of them are advantaged, and they will take turns for the following tests. Knowing that no two children have the same height, in how many ways can the $N$ students be arranged so that exactly $M$ of them always have a shorter colleague in front? There are $T$ tests, and the answers will be displayed modulo $P$.

## Input data

The input file `basket.in` will contain on the first line two natural numbers $T$ and $P$. The next $T$ lines will contain 2 natural numbers $N$ and $M$.

## Output data

The output file `basket.out` will contain $T$ lines, the $i^{th}$ line containing the answer for test $i$.

## Constraints and clarifications

$1 \leq M \leq N \leq 300$  
$1 \leq T \leq 10000$  
$P$ is a non-zero prime number less than $2\,000\,000\,000$  
For 10% of the tests $T \leq 100$ and $N \leq 8$  
For another 20% of the tests $T \leq 15$  
For another 20% of the tests $N \leq 50$  

## Example

`basket.in`  
```
2 666013
3 1
4 2
```

`basket.out`  
```
4
11
```