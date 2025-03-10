
~[img1.png|align=right]

Miki and Andrei have reunited, with your help, just in time for Halloween and they want to have fun together in the spirit of this holiday. Andrei found a book with phone numbers in his castle and now suggests to Miki that they make prank calls to scare the people who answer.  
Miki likes the idea, but suggests they do it in the least costly way possible.

On the first page of the book there is information about the $N$ available telephone exchanges, namely the prefix they serve (a string of digits $P_i$) and the cost to call that exchange (a natural number $C_i$). An exchange can be used to call any phone number that starts with that exchange's prefix.

After a few initial attempts, Miki and Andrei discover a secret, namely that operators with similar prefixes are friends with each other and are willing to connect them to another exchange, but for a cost, of course. Therefore, if the two want to be connected from a certain exchange $i$ to another exchange $j$, they have to pay $X \times d(P_i, P_j)$ where $d(P_i, P_j) = $ starting from prefix $P_i$, how many digits need to be deleted from the end $+$ how many digits then need to be added to the end to obtain prefix $P_j$. In other words, how many operations are needed in a text editor that only allows writing at the end and the *backspace* key to transform $P_i$ into $P_j$ (because that's what the operator has to do to redirect the call).

# Task

The prefixes and the cost for each operation are given. Miki and Andrei randomly choose $Q$ phone numbers from the book and ask you to find the minimum cost to make pranks to these numbers.

# Input data

The first line of the input contains $N$, $Q$, and $X$. Each of the following $N$ lines contains a string of digits $P_i$ and a positive integer $C_i$, separated by a space, representing the prefix and the cost of the $i^{th}$ exchange.

The next $Q$ lines contain one phone number each, represented by a string of digits.

# Output data

Print $Q$ lines, each containing an integer, the $i^{th}$ of these representing the minimum cost to call the $i^{th}$ phone number from the input, if that number can be called, or $-1$ otherwise.

# Constraints and clarifications

- $1 \leq N, Q \leq 1\ 000\ 000$
- $1 \leq S_p \leq 1\ 000\ 000$, where $S_p = $ the sum of the lengths of the prefixes
- $1 \leq S_t \leq 1\ 000\ 000$, where $S_t = $ the sum of the lengths of the phone numbers
- $0 \leq C_i \leq 10^9$ for $1 \leq i \leq N$
- $0 \leq X \leq 10^9$
- There is no prefix longer than a phone number

|#| Score | Constraints                                                |
|-|-------|-----------------------------------------------------------|
|1| 13    | $1 \leq S_p, S_t \leq 1\ 000$                             |
|2| 21    | $1 \leq N \leq 100$, $1 \leq S_p \leq 10\ 000$, $1 \leq S_t \leq 100\ 000$ |
|3| 17    | $1 \leq S_p, S_t \leq 300\ 000$                           |
|4| 12    | For any two exchanges $i$, $j$, either $P_i$ is a prefix of $P_j$, or vice versa |
|5| 37    | No additional constraints.                                 |

# Example

`stdin`
```
5 4 2
0722 5
0213 2
02 7
902 10
07 2
072212352423
021435246
9022432342
90358293022
```

`stdout`
```
2
6
10
-1
```

## Explanation

For the phone number $072212352423$, we use the prefix $07$ with a cost of $2$.

For the phone number $021435246$, starting from the prefix $07$, we modify it as follows:
- Delete $7$
- Add $2$ at the end  

And we get the prefix $02$. These two operations cost in total $2 \times X = 4$ and added with the prefix cost gives a total cost of $6$.

For the phone number $9022432342$, we use the prefix $902$ with a cost of $10$.

For the phone number $90358293022$, we have no matching prefix.

## Editorial Note

In case you get bored trying to solve this problem, we decided to include a few examples of pranks played by Miki and Andrei. They're not necessarily good, but we hope you enjoy them:

- "Hello, is your refrigerator running? ...Well, go catch it before it runs too far."
- "Hello, we need help. Goblin Ragnok has fallen in love with our paladin, but he doesn't have enough aura points to win her over. Can you donate some?"
- "Good day, a fiery wild boar has been seen wandering through your area. Make sure to barricade your doors and windows and protect your daughters."
- "Haven't you heard about the latest *glamour leopard* trend? It's very simple, you can book yourself now for a real fur transplant!"
- "Good day, we're collecting gifts for Dracula's wedding... Please don't donate stakes!"
- "[in an aggressive growl] Don't lock the door on me...[then continuing in a very polite tone] to continue the unsolicited death metal program, please press 1"
- "Good day, we're contacting you for an opinion survey on the bakery products you have recently received. You found them too stale you said? Well of course, they are made from crochet!!!"
