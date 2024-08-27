# Sotron2

Akane and Yukari are playing the online version of the hopscotch game together on the computer. The character they control in the game is on an infinite horizontal line. They take turns controlling the character, starting with Akane. When it's Akane's turn, the character will jump $a$ meters, either to the left or to the right. When it's Yukari's turn, the character will jump $b$ meters, either to the left or to the right. Akane likes the number $D$. Thus, she wonders if she and Yukari can work together so that the character is $D$ meters away from the initial position when it's Akane's turn.

## Input data

The first line of the input file contains the number $T$ of test cases. There follow the $T$ test cases. Each test contains a line with three numbers, $a$, $b$, and $D$.

## Output data

The output file will contain the answer for the $T$ test cases, on separate lines. If it is possible for the character to be $D$ meters from the initial position when it's Akane's turn, then print 1, otherwise print 0.

## Constraints and clarifications

For tests worth 10 points:

$T = 100000$

$0 \leq a,b,D \leq 100$

$a = b$

For other tests worth 10 points:

$T = 100000$

$0 \leq a,b,D \leq 100$

$|a - b| \leq 1$

For other tests worth 20 points:

$T = 10$

$0 \leq a,b,D \leq 100$

For other tests worth 20 points:

$T = 10$

$0 \leq a,b,D \leq 1000$

For other tests worth 40 points:

$T \leq 100000$

$0 \leq a,b,D \leq 10^9$

## Example

`sotron2.in` `sotron2.out`

4 

1 2 3 

7 8 3 

100 101 0 

1 1 1 

1 

1 

1 

0 

## Explanation

In the first test, Akane can jump one meter to the right, then Yukari two meters to the right, after which the character is 3 meters away from the initial position when Akane is at play.

In the second test, Akane can jump 7 meters to the left, then Yukari 8 meters to the right, after which the character is 1 meter away from the initial position when Akane is at play. Repeating this 3 times, the character reaches a distance of 3 meters from the initial position when Akane is at play.

In the third test, the character starts at position 0, so it is automatically at the indicated position when Akane is at play.

In the last test, no matter how the two jump, the character is always at an even number of meters from the initial position when Akane is at play, so it is impossible for it to be 1 meter from the initial position when Akane is at play.