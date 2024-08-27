# Sentence2

Dubota received a task from his computer science teacher to split a text into sentences and then into words. However, since he was not paying attention, he noted down something else as his task. He receives a string $S$ and a dictionary composed of $C$ words. Words are identified solely by the characters they are composed of, meaning any permutation of the characters of a word represents the same word. For example, if we have a word identified by the characters adt, then the following character sequences: dat, tda, or tad all represent the same word. Now, Dubota needs to split the initial string into words that form a sentence. A sentence is a sequence of words such that each character of the initial string belongs to a word and only one word, and any word is part of the dictionary. In a sentence, a word from the dictionary can appear multiple times.

## Task

Determine how many possibilities Dubota has to split the string $S$ into sentences. Since this result can be very large, it is enough to determine the result modulo $666019$.

## Input data

In the output file `propozitie2.in`, the first line contains a string of characters, $S$, and the second line contains a number, $C$. The following $C$ lines each contain a string of characters representing a word from the dictionary.

## Output data

In the output file `propozitie2.out`, print a single number representing the required result.

## Constraints and clarifications

$C \leq 5000$ 

the length of the string $S \leq 5000$ 

the length of a word in the dictionary $\leq 100$ 

Words are composed of lowercase letters of the English alphabet ('a' - 'z'). 

Note: The dictionary may contain homographs (different words that have the same spelling).

## Example

`propozitie2.in`

```
acbad
5
bac
ad
a
bc
d
```

`propozitie2.out`

```
5
```

## Explanation

The 5 possibilities to split the initial string into words, identified by the indices of the words from the dictionary:

$1, 2$  
$1, 3, 5$  
$3, 1, 5$  
$3, 4, 2$  
$3, 4, 3, 5$