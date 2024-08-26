## Task

Macarie, passionate about numbers, and especially matrices, begins one day to fill an infinite grid with numbers like this: in the top left corner $(1, 1)$ he places $0$, then writes from left to right and top to bottom the smallest number that does not appear in the respective row and column. Given the row and column of a cell in the table, find the number at that position. 

## Input data

The input file `tabela.in` contains on the first and only line the numbers $L$ and $C$, the row and column of the square whose value we want to determine. 

## Output data

The output file `tabela.out` should contain on the first line the number written on the paper at row $L$ and column $C$. 

## Constraints and clarifications 

$L$ and $C$ are natural numbers in the range $[1, 2\ 000\ 000\ 000]$

## Example

`tabela.in`
`
2 3 
`

`tabela.out`
`
5 
`

`tabela.in`
`
3 4 
`

`tabela.out`
`
7 
`

## Explanation

: The first part of the table will look like this: ~[table.png|]