Locks

To safeguard the subjects of the preONI competition, the committee that proposed the problems, consisting of $N$ people, decided to keep the subjects in a safe. A specific number of locks are required to close the safe, with each lock having a certain number of keys that can open it. The distribution of the keys among the committee members must adhere to the following conditions:
* Any two members possess the same number of keys
* Each member holds keys from distinct locks
* All the locks of the safe can only be opened in the presence of any group consisting of at least $N-1$ members

## Task

Knowing that no key can open two distinct locks, determine the minimum number of locks required, as well as a key distribution that meets the above conditions.

## Input data

The input file `lacate.in` will contain a natural number $N$, representing the number of committee members.

## Output data

The first line of the `lacate.out` file will contain two natural numbers $L$ and $C$ representing the minimum number of locks required and the number of keys that each member will have, respectively. On the next $N$ lines will be the keys held by each member, such that on line $i+1$ there will be $C$ numbers representing the keys held by member $i$; the keys are numbered from $1$ to $L$, with each number representing the lock number that the respective key opens.

## Constraints and clarifications

$2 \leq N \leq 256$

## Example

`lacate.in`
```
2
```

`lacate.out`
```
1 1
1
1
```