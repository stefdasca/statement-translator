# Boltz

Before the existence of smartphones, legends say that to drive away boredom, people invented different games to play, for example, on a long bus ride. One such game is called Boltz. The players sit in a circle and start enumerating the natural numbers in turn. The first player shouts $1$, the next $2$, then $3$ $\dots$. So far, the game is not very interesting, but there is one additional rule. If the number that must be spoken contains the digit $7$ or is a multiple of $7$, the player must shout BOLTZ, after which the direction of play changes. To better understand how the game works, below is an ## example with the first $20$ turns of a game with $3$ players. If a player makes a mistake, they are eliminated from the game, and the game continues with the next player, with the next number (the direction does not change, even if the number that was missed contained the digit $7$). For example, it is Thomas's turn, followed by Charles, followed by Ronald. Thomas shouts $6$, and Charles should shout BOLTZ. If he does not, he is eliminated from the game, and Ronald now has to shout $8$. The last remaining player is the winner of the game. Thomas is a fan of statistics, so he is not interested in which player has the greatest chance to win but what the probability of that player winning the game is.

## Input data

The input file contains the first line, $N$, the number of players. Next, there are $N$ lines, each describing one of the players in the initial order of play (the first line describes the first player). Each of the $N$ lines contains two integers, $p$ and $q$, separated by a space. $p$ is the probability that the player will make a mistake when they have to shout a number, and $q$ is the probability of making a mistake when they have to shout BOLTZ. Probabilities are expressed as percentages.

## Output data

For the player with the maximum probability of winning, print that probability, expressed as a percentage, with exactly $3$ decimal places of precision.

## Constraints and clarifications

$2 \leq N \leq 8$    
$1 \leq p, q \leq 99$

## Example

`boltz.in`    
```    
2    
50 50    
50 50    
```    

`boltz.out`    
```    
66.667    
```    

`boltz.in`    
```    
3    
60 65    
40 50    
20 80    
```    

`boltz.out`    
```    
66.331    
```    

## Explanation

For the first example, each player has a  $50\%$ chance of losing when it's their turn. The second player has a higher probability of winning (intuitively, because the first player has more chances to make a mistake); it can be demonstrated that the probability is equal to $66.\(6\)\%$.