A number is called **special** if the sum of its even digits is greater than the sum of its odd digits.

For example, the numbers $1278$, $84$, $289$ are special numbers. The numbers $1298$, $742$, $9773$ are not special numbers.

On a weekend day, after finishing all their homework for the coming week, since the weather was bad outside and they were bored, Alina and Cristina decided to play a game. They wrote a number on each of $n$ cards, stacked the $n$ cards, and established the following game rule: Each of them draws a card in turn (Alina, being the oldest, draws the first card). They form a new number from the last two digits of the number drawn by Alina and the first two digits of the number drawn by Cristina and check if it is a special number. They set aside the two cards and draw two more cards in turn. At the end of the game, they want to find out which was the largest special number formed.

# Task

Determine the largest special number formed during the game.

# Input data

The input file `specialmax.in` contains on the first line an even number $n$, representing the number of cards, and on the following lines, the $n$ natural numbers written on the $n$ cards.

# Output data

The output file `specialmax.out` will contain the largest special number formed according to the game rule.

# Constraints and clarifications

* $n$ is a non-zero even natural number, with a maximum of $6$ digits;
* The numbers written on the cards are non-zero natural numbers with at least two digits and a maximum of $6$ digits;
* It is guaranteed that at least one special number will be formed from the numbers in the file.

# Example

`specialmax.in`
```
8 
98 
312 
7125  
4048 
403 
26 
31987 
25673
```

`specialmax.out`
```
2540
```

## Explanation

In the first round of the game, Alina drew the card with the number $98$, Cristina drew the one with the number $312$. The number formed according to the game rule is $9831$, which is not a special number.

In the second round of the game, Alina drew the card with the number $7125$, Cristina the one with the number $4048$.

The number formed according to the game rule is $2540$, which is a special number.

In the third round of the game, the number obtained after drawing the two tickets is $326$, which is a special number.

After the fourth round, the number $8725$ is obtained, which is not a special number.

The largest special number obtained is: $2540$