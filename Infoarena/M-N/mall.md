# Mall

Varu has constructed a mall and rented it out to $N$ seed packaging companies. Since these companies have stalls where you can try different assortments of their products for free, Varu has decided to hire $M$ cleaners to take care of the cleanliness. These cleaners will be allocated to the $N$ companies, and they will only be responsible for the hygiene of the company they are assigned to. Since imposing staff on a company can mean a financial deficit for it, the owners have set a few conditions for Varu: if company $i$ has fewer than $C_i$ cleaners assigned, it will pay a rent of $L_i$ RON; if company $i$ has exactly $C_i$ cleaners assigned, it will pay a rent of $E_i$ RON; and finally, if company $i$ has more than $C_i$ cleaners assigned, it will pay (or receive from Varu) a rent of $H_i$ RON. As there is no relation between the three amounts ($L_i$, $E_i$, or $H_i$), the allocation of cleaners becomes a difficult problem. Help Varu to allocate all the $M$ cleaners in such a way that the total gain he can obtain from the $N$ companies is maximized.

## Input data

The first line of the file `mall.in` contains two numbers $N$ and $M$. On the next $N$ lines, there are four numbers on each line: $L_i$, $E_i$, $H_i$, and $C_i$.

## Output data

The file `mall.out` will contain a single line which will contain the maximum total gain Varu can obtain.

## Constraints and clarifications

$1 \leq N, M \leq 1\ 024$

$0 \leq L_i, E_i, C_i \leq 100\ 000$

$-100\ 000 \leq H_i \leq 100\ 000$

In case $H_i$ is negative, company $i$ will have to receive the amount $|H_i|$ RON from Varu.

## Example

`mall.in`
```
3 5
2 3 -1 2
7 2 0 3
2 1 -3 2
```

`mall.out`
```
12
```

## Explanation

If we assign two cleaners to the first company, two cleaners to the second company, and only one cleaner to the last company, then we will obtain the maximum gain $3 + 7 + 2 = 12$.