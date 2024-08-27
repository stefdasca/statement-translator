## Task

On the island of Java, cruel experiments are conducted on some of the most beautiful creatures in the world, the beetles. $M$ researchers conduct experiments on $N$ beetles. Unfortunately, after devising an intelligent plan, all the beetles escaped from the laboratory and fled to different parts of the island. The researchers must bring the beetles back to continue the experiments. To do this, each researcher is sent to find at most one beetle. The beetles are numbered from $1$ to $N$. Researchers have badges with numbers from $1$ to $M$. A researcher can search for a beetle only if they have ever performed an experiment on that beetle (otherwise, they wouldn't recognize it). Knowing the experiments that took place before the beetles escaped, determine the maximum number of beetles that can be brought back to the laboratory after a finite amount of time. It is known that if a researcher is sent to search for a beetle, they will find it in a finite amount of time (because it would be impossible for a Java beetle to be smarter than a researcher).

## Input data

The first line of the file `java.in` contains the natural number $T$, representing the number of tests. The $T$ tests will be described as follows. The first line of each test contains three natural numbers: $M$, $N$, and $E$. $M$ is the number of researchers, $N$ is the number of beetles, and $E$ is the number of experiments that have taken place. The next $E$ lines contain two natural numbers $A$ and $B$, meaning that researcher $A$ conducted an experiment on beetle $B$. A researcher can conduct multiple experiments on the same beetle.

## Output data

For each test, print a line in the file `java.out` containing a natural number: the maximum number of beetles that can be brought back to the laboratory after a finite amount of time.

## Constraints and clarifications

$1 \leq T \leq 6$

$1 \leq N, M \leq 10000$

$0 \leq E \leq 200000$

## Example

`java.in`

```
2
4 5 2
1 2
1 2
3 3 5
1 1
1 2
2 2
3 3
1 3
```

`java.out`

```
2
3
```