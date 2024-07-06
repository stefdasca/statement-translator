In the headquarters of a company, entry is allowed only with the help of magnetic cards. Whenever access codes are changed, the cards need to be formatted. Formatting involves printing a pattern by magnetization. The device in which the cards are inserted, called a card reader, checks this pattern. All cards are of the same dimensions, square surface and negligible thickness. Each of the two flat faces of a card is divided into $N \times N$ identical square cells. Through formatting, some cells, marked in black in the example, are magnetized allowing infrared radiation to pass from one side to the other of the card. Inside the card reader, one side of the card is uniformly illuminated. On the other side, the light beams passing through the card are electronically analyzed. To allow access to the building, the pattern printed on the card must exactly match the pattern of the template that stores the entry code. Multiple cards cannot be inserted simultaneously through the slot of the device. The card can be inserted into the slot with any of its edges towards the slot opening and with either of the two faces oriented towards the template. After insertion, the card is placed in a plane parallel to the template, pressed against it, so that the four corners of the card exactly overlap with the corners of the template. The patterns printed on the two faces of a card are identical. A magnetized cell corresponds to a magnetized cell on the opposite side, and a non-magnetized cell corresponds to a non-magnetized cell. A magnetized cell is transparent to infrared radiation regardless of which face is illuminated.

An employee of the company has several cards. On some of these, the new entry code has been printed, while others have older codes. To find out which cards allow access to the company's headquarters, the employee must check them all, inserting them one by one, in all ways deemed necessary, into the slot of the card reader.
~[0.png|align=center|width=45em]

# Task
Write a program that determines which of the cards allows access to the company's headquarters.

# Input data
The input file `cartele.in` contains on the first line two natural numbers $N$ and $C$ separated by a space. $N$ is the dimension of the arrays representing the template pattern and the card patterns. $C$ represents the number of cards. There follow $C+1$ blocks of $N$ lines each. The first block of $N$ lines encodes the template. The next $C$ blocks of $N$ lines each encode one card. Each line contains $N$ integer values, separated by a single space. Magnetized cells correspond to the value $1$, and the others, the value $0$.

# Output data
In the output file `cartele.out` will be written $C$ lines, one value per line. On line $i$, the value $1$ will be written if card $i$ allows access to the building and the value $0$ in case it does not.

# Constraints and clarifications
- $1 < N, C \leq 50$

# Example
`cartele.in`
```
3 2
0 1 0
0 0 1
1 0 0
1 0 0
0 0 1
0 1 0
0 0 1
0 0 1
0 1 0
```
`cartele.out`
```
1
0
```

## Explanation
The input data corresponds to the situation in the figure. Card $1$ matches the template perfectly if rotated counterclockwise by $90 \degree$. Card $2$ does not match the template, regardless of how it is inserted into the slot.