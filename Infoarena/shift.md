# Shift

A machine is given that can read and write characters. The machine has a tape of 26 pairs of characters (arranged one after the other). One character from a pair belongs to the set $'a'\ldots'z'$ and each character appears exactly twice on the tape. To write a text, the machine needs to read it first, so it has a read head initially positioned at position $1$ on the tape. To read a character, the machine must position its head over an element of the tape that contains the respective character. It is known that, to move the read head in one direction (left or right), the machine will consume one joule. Also, to read the first character from a pair $i$, the machine will consume $C_{i,0}$ joules and, to read the second character from a pair $i$, the machine will consume $C_{i,1}$ joules.

## Task

Given a text $S$, write the minimum time required to write it with the machine.

## Input data

The input file `shift.in` will contain on the first line the text $S$. The next $26$ lines will each contain two characters $a_{i,0}$ and $a_{i,1}$ separated by a space representing the first and respectively the second character of pair $a_i$. The following $26$ lines will contain $C_{i,0}$ and $C_{i,1}$, the number of joules needed for writing the first character from pair $i$ and respectively the number of joules needed for writing the second character from pair $i$.

## Output data

The output file `shift.out` will contain a single number, $Sol$, representing the minimum number of joules required to write the text $S$ with the help of the machine.

## Constraints

$1 \leq \text{length}(S) \leq 100\ 000$  
The string $S$ will contain only characters from the set $'a'\ldots'z'$  
$1 \leq C_{i,j} \leq 10$  

## Example

`shift.in` 
```
phqghumeay 
l n 
l f 
d x 
f i 
r c 
v s 
c x 
g g 
b w 
k n 
q d 
u w 
o z 
v s 
r t 
k j 
p e 
p y 
t m 
y q 
e i 
m z 
a a 
o b 
j u 
h h 
1 1 
1 2 
2 2 
1 1 
1 1 
2 2 
2 1 
2 1 
2 2 
2 1 
1 2 
1 2 
2 2 
1 1 
1 1 
2 1 
1 1 
2 2 
2 2 
2 2 
2 2 
1 2 
1 1 
1 1 
1 1 
1 1 
84
```

`shift.out` 
```
84
```