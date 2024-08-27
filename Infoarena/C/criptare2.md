# Encryption2

Alice wants to send encrypted words to Bob. For each word out of the $N $ words, Alice has a key with which she encrypts each message. A key consists of a bijective function. Let $W$ be a word from the set of words owned by Alice. We denote by $f(W)$ the encryption of the word $W$ with the key $C $, and the set $F = \{ f(W_1), f(W_2), \dots, f(W_N) \}$. Informally, a key determines how characters in a word are substituted. Unfortunately, Tractorel manages to intercept the $N $ messages that Alice tries to send to Bob, and Bob receives $M $ words from Tractorel instead. Bob asks for your help to detect for each word out of the $M $ received from Tractorel whether it belongs to the set $F$ defined earlier. You have the opportunity to respond with $1 $ if affirmed, $0 $ if negative.

## Input data

The input file `criptare2.in` contains 4 lines. The first line contains a natural number $N$, the next line contains the $N $ words that Alice will encrypt, separated by a space. The 3rd line contains a natural number $M$ and the 4th line contains the $M $ words that Bob received from Tractorel.

## Output data

The output file `criptare2.out` will contain $M $ integers, one on each line. On the $i $th line, there will be a single number from the set $\{0,1\}$ representing the answer for word $i $ sent by Tractorel from the $M $ words.

## Constraints

$1 \leq N \leq 20000$

$1 \leq M \leq 20000$

For obscure reasons, the length of a word does not exceed 26

## Example

`criptare2.in`
```
5
en abcbz un oifalzeil zbqbikepe
10
ne vedem dar nu prea pe infoarena dimineata tractorel valoare
```

`criptare2.out`
```
1
1
0
1
0
1
1
1
0
0
```

## Explanation

"ne" can be encrypted as "en" or "un". "vedem" as "abcbz". "nu" $\rightarrow$ {"en", "un"}, "pe" $\rightarrow$ {"en", "un"}, "infoarena" $\rightarrow$ {oifalzeil}, "dimineata" $\rightarrow$ "zbqbikep".