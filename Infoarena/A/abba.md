# Abba

X spent his 4 years at the Theoretical Institute of Informatics waiting for a diploma which indicated he graduated from "high school". In his free time (practically his whole time was free), he came across the following scenario: The kids from the humanities were playing with some words, but without fully understanding what it was about (if they knew better, they might not have gone into humanities). Each child says in turn a sentence (a sequence of words), following this rule:
First child: $a$ $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_$ $b$
Second child: $a$ $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_$ $ab$ $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_$ $b$
Third child: $a$ $\_\_\_\_\_\_$ $aab$ $\_\_\_\_\_\_\_\_\_$ $ab$ $\_\_\_\_\_\_$ $abb$ $\_\_\_\_\_$ $b$
Fourth child: $a$ $\_\_$ $aaab$ $\_\_$ $aab$ $\_\_\_\_$ $aabab$ $\_\_$ $ab$ $\_\_$ $ababb$ $\_\_$ $abb$ $\_\_$ $abbb$ $\_$ $b$
In other words, the first child says the words 'a' and 'b', and after him, each child repeats what the previous one said, adding between every two words the concatenation of these words. X has several questions, which can be formulated in computational terms as below. The question is a word, and the answer for it is which child says that word for the first time, and which word it is in his list, respectively $-1$ if that word does not appear at all.

## Task

The first line contains $Q$, the number of words X is thinking about. The following $Q$ lines each contain one word.

## Output data

For each of the $Q$ words, on a separate line, print either $x$ $y$ meaning that the first appearance of the word is at the $x$-th child, and the word is the $y$-th in the list of the $x$-th child modulo $10^9 + 7$, or $-1$ if it does not appear at all.

## Constraints and clarifications

$1 \leq Q \leq 10^4$
The sum of the lengths of the $Q$ words X is thinking about does not exceed $10^6$.
The words X is thinking about are formed from lowercase letters of the English alphabet.
The answer must be printed modulo $10^9 + 7$.

Subtasks
$10$ points: the sum of lengths is at most $1000$, it is guaranteed that all words appear, and they appear for the first time in the first $10$ sentences. $(test$ 1$)$
$20$ points: all words appear, and they appear for the first time in the first $14$ sentences. $(tests$ 2 and 3$)$
$10$ points: all words appear, and they appear for the first time in the first $100$ sentences, in the first $100$ words of that sentence, and their length is at most $100$. $(test$ 4$)$
$30$ points: the words X is thinking about are chosen pseudo-randomly: any two existing words of the same length have the same probability of being chosen, and any two non-existing words of the same length have the same probability of being chosen. $(tests$ 5-7$)$
$30$ points: the initial constraints apply $(tests$ 8-10$)$

## Example

`abba.in`
`abba.out`
$10$
$a$
$b$
$aab$
$ab$
$ba$
$abc$
$aaaaabaaaabaaaaabaaaabaaaab$
$abbbbabbbbabbbbbabbbbabbbbbabbbbabbbbb$
$abbbbabbbbabbaaaaaabbbbbbbbbbbbaaababbbaabbbbb$
$aabaababaababaabaababaababaabaababaababaababaabaababaababaabaababaababaabab$
$1$ $1$
$1$ $2$
$3$ $2$
$2$ $2$
$-1$
$-1$
$9$ $14$
$10$ $488$
$-1$
$10$ $180$

## Explanation

Looking at the diagram above, we observe that the first occurrences of words $1\text{-}4$ are $(1, 1)$, $(1, 2)$, $(3, 2)$ respectively $(2, 2)$. 
It can be demonstrated that the words 'ba' and 'abc' will never appear, so the answer is $-1$.