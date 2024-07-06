Un proprietar vinde un teren de formă dreptunghiulară împărțit în $M \times N$ parcele de formă pătrată cu lungimea laturii de o unitate. Fiecare parcelă costă $V$ lei. Vlad s-a interesat și a aflat pentru fiecare din parcelele terenului care este valoarea de revânzare. El constată că unele parcele i-ar putea aduce profit, iar altele i-ar aduce pierdere. Fiind isteț, negociază cu proprietarul să cumpere atâtea parcele de teren câte pot fi împrejmuite cu un singur gard de lungime egală cu $2M+2N$ unități. Terenul are pe fiecare din cele patru laturi acces la drumul exterior, pe o porțiune de lungime egală cu o unitate. Vlad negociază astfel încât terenul achiziționat să conțină și cele patru parcele de acces la exterior.

# Task
Knowing $M$ and $N$ — the dimensions of the land, the resale values for each parcel of the land, $V$ — the purchase price of each parcel, and $x_{nord}$, $x_{sud}$, $y_{vest}$, and $y_{est}$ — the positions of the parcels with access to the exterior road, determine:
1. The profit $P_{\text{arie\_minimă}}$ that Vlad can obtain after purchasing and then reselling the area of land with the minimum area, fenced according to the negotiated conditions.
2. The maximum profit $P_{\text{max}}$ that Vlad can obtain after purchasing and then reselling an area of land fenced according to the negotiated conditions.

# Input data
The file `fence.in` contains on the first line the number $t$.
For all input tests, the number $t$ can only have the value $1$ or $2$.
The second line contains the numbers $M$, $N$, $V$, $x_{nord}$, $x_{sud}$, $y_{vest}$, and $y_{est}$ separated by a space, and on the next $M$ lines contain $N$ natural numbers separated by a space, representing the resale values of the $M \cdot N$ land parcels.

# Output data
If the value of $t$ is $1$, then only Task 1 will be solved.
In this case, the output file `fence.out` will contain on the first line the number $P_{\text{arie\_minimă}}$.
If the value of $t$ is $2$, then only Task 2 will be solved.
In this case, the output file `fence.out` will contain on the first line the number $P_{\text{max}}$.

# Constraints and clarifications
- $3 \leq M, N \leq 1\ 000$
- $1\ 000 \leq V \leq 10\ 000$
- $2 \leq x_{nord}, x_{sud} \leq N-1$
- $2 \leq y_{vest}, y_{est} \leq M-1$
- $(x_{nord} - x_{sud}) \cdot (y_{est} - y_{vest}) \geq 0$
- The resale value of any land parcel is a natural number in the range $[1, 20\ 000]$.
- The profit is understood as the sum of the resale values corresponding to the fenced parcels from which the product of the purchase price $V$ and the number of fenced parcels is subtracted, and it can be negative.
- For a correct resolution of the first task, $20\%$ of the score will be earned.
- Task 2 contains tests worth 30 points where the condition $M, N \leq 15$ is met.

# Example 1
`fence.in`
```
1
5 7 6 3 5 3 2
3 5 8 4 9 8 7
9 3 7 6 4 5 9
6 6 8 2 5 4 8
3 3 4 7 7 2 1
8 7 9 2 8 4 2
```
`fence.out`
```
3
```

## Explanation
$M=5$, $N=7$, $V=6$, $x_{nord}=3$, $x_{sud}=5$, $y_{vest}=3$, $y_{est}=2$
~[img1.png|width=25em]
$P_{\text{arie\_minimă}} = (8+7+6+4+5+9+6+6+8+2+5+7+8) - 6 \cdot 13 = 81-78 = 3$

# Example 2
`fence.in`
```
2
5 7 6 3 5 3 2
3 5 8 4 9 8 7
9 3 7 6 4 5 9
6 6 8 2 5 4 8
3 3 4 7 7 2 1
8 7 9 2 8 4 2
```
`fence.out`
```
8
```

## Explanation
$M=5$, $N=7$, $V=6$, $x_{nord}=3$, $x_{sud}=5$, $y_{vest}=3$, $y_{est}=2$
~[img2.png|width=25em]
$P_{\text{max}} = (8+4+9+8+7+7+6+4+5+9+6+6+8+2+5+7+7+8) - 6 \cdot 18 = 116 - 108 = 8$