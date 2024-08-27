## Task

Phineas, discovering what an aglet is, decides to surprise Ferb with a new pair of shoelaces. There are a total of $N$ distinct shoelaces, and Ferb likes only one of them, which Phineas does not know. Placing the $i^{th}$ shoelace in the shoes takes $A_i$ seconds. Phineas knows that Ferb is not very talkative, so he can only ask him repeatedly in the following manner: he first chooses a subset of the $N$ shoelaces, and after $T$ seconds, Ferb tells him whether the shoelace he likes is in that subset or not. Since he doesn't want to upset his friend but also doesn't want to waste too much time without inventing something new, help Phineas by telling him the minimum time necessary to put the preferred shoelace on Ferb's shoes, whichever it might be.

## Input data

In the input file `aglet.in` the first line will contain $N$, the number of shoelaces, and $T$, the time after which Ferb responds. The next line contains the array $A$, sorted in ascending order.

## Output data

In the output file `aglet.out` will contain the answer Phineas is asking for.

## Constraints and clarifications

$N \leq 1\ 000\ 000$

$T \leq 10^9$

$A_i \leq 10^9$, $1 \leq i \leq N$

$A_i \leq A_{i+1}$, $1 \leq i \leq N - 1$

An aglet is the plastic or metal sheath found at the end of a shoelace.

### Subtasks

Subtask 1 (20 points): $N \leq 15$

Subtask 2 (20 points): $N \leq 200\ 000$, $A_i = A_N$ for $1 \leq i \leq N$

Subtask 3 (30 points): $N \leq 200\ 000$

Subtask 4 (30 points): initial constraints

## Example

`aglet.in`

```
4 3
1 2 2 3
9
10 884 231 418 496 581 644 762 781 803 804 943
4117
```

`aglet.out`

```
9
```

## Explanation

Phineas can first ask about shoelaces $1$ and $4$. Then, depending on the answer received from Ferb, he asks the last question with one of the remaining $2$, and then puts it on Ferb's shoes. The costs will be:

If it is shoelace $1$: $3 + 3 + 1 = 7$

If it is shoelace $2$: $3 + 3 + 2 = 8$

If it is shoelace $3$: $3 + 3 + 2 = 8$

If it is shoelace $4$: $3 + 3 + 3 = 9$

The time needed to put any shoelace will be $9$ seconds. There is no other way of asking questions so that this time is less.