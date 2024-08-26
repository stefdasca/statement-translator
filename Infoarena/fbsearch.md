# Facebook Search

For this problem, you will need to implement the Facebook search function for a user. When we type a person's name, Facebook gives us suggestions from the very first letter entered. These suggestions are personalized based on their relevance to each user. Thus, if $Traian$ types "e", it will autocomplete "$Emil\ Boc$", and if $Vasile$ types "e", it will autocomplete "$Elena\ Popescu$". There will be $M$ operations:
- $Q\ X$ - Display the search result for the string $X$ entered, based on relevance. If two users have the same relevance, the lexicographically smallest one will be displayed.
- $U\ User\ R$ - Add $R$ to the specified user's relevance (this is based on common interests, proximity, likes, etc).

## Input data

The input file `fbsearch.in` contains on the first line $T$, the number of tests. In the following, for each test you will find:
The first line contains $N$, the number of users and $M$, the number of operations.
The next $N$ lines contain the users.
The next $M$ lines contain the described operations.

## Output data

In the output file `fbsearch.out`, print the answers to the $Q$ type questions. If there is no answer, print "Search Bing for $X$", where $X$ is the search string.

## Constraints and clarifications

$1 \leq T \leq 3$  
$1 \leq N \leq 100\ 000$  
$1 \leq M \leq 100\ 000$  
$0 \leq R \leq 10$  
Users and queries will not have more than $32$ characters and will only contain characters from the English alphabet and the character "$_$" (no spaces). Case is not considered in searches, but users must be displayed as in the input file. Initially, relevance is $0$ for all users.

## Example

`fbsearch.in`  
```
1  
5 7  
AndreiPopescu  
GiuliaMateescu  
AndreiAnton  
Teo  
Teodor  
Q An  
Q BiEnCuTzA  
U AndreiPopescu 1  
Q andr  
Q Teo  
U Teodor 1  
Q Teo
```  
`fbsearch.out`  
```
AndreiAnton  
Search Bing for BiEnCuTzA  
AndreiPopescu  
Teo  
Teodor
```