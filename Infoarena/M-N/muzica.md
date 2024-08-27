# Music

Vasile found out that DJ Random will mix the playlist for the Freshmen’s Ball of the Faculty of Mathematics and Computer Science at the University of Bucharest. For simplicity, we will consider that each song can be encoded (using algorithms far too intelligent for Vasile) into 32-bit integers. Vasile also has a favorite playlist, and he is curious to know how many of the songs in his playlist are also present in DJ Random's playlist. DJ Random is quite lazy, and therefore he will generate his songs as follows: he chooses the first two songs $R[1] = A$ and $R[2] = B$, and for the rest, he uses the formula $R[i] = (C * R[i - 1] + D * R[i - 2]) \mod E$.

## Input data

The input file `muzica.in` will contain on the first line $N$, the number of songs in Vasile's playlist, and $M$, the number of songs in DJ Random's playlist. The second line contains $A$, $B$, $C$, $D$, and $E$, the constants with which DJ Random constructs his playlist, and the third line contains $N$ numbers representing the songs from Vasile's playlist.

## Output data

The output file `muzica.out` will contain on the first line the number of songs from Vasile's playlist that are also in DJ Random's playlist.

## Constraints and clarifications

$3 \leq N \leq 10\ 000$  
$3 \leq M \leq 10\ 000\ 000$  
$1 \leq A, B, C, D, E \leq 1\ 000\ 000\ 000$  
Any song is associated with a 32-bit integer.  
It is guaranteed that Vasile is an original guy and does not have two identical songs in his playlist.

## Example

`muzica.in`  
3 4  
1 1 1 1 1000000000  
1 2 7  

`muzica.out`  
2  

## Explanation

The songs in Vasile's playlist are: $1$, $2$, $7$, and the songs in DJ Random's playlist are: $1$, $1$, $2$, $3$. Therefore, there are two songs that are present in both Vasile's playlist and DJ Random's playlist, namely: $1$ and $2$.