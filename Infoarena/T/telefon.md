# Phone

The test cases for this problem are not well-constructed enough to accurately differentiate between inefficient or incorrect solutions. Click here if you want to help us improve the quality of the tests for this problem! We have a phone where the number buttons are arranged as shown in the adjacent figure. This phone is operated by a robot that initially has its control head above the $*$ button. The robot is commanded with the following commands:

- $S\  x$ – the control head moves $x$ units up
- $J\  x$ – the control head moves $x$ units down
- $DR\  x$ – the control head moves $x$ units to the right
- $ST\  x$ – the control head moves $x$ units to the left
- $A$ – the control head presses the button above which it is located.

At the end of dialing the number, the head must be positioned above the $\#$ button.

## Task

Write a program that reads a phone number, with at most $10$ digits, and then dials that number using the robot, following a path of minimum length over the keyboard.

## Input data

The input file `telefon.in` contains an integer, representing the phone number to be dialed.

## Output data

The output file `telefon.out` will contain the commands that the robot must execute to dial the given phone number. The commands will be written on a single line, in the order in which the robot must execute them. Two commands will be separated by a single space.

## Example

`telefon.in` 
`123804`

`telefon.out` 
`S 3 A DR 1 A DR 1 A J 2 ST 1 A J 1 A S 2 ST 1 A J 2 DR 2`

## Explanation

First, we need to move the control head from above the $*$ button to above the $1$ button. For this, we move up $3$ positions $(S\  3)$ and press the button $(A)$. Next is the $2$ button, so we move the head one position to the right $(DR\  1)$ and press $(A)$. To reach the $3$ button, again we move one position to the right $(DR\  1)$ and press $(A)$. To get above the $8$ button, first we move the head down $2$ positions $(J\  2)$, then left one position $(ST\  1)$ and press $(A)$. The $0$ button is below the $8$, so we move down $(J\  1)$ and press $(A)$. Now we need to get to $4$, so we move up $2$ positions $(S\  2)$, then move the head one position to the left $(ST\  1)$ and press $(A)$. Finally, we move the head above the $\#$ button with the commands $J\  2$ and $DR\  2$. Here, we do not need to press the button.