# With Clean Hands

- Our gangsters are not like the American ones - ours have no tradition! - I hope we won't let them form one! - Without a doubt, and yet lately there have been gangs using weapons, the ones I told you about and a few more that I managed to wipe out, against them you can't find witnesses, nor evidence. I have a simple method - I rely on the fact that most of them are nervous and hysterical, manage to get them to pick up weapons, and then whoever shoots first... and since I'm quite good at that... I even like it, I admit! - So let's repeat: We reach Semaca... through Buciurligă. - The one with the van robbery? - Semaca's rival, and we reach Buciurliga through Pascu, his right-hand man. Do you approve the scheme? - Let's approve it! Only things couldn't be that simple - the connection between Buciurliga and Semaca was going to be made through Lăscărică. And before taking out Semaca, commissioners Roman and Miclovan first had to deal with his monstrous coalition of gangsters: Pleoarca, Şchiopu, and Burdujel. To simplify things in the future, the party activist prepared a list of priorities in their sector - more precisely, the most relevant criminal minds sorted by their importance in the eyes of the leadership. As often happens in practice, the ideals of the leadership differ from those of the subordinates, so, using his intuition, Miclovan wrote down the "true" importance of each gangster, in the form of a positive integer. The commissioners agreed to eliminate the gangsters in ascending order of their real importance for ease of function and to sow panic among them. However, they wouldn't want to get on the party secretary's bad side - they will suppress figures only in ascending order of official priorities. Additionally, to eliminate as much criminal activity as possible, they will go through the received list in ascending index order, choosing to eliminate a gangster each time his importance is strictly greater than that of the last eliminated one (you, being awarded computer scientists, know this is not necessarily the best possible algorithm to make these choices). It was war, values were overturned, armed hand attacks became normal, so managing Bucharest's situation became a fundamental time-consuming problem - The commissioners ask for your help in writing a program to automate the following operations: Following significant events (such as the robbery of Lembert Jewelry), the importance of a figure changes - 1 $pos$ $val$ - the importance of the $pos$-th criminal on the list becomes $val$. 2 $pos$ - The commissioners want to know if they start from the gangster at position $pos$, using the mentioned method, how many gangsters would be suppressed? 

## Task

## Input data

The first line of the input file `cumainilecurate.in` contains two integers $N$ and $M$, separated by a space, indicating the number of gangsters on the received list and the number of queries respectively. The second line contains $N$ positive integers separated by spaces, representing the importance of each mafia member on the list, in order. The next $M$ lines each have one of the structures 1 $pos$ $val$ or 2 $pos$, with the meanings from the statement. 

## Output data

The file `cumainilecurate.out` must contain as many lines as there are type 2 operations in the input file, each line representing the answer for the corresponding type 2 operation from the input.

## Constraints and clarifications

$1 \leq N \leq 10^5$ 

$1 \leq M \leq 6 \cdot 10^4$

$1 \leq$ importance of a gangster $\leq 10^9$

Attention! Large volume of input data, we recommend optimizing the reading using this code.

### Subtask 1 (20 points) 

$1 \leq N \leq 3000$

$1 \leq M \leq 2000$

### Subtask 2 (20 points) 

It is guaranteed that in the input there will be at most 10 operations of type 1.

### Subtask 3 (60 points) 

Initial constraints


## Example

`cumainilecurate.in`
```
5 11
1 5 3 4 2
2 1
2 2
2 3
2 4
2 5
1 2 2
2 1
2 2
2 3
2 4
2 5
```

`cumainilecurate.out`
```
1
2
3
4
5
1
2
3
4
5
```

## Explanation

First example

For the first 5 queries, these are the chosen gangsters: `1 5 3 4 2` (it is clear here that the calculated strategy of the commissioners is not the best, the optimal variant being, in fact, `1 5 3 4 2` )

`1 5 3 4 2`

`1 5 3 4 2`

`1 5 3 4 2`

`1 5 3 4 2`

After modifying the importance of gangster number 2, the list looks as follows: `1 2 3 4 2`

For the next 5 queries, these are the chosen gangsters: `1 2 3 4 2` (it is noted that, this time, the strategy of the commissioners is the correct one)

`1 2 3 4 2`

`1 2 3 4 2`

`1 2 3 4 2`

`1 2 3 4 2`

Second example Gangsters chosen are: `3 1 4 2 5`