# Words2

Archaeologists have recently discovered the ruins of the capital of the ancient civilization Ofni. After studying several inscriptions, the following observations were made regarding the orthography of the language spoken in Ofni:
- All words consisted only of lowercase English alphabet letters.
- All words had the same number of letters, $N$.
- If we associate each letter with a number corresponding to its position in the alphabet ($0$ for $a$, $1$ for $b$, $\dots$, $25$ for $z$) and each word has a code equal to the sum of the numbers associated with its letters (for example, the word $abc$ will correspond to the code $0+1+2=3$), then all the words in the Ofni language had the code divisible by $D$.

After establishing all these rules, the archaeologists would like to know how many words could have been in the language spoken in Ofni. Since the number of words can be very large, the archaeologists are satisfied with the remainder obtained when it is divided by $9967$.

## Task

Write a program that for given values $N$ and $D$, determines the remainder of the maximum number of words that the language spoken in Ofni can have when divided by $9967$.

## Input data

The file `cuvinte2.in` contains the values $N$ and $D$ on separate lines.

## Output data

The file `cuvinte2.out` will contain the required result.

## Constraints and clarifications

$1 \leq N \leq 1\,000\,000\,000$  
$1 \leq D \leq 1000$  
For $25\%$ of the tests $N \leq 50$  
It is considered that $0$ is divisible by any number.

## Example

`cuvinte2.in`
```
2 
49 
```
`cuvinte2.out`
```
3 
```

## Explanation

There are $3$ words of length $2$, whose codes are divisible by $49$. These are $aa$, $yz$, and $zy$. $aa$ has the code $0$, and $yz$ and $zy$ each have the code $49$.