# Words

Two friends, Marius and Andrei, thought of a game. Marius writes a sequence of $N$ numbers on a sheet of paper. Under each number, he writes a letter: under the first number the letter $A$, under the second number the letter $B$, and so on, in lexicographical order. Marius and Andrei use an alphabet with several thousand letters, known only to them, which starts with the letters from $A$ to $Z$ (to be able to use it in communication with other people as well). Therefore, the letters are used as indices for the numbers in the sequence. Andrei then looks for all the possible words that meet the following conditions: a word represents a sequence of letters, the numbers in the sequence, corresponding to the letters in a word and written in the order given by these letters, are in strictly increasing order. For example, for the sequence $2$ $1$ $3$ $5$ $4$, writing the letters $A B C D E$ below, some of the valid words are $AC$, $ACD$, $ACE$, but $AB$, $ED$ or $BDE$ are not valid words. Then Andrei chooses those words of maximum length from these words and writes them in lexicographical order. From these words of maximum length, he tells Marius the $K$-th one. If Andrei says the word correctly (and quickly), he wins the game.

## Task

Write a program that determines the required word and helps Andrei win the game.

## Input data

The input file `cuvinte.in` contains on the first line two numbers $N$ and $K$, separated by a space, representing the number of numbers in the sequence and the order number of the requested word, respectively.
The second line contains $N$ integers separated by a space, the numbers written by Marius on the paper.

## Output data

The output file `cuvinte.out` will contain the required word. Since the letters following $Z$ in the alphabet of the two friends are not known, instead of the letters of the word, the order numbers of these letters in the alphabet will be written. Thus, for example, the word $ACZ$ would be written as $1$ $3$ $26$.

## Constraints and clarifications

$2 \leq N \leq 200$  
$1 \leq K \leq 2\ 000\ 000\ 000$  
The numbers in the sequence are integers between $0$ and $10\ 000$ inclusive  
It is guaranteed that there is a solution and at most $2\ 000\ 000\ 000$ words of maximum length can be formed.

## Example

`cuvinte.in`
```
5 3
2 1 3 5 4
```

`cuvinte.out`
```
2 3 4
```

## Explanation

The numbers in the output file correspond to the positions $2$, $3$ and $4$ in the sequence where the numbers $1$, $3$ and $5$ are located.