Dk

Victor the Farmer is hungry. Unfortunately, he has run out of money and has no way to pay for his shawarma. The staff at Dristor Kebab offered him an irresistible deal: the seller gives Victor a sheet with $N$ numbers, and the hungry Victor gets a free shawarma if he quickly tells how many of the $N$ numbers on the sheet are prime. Being very hungry, Victor asks for help.

## Task

Given the $N$ natural numbers, tell how many of them are prime.

## Input data

The first line of the input file `dk.in` contains the natural number $N$ (the number of numbers on the sheet). The next $N$ lines contain the $N$ numbers $X_1 , X_2 , \dots, X_n$, one per line.

## Output data

The output file `dk.out` will contain the required value.

## Constraints and clarifications

$1 \leq N \leq 400\ 000$  
$1 \leq X_i \leq 10^9$  

For 20$\%$ of the tests  
$1 \leq N \leq 1\ 000$  

For another 20$\%$ of the tests  
$1 \leq N \leq 100\ 000$  

## Example

`dk.in`  
```
5  
6  
3  
2  
11  
9  
```

`dk.out`  
```
3  
```

## Explanation

The prime numbers are $3$, $2$, and $11$.