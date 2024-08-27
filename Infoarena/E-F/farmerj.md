## Task

Rob Kolstad is angry with Farmer John and his cows due to recent troubles faced by the USACO team (lack of funds, stolen problems, etc.). Being superstitious, he believes the problems stem from Farmer John's name. Therefore, he wants to change Farmer John's name. To achieve this, Rob has a string $S$. He wants to obtain 2 character strings that will form the new name for Farmer John and have the following properties:
- There must be a way to interlace the 2 strings such that the resulting string is a subsequence of the string $S$ (note! subsequence is different from subarray).
- The sum of the lengths of the 2 strings must be maximum

Besides these conditions, the 2 strings must satisfy certain pronunciation criteria. Specifically, there are $M$ pairs of characters that cannot appear one after the other in either of the 2 names.

## Input data

The first line of the input file `farmerj.in` contains the string $S$ that Rob has. The second line contains the integer $M$. The next $M$ lines each contain 2 alphanumeric characters that cannot appear one after the other in either of the 2 names.

## Output data

The output file `farmerj.out` will print 2 lines. The $i$-th of the 2 lines will contain the positions within the string $S$ of the characters that make up the $i$-th name. These positions must be printed in ascending order. 

## Constraints

$1 \leq$ length of the string $S \leq 50$

The string $S$ is composed only of alphanumeric characters.

Evidently, the character at any position $i$ in $S$ can belong to only one of the 2 names.

Any of the 2 names can contain 0 characters.

## Examples

`farmerj.in`    
```
FJOHNARMERZ  
14  
FJ  
FO  
FH  
FN  
ZF  
ZJ  
ZO  
ZH  
ZN  
ZA  
ZR  
ZM  
ZE  
ZR  
```  

`farmerj.out`  
```
1 6 7 8 9 10  
2 3 4 5  
```  

`farmerj.in`    
```
123456789  
5  
81  
84  
89  
56  
68  
```  

`farmerj.out`  
```
1 2 3 4 5 9  
6 7 8  
```  

`farmerj.in`    
```
1223  
2  
22  
23  
```  

`farmerj.out`  
```
1 2 4  
3  
```  