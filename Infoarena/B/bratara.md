# Bracelet

Since March 1st is approaching, Iulia is preparing some unique bracelets for her friends who are passionate about mathematics. They need to meet the following rules:
- They are sequences consisting of at least two natural numbers.
- Any two numbers, $a$ and $b$, in adjacent positions will respect the condition: the tens digit of $a$ coincides with the most significant (first from the right) digit of $b$ and the units digit of $a$ is identical to the second most significant digit (the 2nd from the right) of $b$. Additionally, if the same conditions are met by the last and first term in the sequence, then the bracelet is lucky.
- All numbers start with a digit different from 0.
- An example of such a bracelet is: $1234$ $34551$ $517890$ $9001$. The sequence $17235$ $3524$ $24758$ $58117$ is a lucky bracelet. The following sequence is not a bracelet: $1234$ $3112$ $12567$ $5642$ because $1234$ and $3112$ do not meet the adjacency requirement.

## Task

Given a sequence with $n$ natural numbers, Iulia wants to know:
1. how many bracelets she can form using only numbers in consecutive positions in the sequence that follow the given rules and cannot be extended in length
2. what is the longest lucky bracelet; if there are multiple lucky bracelets of maximum length, the leftmost one in the sequence should be recorded.

## Input data

In the file `bratara.in`:
- the first line contains a value $C$ which can be $1$ or $2$. If $C = 1$, solve Task $1$, for $C = 2$, solve Task $2$.
- the second line contains $n$ – the number of terms in Iulia's array.
- the third line contains the $n$ natural numbers of the sequence, separated by a space.

## Output data

In the file `bratara.out`, you will:
- print a natural number, representing the number of bracelets found in the sequence, if $C$ is $1$
- print three natural numbers $k$, $s$, $d$, separated by a space, with the meaning: $k$ = the maximum number of values included in a lucky bracelet, $s$ and $d$ the indices of the left and right endpoints of the requested bracelet, if $C$ is $2$;
- if there are no lucky bracelets in the sequence, print $-1$

## Constraints and clarifications

$2 \leq n \leq 100\,000$

The numbers in the sequence each have a minimum of $4$ and a maximum of $9$ digits

## Example

`bratara.in`
```
1
7
1232 32112 17235 3524 24758 51117 12234
```

`bratara.out`
```
2
```

## Explanations

$1$ $7$ $1232$ $32112$ $17235$ $3524$ $24758$ $51117$ $12234$
$2$

The two bracelets found are: $1232$ $32112$ $17235$ $3524$ $24758$
and $2$ $7$ $1232$ $32117$ $17235$ $3524$ $24721$ $21117$ $1721$
$4$ $3$ $6$

There is only one simple bracelet that includes all elements of the sequence. But the lucky bracelets are: $17235$ $3524$ $24721$ $21117$ and $21117$ $1721$

The longest bracelet is the first one, consisting of $4$ numbers, starting at position $3$ and ending at position $6$ in the given sequence.