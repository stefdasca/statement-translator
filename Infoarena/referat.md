```markdown
Report

Dani and his friends Adi, Alex, and Ioan have to write a report for a college project. They wrote text in Latex consisting of $N$ words numbered from 1 to $N$. For each word $i$, the length of the word is known: $S_i$. Latex has a limit of $L$ characters per line. As a result, while writing the text, if they were on line $X$ and wanted to write a new word but this word no longer fit on the line, the word automatically moved to line $X + 1$. The words are written one after another without spaces (instead, they use uppercase letters to make the text clear). After much work, the boys managed to write the text in Latex. Like in any story that involves the word "college," a problem arose. The boys forgot to write a very important word of length $P$. The good part, however, was that no matter how important the word was, it did not really matter where in the text it was inserted (the reviewers wouldn't notice anyway). As a result, the 4 boys decided to insert the word somewhere such that the total number of lines increased by at least 1 (the bigger the project, the better it seems). Since they are not very good with computers, your job is to tell them in how many distinct places they can insert this new word. A word can be inserted at the beginning of the text, at the end of the text, or between 2 existing words in the text.

## Input data

The input file `referat.in` will contain on the first line $N$, $L$ and $T$ (the number of tests). The next line will contain $N$ natural numbers, the $i$-th number is $S_i$, representing the length of word $i$. On the next $T$ lines, there will be a number $P$, representing the length of the word we want to insert into the text.

## Output data

The output file `referat.out` will contain $T$ lines with exactly one natural number, representing the number of positions where the new word can be inserted such that the boys obtain at least one more line for the respective test.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$  
$1 \leq T \leq 10$  
$1 \leq P, S_i \leq L \leq 1\ 000\ 000\ 000$  
For 30% of the tests:  
$N \leq 1000$

## Example

`referat.in`  
5 10 1  
7 1 5 2 8  
4

`referat.out`  
3

## Explanations

The children have 5 words of lengths 7, 1, 5, 2, 8, let’s say the following words: Sambata A Venit Cu Beatrice, and the word we want to insert is Rece. Initially, the text placed on lines with a maximum length of 10 is:  
SambataA  
VenitCu  
Beatrice  
Depending on where we insert the word Rece, we get the following line distributions:  
Rece  
SambataA  
VenitCu  
Beatrice  

Sambata  
ReceA  
VenitCu  
Beatrice  

SambataA  
ReceVenit  
CuBeatrice  

SambataA  
VenitRece  
CuBeatrice  

SambataA  
VenitCu  
ReceBeatrice  

and  
SambataA  
VenitCu  
Beatrice  
Rece  
We observe that only if we insert the word Rece at the beginning, right before the word Beatrice, and at the end, the number of lines increases by 1. Thus, the answer is 3.
```