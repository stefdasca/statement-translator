```markdown
# Task

Laura has recently developed a passion for **randomly** generated character strings. To help her get through the session more easily, her friends decided to cheer her up and bought her such a string of length $N$, containing only lowercase letters of the English alphabet.

This morning, Laura started listening to music on the radio and heard $M$ words, all having the same length $L$, which she liked very much. These words are also formed from lowercase letters of the English alphabet. Now she wants to see, for each word, whether it appears as a subsequence in the gifted string. Since the words are quite long, Laura is not sure if she heard them correctly, but she is convinced she did not misunderstand more than $K$ letters of each word.

Therefore, you need to tell her, for each of the $M$ words, if there exists a subarray of length $L$ in the gifted string such that the word and the subarray differ in at most $K$ positions.

# Input data

The input file `radio.in` contains:

On the first line, there are $4$ integers $N \\ M \\ L \\ K$, with the meaning given in the statement. On the next line, there are $N$ characters not separated by spaces representing the gifted string. On the following $M$ lines, there are $L$ characters not separated by spaces, representing the words that Laura heard on the radio (as she understood them).

# Output data

The output file `radio.out` will contain $M$ lines. On line $i$, you will print $1$ if there exists a subarray in the gifted string that differs in at most $K$ positions from the $i$-th word in the input file; otherwise, print $0$.

# Constraints and clarifications

* $1 \\leq N \\leq 1 \\ 000 \\ 000$
* $1 \\leq M \\leq 500$
* $1 \\leq K \\leq 50$
* $500 \\leq L \\leq 2 \\ 500$
* A string of letters `{a - z}` generated randomly means a string in which any letter `{a - z}` has the same probability of appearing at each position.
* For $10\\%$ of the tests, $N \\leq 10 \\ 000$.
* For $30\\%$ of the tests, $N \\leq 100 \\ 000$.
* For another $10\\%$ of the tests, $K = 0$.
* All tests will respect the condition $500 \\leq L \\leq 2 \\ 500$. The following example does not comply with this constraint and is not randomly generated, as its purpose is to help understand the statement.

# Example

`radio.in`
```
10 3 6 2
anaaremere
roaane
aareme
renere
```

`radio.out`
```
0
1
1
```

## Explanation

For the word `roaane`, there is no subarray in `anaaremere` such that the word and the subarray differ in no more than $2$ positions. The word `aareme` appears exactly in the given string, and for `renere`, there is the subarray `remere`, which differs by just one position.
```