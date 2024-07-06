Ilinca has read about message encryption and now wants to communicate with her friend Miruna only through encrypted messages using her own encryption system.

Ilinca knows that each character is represented in computer memory using $8$ bits, in which the writing in base $2$ of the respective character's ASCII code is stored. To encrypt the character, Ilinca uses a square matrix having $8$ rows (numbered from $0$ to $7$ from top to bottom) and $8$ columns (numbered from $0$ to $7$ from left to right). On the first row of the matrix, Ilinca writes the $8$ bits representing the writing in base $2$ of the character's ASCII code, where the most significant bit (corresponding to $2 ^ 7$) is written at position $0$. On each of the next $7$ rows of the matrix, she writes a circular permutation to the left of the previous row. She lexicographically orders the rows of the formed matrix and defines the *crypt* of the character as being the sequence of bits represented by the last column of the matrix, traversed from top to bottom, followed by the index of the row in the matrix where, after the lexicographic order, the base $2$ representation of the character's ASCII code ended up. If there are equal rows in the matrix, after the lexicographic order, they will retain their initial relative order, so the row containing the base $2$ representation of the character's ASCII code will be the first among them.

To encrypt a message, Ilinca writes the crypts of the characters in the respective message in order.
Miruna knows Ilinca's encryption system, therefore she knows how to decrypt the received messages.

# Task

Write a program to solve the following two tasks:

1. Read a message and display the encrypted message according to Ilinca's system.
2. Read an encrypted message according to Ilinca's system and determine the decrypted message.

# Input data

The input file `cript.in` contains on the first line a natural number $c$, which can be $1$ or $2$, representing the task to be solved. The second line of the file contains a string of characters.

# Output data

The output file `cript.out` will contain a single line which will contain the encryption of the string from the input file (if $c = 1$), or the decryption of the string from the input file (if $c = 2$).

# Constraints and clarifications

* The length of the unencrypted message is non-zero and does not exceed $30 \ 000$.
* The characters from the read string have codes between $32$ and $127$.
* We say that string $s_1$ precedes in lexicographic order string $s_2$ if $\\exists \ k$ such that $s_{1_i} == s_{2_i}$, $\\forall \ i < k$ and $s_{1_k} < s_{2_k}$.
* For tests worth $50\\%$ of the score, the task is $1$.

# Example 1

`cript.in`
```
1
AB
```

`cript.out`
```
100010004101000004
```

## Explanation

The character `A` has the ASCII code $65$, represented on $8$ bits as $01000001$. The permutation matrix is on the left, and on the right is the matrix with the lexicographically ordered rows:

$01000001 \ \ \ \ \ \ \ \ 00000101$  
$10000010 \ \ \ \ \ \ \ \ 00001010$  
$00000101 \ \ \ \ \ \ \ \ 00010100$  
$00001010 \ \ \ \ \ \ \ \ 00101000$  
$00010100 \ \ \ \ \ \ \ \ 01000001$  
$00101000 \ \ \ \ \ \ \ \ 01010000$  
$01010000 \ \ \ \ \ \ \ \ 10000010$  
$10100000 \ \ \ \ \ \ \ \ 10100000$

The row representing `A` has index $4$. The crypt of the character `A` is $100010004$. The same process is done for `B`.

# Example 2

`cript.in`
```
2
101110001111000002
```

`cript.out`
```
VI
```

## Explanation

$101110001 = \text{crypt of the character}$ `V`  
$111000002 = \text{crypt of the character}$ `I`