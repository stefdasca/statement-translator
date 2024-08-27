# Chameleons

The Zeylanicus chameleons are renowned for their behavior. If such a chameleon is touched, it changes its color from red to green or from green to red. For her birthday, Cami received four such chameleons as a gift. To study their behavior, she lined them up on a table and observed that at the beginning, they were all red. She started touching them randomly. After $n$ touches, Cami looked at the colors of the chameleons and wondered: in how many ways could I have touched the chameleons to reach this state?

## Task

Write a program that, given a known number of touches, $n$, and a state of the four chameleons, determines the number of ways (modulo $666013$) in which this state can be reached after exactly $n$ touches. 

## Input data

The input file `cameleoni.in` contains on the first line the number $n$ of touches and on the second line, four letters, separated by spaces, encoding the colors of the four chameleons, from left to right, after $n$ touches.

## Output data

The output file `cameleoni.out` will contain on the first line the number of ways (modulo $666013$) to reach the given state after exactly $n$ touches.

## Constraints and clarifications

$1 \leq n \leq 2000000000$ ($2 \cdot 10^9$)  
Colors are encoded by $R$ for red and $G$ for green  
The initial configuration of the chameleons is $R R R R$  

## Example

`cameleoni.in` `cameleoni.out`

## Explanation

`2 R R R R`  
`4`  
There are four ways to reach the given state:  
$1)$ $R R R R \to G R R R \to R R R R$  
$2)$ $R R R R \to R G R R \to R R R R$  
$3)$ $R R R R \to R R G R \to R R R R$  
$4)$ $R R R R \to R R R G \to R R R R$

`2 G R R G`  
`2`  
There are two ways:  
$1)$ $R R R R \to G R R R \to G R R G$  
$2)$ $R R R R \to R R R G \to G R R G$