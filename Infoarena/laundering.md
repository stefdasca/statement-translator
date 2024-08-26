## Task

You rush out of your apartment building, but stop as you encounter Babel, the owner of the bookstore on the ground floor. The problem is not so much that you met him, but that he met you. He is very sad because he has to close his bookstore: it's not making any money, a flaw that tends to affect businesses in general. Now he wants to open another business in the same place. To get rid of the old reputation (and bad luck), he would like to change the business name to something completely different. Formally, the current name of his business is a string of lowercase letters of the English alphabet, let's call it $A$. If the new name will be $B$, then he does not want there to be any index $i$ such that the $i$-th character of $A$ is equal to the $i$-th character of $B$. Moreover, since he has evident financial problems, he would like not to use any other letters than those in $A$, but just to permute these (which will be difficult to achieve anyway, since they are made of iron). Among all possible new names, he would like the lexicographically smallest one, also for reasons of luck. You have kind of realized that Babel has no chance in business ever since he decided to install a billiard table in the bookstore. But if you don't help him now, you won't get rid of him for several months. So your task is as follows: Given a string of characters $A$, find its lexicographically smallest anagram $B$ such that $A$ and $B$ do not match at any position, or determine that no such anagram exists.

## Input data

The input file `laundering.in` contains on the first line the value $T$, representing the number of tests in the file. The next $T$ lines each contain a string $A$, representing the current name of Babel's business.

## Output data

In the output file `laundering.out` there will be $T$ lines, each containing a string $B$, representing the answer for the corresponding test, if it has a solution, or the value $-1$ if Babel's requirement cannot be met.

## Constraints

$1 \leq T \leq 100\ 000$

The sum of the lengths of $A$ within the same input file is at most $1\ 000\ 000$.

$A$ will contain only lowercase letters of the English alphabet.

## Example

`laundering.in`
```
3
ab
cra
zz
```

`laundering.out`
```
ba
acr
-1
```