The content you provided has been translated into English while preserving the required syntax and format. Here is the translated text:

```
You are given `N` distinct words composed of lowercase English letters (`a..z`). You are in front of a terminal and need to type the words. Two types of operations are allowed:
* add the last character
* delete the last character (only if the current string is not empty)

A positive natural number `K` is also given. For each `i` from `1` to `K`, you must choose `i` distinct words from the `N` such that the number of operations used to type all `i` words is minimized. A word is considered typed if at a certain moment the string written in the terminal is identical to that word.

# Input data
The file `cli.in` contains on the first line the natural numbers `N` and `K`, and on the next `N` lines are the `N` words, one per line.

# Output data
The file `cli.out` will contain `K` lines, with the minimal number of operations used to type `i` distinct words from the `N` on line `i`.

# Constraints and clarifications
* `1 \leq K \leq N`
* The sum of the lengths of the words `\leq 1\ 000\ 000`
* For `10` points: `N \leq 18`, the sum of the lengths of the words `\leq 100`
* For another `20` points: `K \leq 50`, the sum of the lengths of the words `\leq 500`
* For another `20` points: `K \leq 50`, the sum of the lengths of the words `\leq 10\ 000`
* For another `30` points: `K \leq 200`, the sum of the lengths of the words `\leq 100\ 000`
* For another `20` points: `N * K \leq 1\ 000\ 000`
* The command line starts and must end with an empty string for each `i` from `1` to `K`.

# Example
`cli.in`
```
3 3
a
b
absc
```

`cli.out`
```
2
4
10
```

Explanation
---
For `i = 1`, we choose the word `a`. The number of operations is `2`: `empty -> a -> empty`
For `i = 2`, we choose the words `a` and `b`. We need `4` operations to type them: `empty -> a -> empty -> b -> empty`
For `i = 3`, we choose all `3` words. The minimum number of operations is `10`.
```