
A grid consisting of $n$ rows and $n$ columns is considered, each element in the grid being a lowercase letter from the English alphabet. Construct the string obtained by traversing the grid in rings from the outside to the inside of the grid, each ring being traversed in a clockwise direction, starting from the top-left corner of each ring. Determine the longest sequence of characters that are located on consecutive positions in the constructed string, which is symmetric. If there are multiple such sequences of maximum length, the last one will be determined.

# Task

Given the natural number $n$ and a grid consisting of $n$ rows and $n$ columns of lowercase letters of the English alphabet, determine the longest sequence of characters located on consecutive positions in the constructed string, which is symmetric. If there are multiple symmetric sequences of maximum length, the last one will be determined.

# Input data

The file `caroiaj.in` contains the natural number $n$ on the first line, and on the following $n$ lines there are $n$ characters each, which are lowercase letters of the English alphabet.

# Output data

On the first line of the file `caroiaj.out`, print the last symmetric sequence of characters, of maximum length from the string formed by traversing the character grid in rings, from the outside to the inside of the grid, each ring being traversed in a clockwise direction, starting from the top-left corner of each ring.

# Constraints and clarifications

* $1 \leq n \leq 500$
* the lowercase letters in the grid belong to the English alphabet

# Example 1

`caroiaj.in`
```
5
abcde
bceaf
abade
abbad
ffabc  
```

`caroiaj.out`
```
abcdefedcba
```

## Explanation

The string of characters formed by traversing the grid in rings in the manner indicated in the text is: `abcdefedcbaffaabceadabbba`. 

The last symmetric sequence of maximum length is: `abcdefedcba`.

# Example 2

`caroiaj.in`
```
3
abc
def
ghi
```

`caroiaj.out`
```
e
```

## Explanation

The string of characters formed by traversing the grid in rings in the manner indicated in the text is: `abcfihgde`. 

The last symmetric sequence of maximum length is: `e`.
```
