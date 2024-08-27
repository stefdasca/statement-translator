## Mcript

On the planet Mars, information transfer in the Martian army was done unencrypted. The cyber attack from Earth prompted them to implement an information encryption system. The Martian alphabet is numeric and contains $N$ symbols, digits from $1$ to $N$. In the Martian dictionary, there are $M$ distinct words. The Martians created the encryption code as a sequence $c_1, c_2, \dots, c_N$ of distinct symbols from the alphabet with the meaning: the symbol $c_1$ is encoded by $1$, the symbol $c_2$ is encoded by $2$, and so on. A word is encrypted by replacing the symbols from which it is formed with the corresponding symbols of the encryption code. For example, for $3$ symbols and the encryption code $312$, the word $133211$ will be encrypted as $211322$. Earthlings intercepted a message consisting of $K$ lines, each line containing a certain number of encrypted words. In the cyber war between Earth and Mars, the Earthlings found out the encryption code and the dictionary.

## Task

You have been designated the smartest computer scientist on Earth and you need to implement an algorithm to verify if the sentences that make up the message are valid or have been tampered with on the way from Mars to Earth. A sentence is valid if all the words that compose it appear, after decryption, in the Martian dictionary.

## Input data

The text file `mcript.in` contains:
* The first line contains the number $N$ of symbols in the Martian alphabet.
* The second line contains the string of digits (without separating spaces) representing their encoding.
* The third line contains the number $M$ of words in the dictionary, followed by those $M$ words, separated by a space.
* The next line contains the number $K$ of sentences of the intercepted encrypted message and then, on $K$ successive lines, the number of words in the current sentence, followed by the words that form it, separated by a space.

## Output data

The text file `mcript.out` will contain $K$ binary numbers, one per line, corresponding to the $K$ sentences from the encrypted message as follows: $1$ for a valid sentence and $0$ otherwise.

## Constraints and clarifications

$1 \leq N \leq 9$

$1 \leq M \leq 1\ 000\ 000$

A Martian word is formed from at most $9$ symbols, not necessarily distinct.

The words in the message use only symbols from the Martian alphabet.

The total number of words in the message will not exceed $800\ 000$.

A sentence has at least one word.

## Example

`mcript.in`

```
3 
132 
4 
213 32 31 12 
3 
3 312 23 21 
4 13 312 13 213 
1 13 
```

`mcript.out`

```
1 
0 
1 
```

## Explanation

$1$ $(312 \rightarrow 213, 23 \rightarrow 32, 21 \rightarrow 31)$

$0$ $(213 \rightarrow 312, 312$ - non-existent word in the dictionary$)$

$1$ $(13 \rightarrow 12)$