In a recently discovered archaeological document, there is a reference to a great treasure. Since the document can be interpreted in multiple ways, $n$ archaeologists are called upon to independently study the document.

Upon completing their study, each archaeologist creates a map marking a **closed** and **convex** polygonal area where the treasure is presumed to be located.

Due to limited funds allocated for the treasure discovery, it is decided to begin field research only in the map area that is specified by all archaeologists.

# Task
Given the value $n$ and the coordinates of the vertices of the areas determined by the archaeologists, determine the area of the map specified by all archaeologists (the intersection of the $n$ areas).

# Input data
The input file `tezaur.in` contains on the first line the number $n$.

For each archaeologist $i$ from $1$ to $n$, the line $2i$ contains $m_i$, the number of vertices for archaeologist $i$'s area. On line $2i + 1$ contain $2m_i$ numbers representing the coordinates of the vertices of archaeologist $i$'s area, in the form $x_{i,1}\\ y_{i,1}\\ \\dots\\ x_{i,m_i}\\ y_{i,m_i}$. **These are given in a counterclockwise direction, and it is not necessary for any 3 points to be non-collinear.**
                  
# Output data
On the first line of the output file `tezaur.out`, write the area of the map specified by all archaeologists. If there is no common area to the zones of the $n$ archaeologists, write the number $0$ in the output file.

# Constraints and clarifications
- $1 \\le n \\le 30$
- $3 \\le m_i \\le 20$, $i \\in \\{1,2,\\dots,n\\}$
- The coordinates of the vertices are integers in the interval $[-1\\ 000,1\\ 000]$.
- The maximum acceptable difference between the displayed answer and the commission's answer is $10^{-2}$.

# Example
`tezaur.in`
```
3
4
-20 30 -20 -20 40 -20 40 30
5
10 80 10 -30 60 -50 100 60 70 80
4
20 10 70 10 70 60 20 60
```
`tezaur.out`
```
400.00
```

## Explanation
~[ex.png|width=30em]