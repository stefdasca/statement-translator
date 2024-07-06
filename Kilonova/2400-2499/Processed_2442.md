```
Amidamaru loves to do his shopping at Cora. Being his favorite store, he made a list of all the products he usually buys, represented by $n$ words.

Since Amidamaru is a well-organized person, he asked his mother to make him a complete shopping list for today, a list in which there are products from the $n$ words, each of which can appear multiple times. The list sent by his mother got corrupted when Amidamaru received it on his phone, spaces disappeared, some characters changed, and now the list is a random string of characters $S$.

Help Amidamaru recover the products that are still on the list by finding out for each of the $n$ words how many times it appears in the string of characters $S$ representing the mixed-up list, and then displaying the product with the most appearances.

# Task

Given $n$ and $S$, determine the word with the most appearances in $S$.

# Input data

The first line of the input file `cora.in` contains $S$, the string of characters.
The second line contains an integer, $n$.
The next $n$ lines contain the $n$ words as strings of characters, representing Amidamaru's products.

# Output data

The first line of the output file `cora.out` will contain a single integer, representing the maximum number of appearances of a product.
The second line will print the name of the product with the maximum number of appearances. If there are multiple solutions, the product with the smallest lexicographic name will be displayed.

# Constraints and clarifications

* $1 \leq$ Length of $S \leq 1 \ 000 \ 000$;
* $1 \leq$ Length of a word $\leq 10 \ 000$;
* $1 \leq n \leq 100$;
* A word can appear in the list only in consecutive positions of the string;
* All words consist of lowercase English alphabet characters.

# Example 1

`cora.in`
```
merepereshajdsperesscajubanan
4
mere
pere
banane
caju
```

`cora.out`
```
2
pere
```

## Explanation

In the example, `mere` appears once, `pere` twice, `caju` once, and `banane` not at all. `pere` is the product with the maximum number of appearances.

# Example 2

`cora.in`
```
primetescojhdftescoffdtescogatoruhuadeprimeprimescoprime
4
gatorade
prime
tesco
sco
```

`cora.out`
```
4
prime
```

## Explanation

`prime` and `sco` both appear exactly $4$ times, but `prime` is smaller lexicographically.
```