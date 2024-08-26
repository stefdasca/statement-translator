# Cowfood

Researchers in nutrition are conducting experiments to find the optimal mixture of herbs to feed cows. They have gathered $K$ different types of plants and mixed them, obtaining formulas represented by arrays of the form $(a_1, a_2, \dots, a_k)$ where $a_i$ represents the quantity of plant type $i$ used in the mixture. It is known that for any valid mixture, $a_1 + a_2 + \dots + a_k$ never exceeds a given value $S$. All the experiments conducted so far have failed because the cows did not like the quantities of herbs in the tested mixtures. Moreover, researchers realized that for any failed experiment of the form $(a_1, a_2, \dots, a_k)$, an experiment $(b_1, b_2, \dots, b_k)$ with $a_1 \leq b_1$, $a_2 \leq b_2$, $\dots$, $a_k \leq b_k$ will also fail.

## Task

Since researchers want to finish their work as soon as possible, it is your duty to find out how many experiments still have a chance of ending successfully.

## Input data

The first line of the input file `cowfood.in` contains three natural numbers $K$, $S$, and $N$.  
Lines 2 to $N + 1$ contain $K$ numbers $(a_1, a_2, \dots, a_k)$, each representing an experiment known to have failed.

## Output data

The output file `cowfood.out` will contain on the first line the number of remaining mixtures that still have a chance of being liked by the cows, modulo $3210121$.

## Constraints

$2 \leq K \leq 30$  
$2 \leq S \leq 10000$  
$0 \leq N \leq 20$  

## Clarifications

Any valid mixture contains at least two non-zero quantities of different herbs.  
All values given in the input file fit within 16-bit integer types.

## Example

`cowfood.in`  
```
2 5 2 
1 3 
3 1 
```

`cowfood.out`  
```
4 
```

## Explanation

The four mixtures that can still be tried are $(1, 1)$, $(1, 2)$, $(2, 1)$, $(2, 2)$.