# Strada Cramei

After last year when the two rascals had their fill with the magical beverage, $Russky$, this year they do not want to fall short and propose to deplete the stocks of the stores on Cramei Street over $n$ days. On this street, there are $m$ stores lined up and numbered from $1$ to $m$, each supplied with a single type of drink among the millions existing in the world. Because they do not want to run out of funds, the two rascals propose to deplete the stock of a single store each day. However, the first rascal feels much more experienced and eager for strong sensations, so he desires something much more refined. To achieve this, he wrote down on a piece of paper a sequence of $n$ digits, lowercase and uppercase letters of the English alphabet, where the character at position $i$ represents the code of the drink he must consume on day $i$ to satisfy his needs. The second rascal also has his own desires to fully enjoy this new experience without too high costs, so he asks his companion that they both start from the same store on the first day, and then, on each of the $n$ days, deplete the stock of the current store and move to the next store. Unfortunately, on their path to pleasure, the first rascal loses his list, so all he can do is try to recreate it on the spot. Because he was under the influence of the magical beverage when he wrote it the first time, he cannot exactly remember the code of each drink for each day and decides to put a question mark in place of each day of which he is not sure, which means that on that day he is willing to drink any type of beverage. Since the desire of the second rascal is fulfilled by default, the two want to depart from a store such that the newly generated list by the first rascal is followed exactly. Considering they are both very tired from the journey and the only thing they want is to relax, they are asking for your help. However, knowing you are such good programmers, they are not satisfied with just the index of the store from where they should start but also ask you to tell them from the position of how many stores they can start on day $1$ such that the list is strictly followed.

## Task

## Input data

The input file $stradacramei.in$ contains on the first line a string $s$, representing the newly generated list of the first rascal, and on the second line a string $t$, representing the configuration of the stores on Cramei Street.

## Output data

The output file $stradacramei.out$ will contain on the first line the number of stores from where the two rascals can start on the first day such that the list is strictly followed.

## Constraints and clarifications

$1 \leq n \leq 200\ 000$  
$1 \leq m \leq 200\ 000$ 

## Example

$stradacramei.in$  
`s=<a?1a>`  
`t=<ab1aa1aAc1a>`  

$stradacramei.out$  
`2` 

## Explanation

The two rascals can start their adventure from store $1$ or from store $4$.