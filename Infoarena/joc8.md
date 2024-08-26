# Joc8

Gigel and Alina are playing a guessing game. Gigel is thinking of a natural number greater than or equal to a certain number $x$ and less than or equal to another number $y$. Alina promises Gigel that she will guess the number he is thinking of by asking a surprisingly small number of questions in the following forms: Did you think of the number $z$? Is your number less than $z$? Gigel will only respond with Yes or No as appropriate. Gigel is skeptical because he does not know how Alina will proceed. However, we reveal Alina's secret to you. She will calculate the natural number $z$ located in the middle of the interval $[x, y]$ and will ask: "Did you think of $z$?". If Gigel's answer is Yes, the game is over because Alina guessed the number Gigel was thinking of. If the answer is No, Alina will ask, "Is your number less than $z$?". If now the answer is Yes, Alina will calculate the natural number located in the middle of the interval $[x, z-1]$ and will again ask question 1. If the answer is No, Alina will calculate the natural number located in the middle of the interval $[z + 1, y]$ and will again ask question 1. Alina's questions will continue similarly until she guesses the number Gigel is thinking of. However, Gigel is tricky, and it's possible that he might try to deceive Alina by giving at least one incorrect answer. In this case, Alina will realize she was tricked when the left boundary of the current interval becomes greater than the right boundary.

## Task

Write a program that simulates the described game.

## Input data

The first line of the input file `joc8.in` contains two natural numbers $x$ and $y$ representing the limits between which Gigel has chosen a number. The following lines contain Gigel's answers. If the answer is Yes, the file contains the digit 1. If the answer is No, the file contains the digit 0. There are always as many answers as there were questions asked by Alina.

## Output data

The first line of the output file `joc8.out` will contain the natural number Gigel was thinking of. If Gigel cheated, the first line will contain the number 0.

## Constraints

1 $\leq$ $x$, $y$ $\leq$ 10\ 000 

## Examples

`joc8.in` `joc8.out` 
100 300 
0 
0 
0 
1 
0 
0 
1 
237 

`joc8.in` `joc8.out` 
25 30 
0 
0 
0 
0 
0 
0
0 
0

## Explanation

For the first example, Alina makes the following assumptions (below by $[expression]$ we denote the integer part of the expression): 
$\left[\dfrac{(100 + 300)}{2}\right] = 200$ (question type 1, answer No, then question type 2 and answer No) 
$\left[\dfrac{(201 + 300)}{2}\right] = 250$ (question type 1, answer No, then question type 2 and answer Yes) 
$\left[\dfrac{(201 + 249)}{2}\right] = 225$ (question type 1, answer No, then question type 2 and answer No) 
$\left[\dfrac{(226 + 249)}{2}\right] = 237$ (question type 1, answer Yes)

For the second example, Alina makes the following assumptions: 
$\left[\dfrac{(25 + 30)}{2}\right] = 27$ (question type 1, answer No, then question type 2, and answer No) 
$\left[\dfrac{(28 + 30)}{2}\right] = 29$ (question type 1, answer No, then question type 2, and answer No) 
$\left[\dfrac{(30 + 30)}{2}\right] = 30$ (question type 1, answer No, then question type 2, and answer No) 
$\left[\dfrac{(31 + 30)}{2}\right]$ = no longer calculated, because $x$ has become less than $y$. It turns out that Gigel cheated.