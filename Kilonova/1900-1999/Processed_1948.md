**"He can call me a flower if he wants to... I don’t mind..."**

After helping to chase away the dust sprites, Henry and Hetty found a job that truly tests their cleaning talent. Specifically, they got employed at a newly established skunk farm. This farm initially consists of $N$ empty cages, arranged in a line. To start the skunk breeding activity, they will perform $M$ operations of the form:
* $1 \\ c_{nr} \\ m_{nr} \\ p_{nr}$: Henry and Hetty bring the $nr$-th skunk to the farm, which they place in cage $c_{nr}$. This skunk has a smell $m_{nr}$ and a smell loss coefficient $p_{nr}$.
* $2 \\ l \\ r$: Henry and Hetty need to find out the minimum smell in a cage within the range $[l, r]$. The smell in a cage $y \\ (1 \\leq y \\leq N)$ is defined as $ max ( m_x - p_x \\times |y - c_x| ) $, for $1 \\leq x \\leq nr, \\ nr$ being the number of skunks brought to the farm until the current operation.

# Input data

The input file `flower.in` will contain two natural numbers $N$ and $M$, with the meaning given in the statement. The following $M$ lines will contain descriptions of the $M$ operations. The first number on each line, type, indicates the type of the operation. If $type = 1$, on that line there will be three more natural numbers $c_{nr}, m_{nr}, p_{nr}$ meaning that the $nr$-th skunk, brought to cage $c_{nr}$, has a smell $m_{nr}$ and a smell loss coefficient $p_{nr}$. If $type = 2$, on that line there will be two more natural numbers $l\\ r$, meaning that Henry and Hetty need to find out the minimum smell in a cage within the range $[l, r]$.

# Output data

The output file `flower.out` will contain, in order, one per line, the answers to the type $2$ operations read from the input file.

# Constraints and clarifications

* $ 1 \\leq N \\leq 200 \\ 000$;
* $ 1 \\leq M \\leq 500 \\ 000$;
* $ 1 \\leq c_x \\leq N$, for each type $1$ operation.
* $ 1 \\leq m_x, p_x \\leq 1 \\ 000 \\ 000 \\ 000$, for each type $1$ operation.
* $ 1 \\leq l \\leq r \\leq N$, for each type $2$ operation.
* Each skunk brought to the farm has a smell loss coefficient greater than or equal to the previous skunk brought. In other words, $p_x \\leq p_{x+1}$ for any $x$, $1 \\leq x < nr$.
* A cage can contain multiple skunks at one time.
* The answer to each type $2$ operation can be represented as a signed $64$-bit integer.
* The answer to a type $2$ operation can be negative.
* For $20%$ of the tests, $N \\leq 1 \\ 000$ and $M \\leq 3 \\ 000$.

# Example

`flower.in`
```
4 6
1 3 5 2
1 1 8 3
2 1 4
1 4 10 4
2 3 4
2 1 2
```

`flower.out`
```
3
6
5
```

## Explanation

The $6$ operations have the following meanings:

1. A skunk is brought to cage $3$ which has a smell of $5$ and a smell loss coefficient of $2$.
2. A skunk is brought to cage $1$ which has a smell of $8$ and a smell loss coefficient of $3$.
3. Now, the cage with the minimum smell in the interval $[1, 4]$ is cage $4$, where the smell value is $3$.
4. A skunk is brought to cage $4$ which has a smell of $10$ and a smell loss coefficient of $4$.
5. Now, the cage with the minimum smell in the interval $[3, 4]$ is cage $3$, where the smell value is $6$.
6. Now, the cage with the minimum smell in the interval $[1, 2]$ is cage $2$, where the smell value is $5$.