## Task

I forgot my password again! I'm sitting at the computer nervously typing incorrect passwords. All I remember is that the password consists only of lowercase letters from the English alphabet. Fortunately, the login system provides more than just "incorrect password." It also tells me the length of the longest prefix of the password I entered that appears as a subsequence (not necessarily contiguous) in the correct password. Formally, for a password $P = p_1 \ p_2 \ \dots \ p_N$ and the entered string $Q = q_1 \ q_2 \ \dots \ q_N$, the response of the login system is the largest $L$ for which there exist indices $1 \leq k_1 < k_2 < \dots < k_L \leq N$ such that $q_i = p_{k_i}$ for all $1 \leq i \leq L$. The system also tells me $N$, the length of my password, and $S$, meaning that the password contains only the first $S$ letters of the alphabet. For example, $S = 4$ means that my password contains only $a, b, c, d$ (not necessarily all of them).

Help me recover my password!

## Interaction

This problem is interactive. Initially, you will read from `stdin` $N$, the length of the password, and $S$. To enter a string, output it to `stdout`, followed by `\n`, and then flush `stdout` (e.g., with `fflush(stdout)` in C or `std::cout << std::flush` in C++). The interactor will respond in `stdin` with $L$, the length of the longest prefix that appears as a subsequence in the correct password.

The interaction terminates either when you find the correct password ($L = N$) or after you have made the 50\,000th query.

## Constraints

- You can input a maximum of 50\,000 passwords.
- For 10\% of the score, $N \leq S \leq 26$ and the characters in the password are distinct.
- For 20\% of the score, $2 \leq N \leq 100$, $2 \leq S \leq 4$.
- For 20\% of the score, $2 \leq N \leq 2000$, $2 \leq S \leq 20$.
- For 30\% of the score, $2 \leq N \leq 3500$.
- For 20\% of the score, $2 \leq N \leq 5000$.

## Example

```
stdout  stdin
3       2
ab      2
abb     2
bab     1
aab     3
```

## Explanation

The correct password is `aab`. The interactor provides $N = 3$ and $S = 2$. For the query `ab`, $L = 2$ (`a a b`). For the query `abb`, $L = 2$ (`a a b`). For the query `bab`, $L = 1$ (`aa b`). For the query `aab`, $L = 3$ (`aab`) and the interaction stops because the correct password has been found.