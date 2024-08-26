## Por Costel and the Censorship Committee

Por Costel is ready to update his Facebook status. But what happens? It seems that the evil Mark Suckerberg is not keeping his word regarding free speech on his social media platform. He has gathered a censorship committee to censor Por Costel's message. Suckerberg does not want to see words like "cocean," "porci," "pateu," etc. The committee will choose certain letters from the message and replace them with $*$. After applying this multiple times, the message should not contain any occurrence of any word from Suckerberg's list as a subarray. You are part of the censorship committee, but secretly, you are fans of Por Costel. You know that each letter in the message has a certain importance (at position $i$ in the message, the letter $m_i$ has an importance $w_i$). You do not want Por Costel's message to lose its meaning and chance to touch hearts, but you also do not want to lose your job at Facebook. Censor the message such that the sum of the importance values of the censored letters is minimized.

## Input data

The first line of the input file `cenzura.in` contains $t$, the number of tests. Each of the $t$ tests has the following format:
The first line will contain a number $n$, the length of the message.
The second line will contain a string of characters, Por Costel's message.
The third line will contain a sequence of $n$ numbers separated by spaces, the $i$-th of these representing the importance value of the $i$-th letter in the message.
The fourth line will contain a number $k$, the number of words in Suckerberg's list.
The following $k$ lines will contain the $k$ words.

## Output data

In the output file `cenzura.out`, there will be printed $t$ lines. Each of them will contain a single number, the minimum value of the importance grades of the letters that can be replaced with $'*'$ to achieve correct censorship of the message.

## Constraints

$1 \leq t \leq 10$

$1 \leq n \leq 1000$

$0 \leq w_i \leq 10^4$

$1 \leq k \leq 100$

$1 \leq$ length of a word from the list $\leq n$

the total number of occurrences of words in Por Costel's message will not exceed $10^5$.
Por Costel's message and the words from Suckerberg's list are composed of lowercase English letters $('a'-'z')$

## Example

`cenzura.in`

```
1
23
cresteporciisefacepateu
1 2 3 4 5 6 7 8 9 8 9 9 2 3 2 1 4 7 8 6 5 6 7
3
porci
rcii
pateu
```

`cenzura.out`

```
13
```

## Explanation

The optimal censorship of the word is `crestepor*iisefacepa*eu` with a cost of $8 + 5 = 13$