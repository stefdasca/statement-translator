## Task

This time Algorel only has to deal with three types of balls which he needs to decorate the Christmas tree with. Normally, Algorel knows how many balls he has of each type: $NrBile_1$, $NrBile_2$, $NrBile_3$. All balls of type $i$ have the same integer $Numar_i$ inscribed on them. For his amusement, Algorel decided to decorate the tree so that the sum of the numbers inscribed on the balls hung on the tree is exactly $S$. Since he can find such an arrangement quite quickly and has nothing else to do until Santa arrives, he decided to count how many such arrangements exist. Two arrangements are considered identical if they use exactly the same number of balls of each type.

## Input data

The input file `plus.in` contains an integer $S$ on the first line representing the sum of the numbers inscribed on the balls in a valid arrangement. The next 3 lines describe the types of balls: line $i+1$ contains two integers separated by a space, $NrBile_i$ and $Numar_i$, with the above meaning.

## Output data

The output file `plus.out` will contain a single integer representing the number of distinct arrangements.

## Constraints

$-1 \leq Numar_i \leq 1$  
$0 \leq S, NrBile_i \leq 100000$  

For 40% of the tests  
$0 \leq S, NrBile_i \leq 300$  

For another 30% of the tests  
$0 \leq S, NrBile_i \leq 5000$  

Algorel recommends using 64-bit integers 

## Example

`plus.in`  
```
1
1 0
1 -1
2 1
```

`plus.out`  
```
4
```

`plus.in`  
```
0
1 1
-1 2
1 3
```

`plus.out`  
```
1
```

## Explanation

The possible arrangements for the first test are as follows (each arrangement is specified by the number of balls used of each type):  
arrangement 1: $0, 0, 1$  
arrangement 2: $1, 0, 1$  
arrangement 3: $0, 1, 2$  
arrangement 4: $1, 1, 2$  

The last arrangement respects the rule because $1*0 + 1*-1 + 2*1 = 1$.  

For the second test, there is only one arrangement with sum 0:  
the one in which we don't put any balls on the tree.