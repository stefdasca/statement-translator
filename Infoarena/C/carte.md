# Book

Even though there are still a few days left until Christmas, Santa has already brought Georgica his gifts because he has been very good. He found under the tree a book titled "The Book Without Spaces". As the name suggests, the book contains words that are not separated from each other. Thus, we say that it consists of a sequence of lowercase letters of the English alphabet. To understand the book's message as best as possible, Georgica needs to separate the words such that the sum of the lengths of the words he does not understand is minimized. Georgica understands a word if it is in his language's dictionary. Given the number of tests $T$, and for each test the content of the book, the number of words in the dictionary $N$, and the $N$ words from the dictionary, determine the minimum sum of the lengths of the words Georgica does not understand after he separates the text in a convenient way.

## Input data

The input file `carte.in` contains on the first line $T$, the number of tests. Next, for each test, the first line contains the string representing the content of the book, the second line contains the natural number $N$, and the following $N$ lines contain one word from Georgica's dictionary each.

## Output data

The output file `carte.out` will contain $T$ lines, with the line $i$ containing the answer for test $i$.

## Constraints and clarifications

$T = 10$  
$1 \leq N \leq 1,000$  
The book does not contain more than $3,000$ characters.  
The words in the dictionary will have at most $3,000$ characters.  
Georgica's dictionary can contain two identical words.

## Example

`carte.in`
```
1
abcd
3
ab
bc
a
```

`carte.out`
```
1
```

## Explanation

Georgica will split the text into words as follows: "a bc d". Among these, only one word is not found in the dictionary - "d", and its length is $1$.