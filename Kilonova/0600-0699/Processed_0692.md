Cosmin and Lensu were walking on the dangerous beaches of Egypt when they saw a shark "carrying" behind it a string of characters $s$. Since Harry Potter taught them how to communicate with animals, Cosmin and Lensu tamed the shark, making it give them the string of characters. They want to keep it, but the shark told them that it will take it back if they do not answer several questions it will ask.

# Task

Given a string of characters $s$ and $T$ queries of the form $left, \ right$. The shark asks you if the letters in the subarray $[left, \ right]$ of the string `s` can be rearranged to form a palindromic word.

# Input data

The first line will contain the natural number $T$, and the second line will contain the string of characters `s`, representing the number of questions the shark asks. In the following $T$ lines, there will be two numbers, $left$ and $right$, representing the beginning and the end of the subarray on which the query is made. The numbers on the same line are separated by a single space.

# Output data

You will print $T$ lines, on each line $i \ (1 \leq i \leq T)$ containing a single word, "YES" or "NO", the answer to the shark's question $i$.

# Constraints and clarifications

* The string s consists only of lowercase English letters;
* $2 \leq |S| \leq 5 \ 000 \ 000$, where $|S|$ is the length of the given string;
* $1 \leq T \leq 1 \ 000 \ 000$;
* $1 \leq left \leq right \leq |S|$;
|#|Points|Constraints|
|-|-|--------|
|1|31|$T \leq 50$ and $|S| \leq 10^5$ |
|2|47|$T \leq 100 \ 000$ and $|S| \leq 10^5$ |
|3|22| Without any additional constraints |

# Note

Due to the very large input data, use the following instructions at the beginning of your program:
```c++
ios_base::sync_with_stdio(false);
cin.tie(nullptr);
cout.tie(nullptr);
```

# Example

`stdin`
```
2
zabac
2 4
3 5
```

`stdout`
```
YES
NO
```

## Explanation

The letters in the subarray [2, 4] already form a palindromic word in the given string order, so the answer to the first query is "YES".
The letters in the subarray [3, 5], specifically a, b, and c, cannot be rearranged to form a palindromic word. Thus, the answer to query number 2 is "NO".