## Task

Due to the approaching summer, the City Authorities, although tired after the fight with the snow from the just-ended winter, are preparing to fight the mosquitoes. To face the upcoming challenge, they must first calculate the number of harmful mosquitoes that will invade the City on the first day of summer. It is known that there are two types of mosquitoes: harmful and harmless. Moreover, it is also known that on day $0$ (today), there is only one harmful mosquito and no harmless mosquitoes. Each day, each mosquito transforms into $K$ mosquitoes of the same type and $P$ mosquitoes of the other type. Knowing that summer arrives in exactly $N$ days, the Authorities ask you to calculate the number of harmful mosquitoes that will invade the City on the first day of summer. Since this number can be very large, the City's salvation can be achieved even if only the required number modulo $666013$ is known.

## Input data

The input file `invazie.in` contains on the first line the number $T$ of tests. The next $T$ lines contain three numbers in the order $K$ $P$ $N$, having the meaning described in the statement.

## Output data

In the output file `invazie.out` you will print $T$ lines, each line containing the required result for the corresponding test from the input file.

## Constraints and clarifications

$1 \leq T \leq 100000$.

$0 \leq K$, $P \leq 2000000000$.

$0 \leq N \leq 10^{18}$.

For $20\%$ of the tests, $T \leq 100$ 

and 

$N \leq 1000$.

## Example

`invazie.in`
```
3
1 2 5
3 4 0
2 2 2
```

`invazie.out`
```
121
1
8
```