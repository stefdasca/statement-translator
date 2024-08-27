# Pagination

Narud3 newspaper's editorial team has recently received material about the effects of snow in Romania from their favorite reporter, Damia. The text sent by Damia consists of $N$ words, each on a separate line. Since the text needs to be arranged on the page in the newspaper, the editorial team is asking for your help! The formatting rules are as follows: Each page has $x$ lines and $y$ columns. On every line, the first character must be the first letter of a word, and the last character must be the last letter of a word (assuming that at least two words fit on a line). The number of spaces between words on a line should be equal if possible; otherwise, the spaces at the beginning will be one character longer. Pages will be separated by an empty line.

## Input data

The first line of the input file `paginatie.in` contains two integers $x$ and $y$ representing the number of lines and the number of columns on a page. Each of the following lines of the input file will contain a word.

## Output data

The output file `paginatie.out` must contain the text formatted as described above.

## Constraints

$1 \leq x,y \leq 1\ 000$  
The words consist of lowercase letters, uppercase letters, digits, or symbols.  
The input file will contain at most $300\ 000$ words.  
The solution is required with the minimum number of lines, and in case of equality, the solution should be the smallest lexicographically (the characters ' ' and '\n' (newline) are considered the largest in ASCII from a lexicographical point of view, the other characters keeping their order).  
The length of a word is at most $50$.  
There will always be a solution.

## Example

`paginatie.in`  
```
4 12
Nu
este
asa
greu
sa
rezolvati
aceasta
problema!
Este
gheata
pe
sosele
:(
```

`paginatie.out`  
```
Nu  este asa
greu      sa
rezolvati
aceasta
problema!
Este  gheata
pe sosele
:(
```