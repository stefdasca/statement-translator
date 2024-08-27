## Sentence

Maria found a string of $N$ characters from the Latin alphabet (characters from $a$ to $z$) which she knows represents a sentence formed from one or more words, with spaces removed. Maria also learned from Gigel that any word in the sentence contains at most $K$ vowels. Now, Maria wonders in how many different ways she can reconstruct the original sentence. Because she suspects there are many possibilities, she asks you to find just the remainder when dividing the total number of possibilities by $9001$.

## Input data

The input file `propozitie.in` contains on the first line, separated by a single space, the numbers $N$ and $K$, as described above. The next line contains a string of $N$ characters, the string found by Maria.

## Output data

The output file `propozitie.out` will contain a single natural number $Res$, which represents the remainder when dividing the total number of ways to form a valid sentence by $9001$.

## Constraints and clarifications

$1 \leq N \leq 100\,000$

$1 \leq K \leq 100$

The vowels in the Latin alphabet are the letters $a$, $e$, $i$, $o$, and $u$

## Example

`propozitie.in`

```
3 1 
ana 
```

`propozitie.out`

```
3 
```

## Explanation

The three sentences that can be formed are: $a$ $n$ $a$, $a$ $na$ and $an$ $a$. Notice that the sentence $ana$ is not valid because the word $ana$ contains two vowels.