
To keep better track, the manager of a store creates a list of the products available in the store at the beginning of the day. He writes the names of the products, using words of the same length, composed only of lowercase letters of the English alphabet. As soon as the list is completed, he associates it with a code representing the smallest word in lexicographic order, obtained by taking one letter from each product name, in the order they are written on the list.

He observes that this code can be obtained in several ways. However, he wants to identify the variant where the chosen letters are as close as possible, in other words, the distance, representing the number of positions, between the smallest and largest positions where the chosen characters are placed, is minimal. For example:

|For the list that includes the products below|The associated code is|A variant of obtaining it where the distance is 4. The position of the letter a from the second word is 2, and the position of e, chosen in the third word, is 5.|The optimal variant is characterized by a distance of 2 because the minimum position of a chosen character is 2, and the maximum is 3.|
|---------------------------------------------|---------------------|---------------------------------------------------------------|----|
|~[img1.jpg]|**aaea**|~[img2.jpg]|~[img3.jpg]|

# Task
The file `minime.in` contains on the first line a pair of natural numbers $N$ and $M$ representing the number of products written on the list and the number of letters in each product name. On the following $N$ lines there are strings of $M$ characters (lowercase letters) representing the names of the products, in the order they were written on the list.

# Input data

The file `minime.in` contains on the first line a pair of natural numbers $N$ and $M$ representing the number of products written on the list and the number of letters in each product name. On the following $N$ lines there are strings of $M$ characters (lowercase letters) representing the names of the products, in the order they were written on the list.

# Output data

The output file `minime.out` will contain $2$ lines:
a) the first line will contain a string of $N$ lowercase letters representing the code associated with the list;
b) the second line will contain a natural number representing the minimum distance in which it can be obtained;

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$;
* $1 \leq M \leq 255$
* The word $A_1A_2\ldots A_N$ is lexicographically smaller than $B_1B_2\ldots B_N$, if there exists an index $K \leq N$ such that $A_i= B_i$ for any $i < K$ and $A_K < B_K$;
* For $50\%$ of tests $N \leq 8\ 000$;
* For the correct resolution of only task a) $20\%$ of the score is awarded, and for the correct resolution of both tasks $100\%$ of the test score is awarded.

# Example

`minime.in`
```
5 5
inele
cacao
ardei
lapte
peste
```

`minime.out`
```
eaaae
3 
```

## Explanation

The minimum distance is 3 and is obtained as follows:
in**e**le
c**a**cao
**a**rdei
l**a**pte
p**e**ste
