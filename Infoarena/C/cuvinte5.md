# Words5

The difference between two words is defined as the square of the minimum number of additions, deletions, or modifications of characters needed to transform one word into the other. For example, to transform $'abc'$ into $'ba'$ in $2$ such modifications, we can do $'abc' \rightarrow 'bc' \rightarrow 'ba'$ , hence the difference between the two words is $2^2 = 4$ . Consider a dictionary. The distance between two words, $A$ and $B$, which do not necessarily belong to the dictionary, with an additional parameter $K$ , is defined as the smallest sum of the differences between consecutive words of a sequence of up to $K + 1$ words, where the first one is $A$, the last one is $B$, and the rest of the words belong to the dictionary. Suppose the dictionary contains only the words $lavera$, $lauera$, and $lalala$. Then the distance between the words $laverita$ and $laura$, when $K = 3$, is obtained by transforming $laverita$ into $lavera$, $lavera$ into $lauera$, and $lauera$ into $laura$. When $K = 2$, however, the distance will be greater, as we will transform $laverita$ into $lavera$ and $lavera$ into $laura$.

## Task

You are given a dictionary of $N$ words and $Q$ queries of the form $K \ A \ B$. For each query, you are required to find the distance from word $A$ to word $B$, with the additional parameter $K$.

## Input data

The first line contains $N$, the number of words in the dictionary. The second line contains the $N$ words, separated by a space. The third line contains $Q$, the number of queries. The next $Q$ lines contain each a query, given in the form $K \ A \ B$.

## Output data

For each query, print a line with the answer.

## Constraints

$1 \leq N \leq 50$  
$1 \leq Q \leq 2500$  
$1 \leq Length \ of \ the \ words \leq 7$  
$1 \leq K \leq N + 1$  
The words are composed of lowercase letters of the Latin alphabet.  
For tests worth $20p$, the queries contain only words from the dictionary (tests $1, 2, 3, 4$).  
For another $20p$, $K = N + 1$ (tests $5, 6, 7, 8$).  
For another $10p$  
$1 \leq Q \leq 50$ (tests $9, 10$).

## Example

`words5.in`  
```
5 
a aa aaa aaab aaabb 
6 
2 a aaaa 
3 a aaaa 
5 ab aaabbb 
4 ab aaabbb 
6 xxx yyy 
6 zz azab
```

`words5.out`  
```
5 
3 
5 
6 
9 
7 
```

## Explanation

For the first query, we can do $'a' \rightarrow 'aaa' \rightarrow 'aaaa'$, the cost is $4 + 1 = 5$  
For the second query, we can do $'a' \rightarrow 'aa' \rightarrow 'aaa' \rightarrow 'aaaa'$, the cost is $1 + 1 + 1 = 3$  
For the third query, we can do $'ab' \rightarrow 'aa' \rightarrow 'aaa' \rightarrow 'aaab' \rightarrow 'aaabb' \rightarrow 'aaabbb'$, the cost is $1 + 1 + 1 + 1 + 1 = 5$.  
For the fourth query, we can do $'ab' \rightarrow 'aaab' \rightarrow 'aaabb' \rightarrow 'aaabbb'$, the cost is $2^2 + 1 + 1 = 6$  
For the fifth query, we can do $'xxx' \rightarrow 'yyy'$, the cost is $3^2 = 9$  
For the last case, we can do $'zz' \rightarrow 'aa' \rightarrow 'aaa' \rightarrow 'aaab' \rightarrow 'azab'$, the cost is $2^2 + 1 + 1 + 1 = 7$