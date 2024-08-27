# Dictree

Throughout this problem, we will call a letter any of the 52 Latin characters (uppercase and lowercase letters, which are considered different). We call a dictionary tree a rooted tree, where each edge is labeled with a letter. A word (finite sequence of letters) can be found in a dictionary tree if there is a path that descends in the tree, starting from the root, such that the edges on the path are labeled with the letters that form the word, in order. A picture is worth a thousand words. This dictionary tree has $10$ nodes. The following words can be found in this dictionary tree: $M, MI, MIT, Ma, i, io, ioi, iq, C$. Some examples of words that cannot be found in this dictionary tree: $Pascal, a, oi, MIM$. Given a set of words, there are infinitely many dictionary trees in which all these words can be found. Determine the number of nodes of the tree with the fewest nodes.

## Input data

The input file `dictree.in` contains on the first line the number $N$ of words. Each of the following $N$ lines contains a word (a sequence of letters without spaces). The words are not necessarily distinct.

## Output data

The output file `dictree.out` will contain a single line, which will contain the minimum number of nodes of a dictionary tree in which the given words can be found.

## Constraints and clarifications

$0 \leq N \leq 25000$  
$1 \leq$ number of letters in a word $\leq 100$

## Example

`dictree.in`  
```
5
io
iq
C
ioi
MIT
```

`dictree.out`  
```
9
```