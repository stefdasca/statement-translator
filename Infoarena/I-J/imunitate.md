# Immunity

The Chamber of Deputies is composed of $N$ deputies, numbered from $1$ to $N$. After the scandal with the vote of the new Penal Code, a restructuring is desired. A list of $M$ pairs of deputies has been found, who if left together would negatively influence each other. It is desired that the new Chamber of Deputies not be penal. This means there should be no deputy who is negatively influenced by more than half of his remaining colleagues. Thus, a deputy who does not meet this condition is selected and eliminated. We need to find the number of ways in which a non-penal Chamber of Deputies can be formed.

## Input data

The input file `imunitate.in` contains on the first line $T$, the number of tests. For each case, there is a line with $2$ natural numbers: $N$ and $M$ with the meanings from the statement. Next, there are $M$ lines that contain two natural numbers $ZG$ and $PO$, indicating that deputies $ZG$ and $PO$ negatively influence each other.

## Output data

The output file `imunitate.out` will contain on each line the required result for each of the $T$ tests.

## Constraints and clarifications

$1 \leq T \leq 20$ 

$1 \leq N \leq 18$ 

$1 \leq M \leq N^2$ 

It is possible that the same pair of deputies appears multiple times.

Two ways are different if the remaining deputies differ.

## Example

`imunitate.in`

```
2
4 6
1 2
1 3
1 4
2 3
2 4
3 4
4 4
1 2
3 2
1 3
4 2
```

`imunitate.out`

```
4
3
```

## Explanation

For the first example, the four possible ways are: $1$; $2$; $3$; $4$. 

For the second example, the three possible ways are: $1, 3, 4$; $1, 4$; $4, 3$.