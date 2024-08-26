## Task

Pe strada principal a unui lost city there are $N$ stores aligned in a straight line. Each store sells a bottle of Русский Стандарт for the price $v_i$. Two scoundrels plan to consume the magical elixir for $L$ days non-stop, but want to vary the tastes. Thus, each starts from a store, $X$ and respectively $Y$, buying a single bottle and advancing one position each day. Scoundrel 2 is secretly disappointed by his friend's desire to consume harmful substances non-stop and considers an act of banditry to evade as many of the $L$ days as possible: If the sum of the prices paid is less than $P$, he will say that the two bottles do not reflect his financial power, and if it is more than $P$, he will accuse his friend of spending too much money on liquids, refusing to drink in both cases. If on a certain day both scoundrels consume, that day will receive the title $KNP$, otherwise, the day is declared $KNN$. If fewer than $Z$ of the $L$ days are $KNP$, Scoundrel 1 will renounce his friend, and if there are more, Scoundrel 2 will attribute his potential health problems to his friend. Tell for a number of $Q$ queries from how many pairs of cities $(X,Y)$ can the two start so that exactly $Z$ out of the $L$ days are $KNP$, and their relationship is not affected. In other words, $(x,y)$ is a solution if the equality is satisfied: (with "==" denoting the binary equality operator that can take values 0 or 1) 

## Input data

The input file `russky.in` contains the input data arranged as follows: 
```
N 
Z 
v_1 v_2 $\dots$ v_N 
Q 
L_1 P_1 $\dots$ L_Q P_Q 
```

## Output data

The output file `russky.out` will print $Q$ numbers, one on each line, representing the answers.

## Constraints and clarifications

1 
$\leq$ 
$Z$ 
$\leq$ 
$L$ 

$i$ 
$\leq$ 
$N$ 
$\leq$ 
1000 

1 
$\leq$ 
$v_i$, $P$ 
$\leq$ 
$10^9$ 

1 
$\leq$ 
$Q$ 
$\leq$ 
100000 

## Example

`russky.in` 
```
10 2 3 3 2 2 3 2 1 1 
2 3 9 5 2 
6 2 10 2 
1 3 2 3 
3 3 3 4 
3 5 3 6 
3 3 
3 1 
0 2 
5 
7 6 
5 
```

`russky.out` 
```
0 
```

## Explanation

For the first query $L=5$, and $P=2$. For example, $v_7 + v_7 =P$, but also $v_8 + v_8 =P$ are in number of $Z = 2$. Both could start from $7$, but the number of remaining days would be less than $L$. The remaining solutions are $(4,4)$ $(5,5)$ $(6,6)$ due to $L=5$.