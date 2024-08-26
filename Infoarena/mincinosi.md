## Liars

HM has quite a few friends (specifically, $N$), but he doesn't know which of them to trust because many of them are notorious liars. To figure this out, he asks the following question: "How many liars are there in my group of $N$ friends?" and records each response. HM must now decide the maximum number of friends that could have answered truthfully (i.e., their answers do not contradict and specify a possibly correct number of liars), and who these friends could be. 

## Input data

The input file `mincinosi.in` contains on the first line $N$, the number of HM's friends. The next line contains the answers of those $N$ friends, the $i$-th number representing the answer of friend $i$.

## Output data

The output file `mincinosi.out` contains on the first line the maximum number of friends that could have answered truthfully. The following lines contain the indices (in the order of the input data) of these friends.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

In case there are multiple solutions with the maximum number of friends, any such solution can be printed.

A friend's response is in the interval $[0, N]$

## Example

`mincinosi.in`

```
5 
4 3 3 0 0 
```

`mincinosi.out`

```
2 
2 
3 
```

## Explanation

The friends who are telling the truth are those with indices $2$ and $3$, who mention that there are $3$ liars (the friends with indices $1$, $4$, $5$). It is observed that a solution with a non-maximum number of friends would be that friend $1$ tells the truth.