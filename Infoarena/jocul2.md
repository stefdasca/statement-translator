## Task

"You just lost the game!" said the old man... SPOILER ALERT Michael asked the true Mr. Jones to leave Section One along with Nikita. Clearly having big plans for her, the true Mr. Jones refused! Michael, employing unorthodox means, reached an agreement with Nikita's father. Michael knows that the old man is an excellent player of the game, so he challenged him to a match, agreeing that the loser will respect the winner's wish. END OF SPOILER The official rules of the game are as follows: Initially, there are $N$ cards on the table. Each card has an integer $V_i$ written on it, between $0$ and $1023$. The old man goes first. The player whose turn it is waits for the referee's verdict: the referee can decide that either the old man has won, Michael has won, or the game continues. If the referee announces that the game continues, the player whose turn it is selects a card and removes it from the table, passing the turn to the other player. If no cards are left on the table, the referee immediately announces that the old man has won. Knowing how vague the official rules of the game are, Michael studied all the matches played by the old man and discovered both the unwritten rule of the game that the referee uses to make announcements as well as the old man's playing strategy. The referee looks at the cards on the table and calculates $S$, the xor sum of their values. Then: he announces the old man as the winner with a probability of $\frac{3}{40} - \frac{(S / 1024)}{20}$; he announces Michael as the winner with a probability of $\frac{1}{40} + \frac{(S / 1024)}{20}$; he announces that the game continues with a probability of $\frac{9}{10}$. When he has to take a card, the old man always applies the same nondeterministic strategy: he looks at the cards on the table and calculates $S$, the xor sum of their values. Then, for each card $i$, inscribed with the value $V_i$, he calculates the weight of the card: $P_i = (S \oplus V_i) + 1$. Having calculated all the weights, he selects one of the cards with a probability proportional to its weight. The game hasn't started yet, only the cards have been placed on the table, but the old man has already pronounced: "You just lost the game!" Michael wants to know how true the old man's words are, so he asks you about his real chances of winning if he follows an optimal strategy.

## Input data

The input file `jocul2.in` contains on the first line the natural number $N$, representing the number of cards initially on the table, and on the second line $N$ natural numbers, representing the values of the cards ($V_i$).

## Output data

The output file `jocul2.out` will contain a single real number $P$, representing Michael's real chances of winning if he follows an optimal strategy.

## Constraints and clarifications

$1 \leq N \leq 20$  
$0 \leq V_i \leq 1023,$  
$1 \leq i \leq N$  
Michael is very meticulous, so he has imposed that you calculate $P$ with a precision of $10^{-4}$.

## Example

`jocul2.in`  
$1$  
$512$

`jocul2.out`  
$0.05$

## Explanation

Initially, the old man is to move. The referee can decide with a probability of $\frac{1}{40} + \frac{512}{1024 \times 20} = 0.05$ the victory of Michael and with a probability of $\frac{3}{40} - \frac{512}{1024 \times 20} = 0.05$ the victory of the old man. Alternatively, with a probability of $0.9$ the game continues, in which case the old man chooses the only card on the table and is declared the winner. In conclusion, Michael's chances of winning are only $0.05$.