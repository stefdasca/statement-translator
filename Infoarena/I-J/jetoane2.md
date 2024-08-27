Tokens 2

After multiple failed attempts to win the lottery, WW decides to give up and take up gambling. He quickly gained experience and even began to win handsome amounts of money (the amounts earned are strictly confidential). It doesn't matter how he managed to learn so much in such a short time, what matters is that the other day WW came across a rather tricky game. He has in front of him a number of tokens, placed next to each other, on which the lowercase letters of the English alphabet are inscribed (one letter on each token). He can perform the following move on the string: choose a subarray from this string, extract it, and then join (if possible) the two remaining pieces. To make the game even more thrilling, each letter has a weight $p_i$. Moreover, WW cannot choose any subarray, but only one from the list of $N$ valid moves (which is obtained at the beginning of the game through an uninteresting algorithm). A valid move is represented by a string of at most 10 characters. When WW extracts a certain subarray, he gets a numeric score equal to the sum of the weights of each letter that makes up that subarray.

## Task

WW will provide the string of tokens, the weights of each letter, as well as the list of valid moves. He asks you to help him determine the maximum score he can obtain.

## Input data

The first line of the file `jetoane2.in` contains 26 natural numbers, less than 1000, representing the weight of each letter. The second line contains the initial string of tokens followed, on the third line, by the number of valid moves, $N$. The next $N$ lines contain a string of at most 10 characters each, representing the description of a move.

## Output data

The first line of the file `jetoane2.out` will contain the maximum number requested by WW.

## Constraints

1 \leq N \leq 170

1 \leq length of the initial string \leq 170

All letters in the input file will be lowercase letters of the English alphabet

Two letters can have the same weight

For 30% of tests N \leq 9

For simplicity and fluidity of the statement, WW can be read as Doubleu

## Example

`jetoane2.in`
```
2 5 3 1 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
aabcdee
5
ab
cd
be
ae
acd
```

`jetoane2.out`
```
19
```

## Explanation

Initially, the string is "aabcdee". WW first extracts the string "cd" ("aab ee"), obtaining the string "aabee" and the cost $1+3=4$. The next move is extracting the string "be" ("aa e"), obtaining the string "aae" and the cost $4+(5+4)=13$. The last subarray extracted is "ae", the string becoming "a" and the final cost, $13+(2+4)=19$.