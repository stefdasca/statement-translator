## Task

The commission has a secret string $s$ consisting of $N \ (1 \leq N \leq 100)$ lowercase English alphabet characters $(a - z)$ and you need to guess the string. You have the following types of operations at your disposal:
$? \ t$ - Is $t$ a subsequence in the secret string $s$? If yes, the commission will print $1$, otherwise, it will print $0$. The length of $t$ must not exceed $100$ characters.
$! \ str$ - The secret string is $str$. This operation can be done only once, and the commission will reward you accordingly.

NOTE: Each operation must be printed on a new line!

Formally, $t$ is a subsequence in $s$ if $t$ can be obtained from $s$ by deleting $0$ or more characters and maintaining the relative order of the remaining characters. For example: $for$, $if$, $arena$ are subsequences of the string $infoarena$.

You can perform at most $6\ 000$ operations.

Interaction

This problem is interactive. For each operation, you will proceed as follows: you will print the operation to $stdout$ and flush $stdout$ (for example with $fflush(stdout)$ in $C$ or with $std::cout \ \ll \ std::flush$ in $C++$). Then you will read the response to your operation from $stdin$:
$1$ or $0$ if your operation was of type $? \ t$;
$-1$ when the program closes, and you must stop its execution (for example $return \ 0$). You can receive $-1$ in $3$ cases: either you guessed the string, you didn't guess it, or you printed an invalid operation.

## Constraints and clarifications

$1 \leq N \leq 100$

For tests worth $30$ points, $N \leq 20$

You can use the operation $! \ str$ only once

If you do not stop the execution of the program using $return \ 0$ after receiving the response $-1$, the evaluator will print the message $KILLED \ BY \ SIGNAL \ 11$

If you do not print the newline character $'\n'$ after each operation, the evaluator will print the message $WALL \ TIME \ LIMIT \ EXCEEDED$

## Example

$stdout$ $stdin$

## Explanation

`? a` `1`
$a$ is a subsequence in the secret string

`? ba` `0`
$ba$ is not a subsequence in the secret string

`? ac` `1`
$ac$ is a subsequence in the secret string

`? abc` `1`
$abc$ is a subsequence in the secret string

`! abc` `-1`
You tried to guess the string $abc$ and the program terminates