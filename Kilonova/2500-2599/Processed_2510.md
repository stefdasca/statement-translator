At a MUN (Model United Nations) conference, $N$ delegates from around the world participate. Each delegate receives a code consisting of at least one and at most $10$ distinct uppercase letters of the English alphabet. Delegates from the same country have a code formed from exactly the same letters, possibly arranged in a different order. The codes of two delegates from distinct countries differ by at least one letter that appears in one, but not in the other. The number of delegates from the host country is at least half plus one of the total number of delegates participating in the conference, and there are at least two countries represented at the conference. At this type of conference, there is a roundtable. Delegates who will take a seat at the roundtable are those who debate (called **speakers**), and all others will receive the status of **supervisors**. The role of each delegate as well as the number of delegates who take a seat at the roundtable are not pre-established, but the protocol states that at this table no two delegates from the same country can sit in adjacent positions (left or right).
 
# Task
 
1) Determine $D$, **the number of delegations, i.e., the number of countries** represented at the conference by at least one delegate.
2) Determine two natural numbers, $S$ and $V$, $S$ representing the **minimum number of delegates who can receive the status of supervisor**, and $V$ **the number of corresponding speakers for the determined number $S$**.
3) Display the codes corresponding to the maximum number of speakers that can sit at the roundtable, in the order of seating at the table, starting from any one of them, so that if there are multiple possible arrangements, the lexicographically smallest one will be displayed.
 
# Input data
 
The first line of the input file `mun.in` contains a natural number $c$, representing the task ($1, 2$ or $3$).
 
The second line of the file contains a natural number $N$, representing the number of delegates participating in the conference, and on the third line there are $N$ words formed from at least one and at most $10$ uppercase letters of the English alphabet, representing the codes of these delegates. The words are separated by a space.
 
# Output data
 
If $c = 1$, the first line of the output file `mun.out` will contain a natural number $D$, with the meaning described in the task.
 
If $c = 2$, the first line of the output file `mun.out` will contain two natural numbers $S$ and $V$, separated by a space, with the meaning described in the task.
 
If $c = 3$, the first line of the output file `mun.out` will contain the sequence of words, separated by a space, representing the codes of the speakers who are sitting at the roundtable, according to the task $3$.
 
# Constraints and clarifications
 
* $5 \leq N \leq 10\ 000$
* We say that the sequence $x_1, x_2 \dots x_v$ is lexicographically smaller than the sequence $y_1, y_2 \dots y_v$ if there is an index $k \ (1 \leq k \leq v)$ such that $x_i = y_i$, for any $1 \leq i < k$ and $x_k < y_k$.
 
| # | Score  | Constraints         |
| - | ------ | --------------------|
| 1 | 30     | $C = 1$, the codes of the delegates consist of a single letter and $N \leq 1\ 000$ |
| 2 | 10     | $C = 1$              |
| 3 | 20     | $C = 2, N \leq 1\ 000$     |
| 4 | 10     | $C = 2$              |
| 5 | 20     | $C = 3, N \leq 1\ 000$     |
| 6 | 10     | $C = 3$              |
 
# Example 1
 
`mun.in`
```
1
5
A B B A A
```
 
`mun.out`
```
2
```
 
## Explanation
 
There are three delegates with the code `A` and two delegates with the code `B` (there are $2$ delegations)
 
# Example 2
 
`mun.in`
```
2
5
ABC BA AB BCA ABC
```
 
`mun.out`
```
1 4
```
 
## Explanation
 
The codes `ABC`, `BCA` and `ABC` are formed from the same letters, so the delegates with these codes are from the same country. The other two codes are for two delegates from another country. Therefore, there are two countries represented at the conference. To follow the protocol, we can seat at most $4$ people at the roundtable. The fifth person will receive the status of supervisor.
 
# Example 3
 
`mun.in`
```
3
5
ABC XA AX BCA BAC
```
 
`mun.out`
```
ABC AX BAC XA
```
 
## Explanation
 
There are also other ways of circular arrangement (such as `ABC XA BCA AX`), but the arrangement of delegates in the order `ABC AX BAC XA` is lexicographically the smallest.