### Task

At the edge of a forest, there are $N$ beehives arranged in a line. They are numbered from $1$ to $N$ in the order they appear. It is the acacia flower season, and the bees are quickly collecting honey. At the end of each day, a beekeeper from a nearby village comes with a truck to collect the honey. The capacities of the trucks can be different. The honey collection process proceeds as follows: the truck starts from beehive $1$ and loads all the honey from it, then moves on to beehive $2$ and does the same, and so on. If, upon reaching a beehive, the truck cannot collect the entire amount of honey, it interrupts the collection and returns to the village. On the following day, the bees from the beehives from which honey was collected replenish the amount of honey from the previous day. Additionally, in each beehive, the amount of honey increases by one kilogram compared to the previous day.

### Task

Given $N$, the number of beehives, the amount of honey present in each at the end of the first day, the number $M$ of days when honey is collected, and the capacity of the truck that visits each day, determine the number of beehives from which honey is collected on each of the $M$ days.

### Input data

The file `miere.in` has the following structure:
- The first line contains $N$, the number of beehives;
- The second line contains $N$ natural numbers, separated by spaces. The numbers represent the amount of honey in the $N$ beehives at the end of the first day, in order from $1$ to $N$;
- The third line contains $M$, the number of trucks;
- The fourth line contains $M$ natural numbers separated by spaces. The numbers represent the capacities of the trucks, in the order they arrive.

### Output data

The file `miere.out` contains $M$ natural numbers, each on a separate line. The $i$-th line contains the number of beehives from which truck $i$ collects honey.

### Constraints and clarifications

* The amounts of honey produced by each beehive and the capacities of the trucks are specified in kilograms.
* $1 \leq N, M \leq 50\ 000$
* It is possible that a truck cannot collect honey from any beehive or can collect honey from all beehives.
* The sum of the amounts of honey in all beehives at any moment and the capacities of the trucks are strictly positive natural numbers and less than $2^{63}$.

### Example

`miere.in`
```
4
2 3 1 7
2
5 6
```

`miere.out`
```
2
1
```

### Explanation

On the first day, the truck collects all the honey from the first $2$ beehives. At the end of the second day, the amounts of honey in each beehive are: $3 \\ 4 \\ 2 \\ 8$. The truck arriving on the second day has a capacity of $6$, so it collects the honey from the first beehive but cannot collect all the honey from the second one, so it returns empty-handed and leaves.