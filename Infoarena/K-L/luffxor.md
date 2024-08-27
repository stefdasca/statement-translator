# LuffXor

Even though he has not yet finished counting the mountains from the previous problem, Bluff was struck by a new problem idea. Enthusiastic about this new inspiration, he hurried to share it with his friends. To Bluff's disappointment, they did not seem too excited about his discovery; moreover, for unknown reasons, he was also nicknamed TractoBluff. Nevertheless, help Bluff's friends solve his problem so they don't feel inferior: We are given $V$, a multiset (the same number can appear multiple times), initially empty, on which three types of operations are performed: A type $0$ operation, given in the form $(0, x)$, inserts the number $x$ into $V$; A type $1$ operation, given in the form $(1, x)$, deletes the $x$-th number inserted into $V$. It is guaranteed that the operation is valid: it has not already been deleted and $x \leq$ the number of insertions made up to that point. Insert operations are indexed starting from $1$; A type $2$ operation, given in the form $(2, x, k)$, requires the calculation of the number of elements $y$ in $V$, with the property $y$ xor $x \leq k$. Given the operations applied to the multiset $V$, find the answers for the type $2$ operations.

## Task

## Input data

The first line of the input file `luffxor.in` contains $m$, the number of operations. The next $m$ lines contain the operations applied, one per line, in the order of their execution, in the aforementioned format.

## Output data

The output file `luffxor.out` will contain $q$ lines, where $q$ is the number of type $2$ operations executed. The answers will be printed one per line.

## Constraints and clarifications

$m \leq 200000$

$1 \leq$ all numbers in the input file $\leq 2000000000.$

The same number can appear multiple times in $V$

For $30\%$ of the tests, $m \leq 10000$

For another $10\%$ of the tests, all numbers in the input file (except for the number of operations and the indices of the delete operations) $\leq 100$

## Example

`luffxor.in`

```
5
0 1
0 2
2 3 1
1 1
2 2 3
```

`luffxor.out`

```
1
0
```