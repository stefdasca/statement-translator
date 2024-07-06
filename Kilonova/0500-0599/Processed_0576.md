```markdown
# Problem statement

You have a keyboard with $27$ keys, specifically: all the lowercase letters from the English alphabet and the `Backspace` key.

You have a search bar that is initially empty. When a key that is not `Backspace` is pressed, the letter corresponding to that key is added to the end of the word in the search bar.
If the key pressed is `Backspace`, the last letter in the search bar is deleted, if one exists. Otherwise, nothing happens.

Given $N$ and a string of characters, in how many ways can you reach the given string after pressing exactly $N$ keys?

# Input

The first line contains $N$. The second line contains the string of characters you need to reach.

# Output

Print the number of ways to reach the given string modulo $10^9+7$, which is a prime number.

# Constraints and clarifications

- $1 \le \text{length of the given string} \le N \le 5000$.

# Example

`stdin`
```
3
a
```

`stdout`
```
53
```

## Explanation

If we denote `B` as a backspace, the ways to reach the string `a` are:
`aBa`, `bBa`, ... , `zBa` - $26$ ways
`BBa` - $1$ way
`aaB`, `abB`, ..., `azB` - $26$ ways

In total, there are $53$ ways.
```