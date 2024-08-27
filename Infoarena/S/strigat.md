# Scream

At the insistence of his aide Arthur, Tick has decided to give up his battle cry "Spoon". Tick wants his scream to be as frightening as possible for the city's villains. Tick knows that there are $M$ words that scare the villains, and if these words are included in his scream, they induce a certain degree of fear. The degree of fear induced by each word is $A_i$. The total fear degree of the scream will be $A_1 *n_1 + A_2 *n_2 + \dots + A_M *n_M$, where $n_i$ is the number of occurrences of word $i$ in the scream. Note that the occurrences of words may overlap.

## Task

Help Tick find a battle cry composed of $N$ characters that induces the maximum degree of fear.

## Input data

The first line of the input file `strigat.in` contains two integers $N$ and $M$ with the meanings from the statement. Then follow $M$ pairs of lines, the first containing a word and the second the degree of fear induced by an occurrence of it.

## Output data

The first line of the output file `strigat.out` contains the maximum degree of fear that a scream of length $N$ can induce. The second line will contain a scream that induces the respective degree of fear.

## Constraints and clarifications

$1 \leq N \leq 100$  
$0 \leq M \leq 100$  
$1 \leq$ length of a word $\leq 100$  
$0 \leq A_i \leq 1000$  
Among the $M$ words, no two words will be identical  
Finding only the maximum degree of fear will be awarded 40% of the points.

## Example

`strigat.in`  
```
4 2  
aa  
5  
ab  
6  
```

`strigat.out`  
```
16  
aaab  
```

## Explanation

`aa` appears 2 times (starting at the first and second positions), `ab` appears once, so the total fear is $5*2+6=16$. No other scream can achieve a higher value.