## Task

One day, our hero Paftenie decides to throw a party. He has $N$ friends that he can invite. He also knows $M$ relations of the form $X$-th friend will only come if the $Y$-th friend also comes (and vice versa) or the $X$-th friend will not come if the $Y$-th friend comes (and vice versa). Paftenie also knows that if two of his friends have the second type of relation, he must necessarily invite one of them; otherwise, they will both be upset. Being a nice person, Paftenie decides not to upset anyone, but he still wants to have as many friends as possible at his party. He has already tried to use a computer to find out how many friends he can bring to his party, but he did not manage very well, so he asks you to do this job for him, promising that he will also invite you to the party if you succeed.

## Input data

The input file `petrecere2.in` will contain $M + 1$ lines. The first line will contain exactly two natural numbers separated by a single space $N$ and $M$, representing Paftenie's number of friends and the number of relations he knows about them, respectively. The next $M$ lines will each contain exactly one relation represented by three natural numbers $T$, $X$, and $Y$. If $T$ is $0$, then the $X$-th friend will come to the party only if the $Y$-th friend also comes (and vice versa), and if $T$ is $1$, then $X$ and $Y$ cannot both be present at the party.

## Output data

The output file `petrecere2.out` must contain exactly one natural number representing the maximum number of friends Paftenie can have at the party without breaking any of the $M$ relations.

## Constraints and clarifications

$2 \leq N \leq 100\ 000$

$1 \leq M \leq 100\ 000$

It is guaranteed that Paftenie can bring at least someone to the party. Paftenie does not necessarily know such relations for all his friends.

## Example

`petrecere2.in`
```
3 2
0 1 2
1 2 3
```

`petrecere2.out`
```
2
```

## Explanation

Paftenie can either call only friends with indices $1$ and $2$, or only the friend with index $3$. Thus, he can invite a maximum of $2$ friends.