Vampire

Daniel, adventurous by nature, went on a trip to the land of vampires. Unfortunately, he fell prey to a vampire and is now captive in its castle. The map of the vampire land can be represented in an orthogonal axis system, and the castle where Daniel is currently held is placed at the origin. It is known that in the land of vampires there is only one sunlit area that is safe for humans. This area is represented by the outline of a square whose diagonals lie on the coordinate axes. It is known that the length of the square's diagonal is $L$. After persistent negotiations, Daniel managed to convince the vampire to release him. Unfortunately, our vampire is passionate about mathematics, especially Euler's beta function. For two natural numbers $x$ and $y$. Hence, the vampire provides Daniel with a teleportation device that, for a fixed number $K$, can transport the user from a point $(x_1, y_1)$ to another point $(x_2, y_2)$, provided that $x_2 = x_1 + K$ and $y_2 = y_1 + K$. For each teleportation, Daniel will have to pay the vampire a certain cost. The cost of a teleportation from $(x_1, y_1)$ to $(x_2, y_2)$ is $\frac{1}{\beta(x+1, y+1)}$. Since Daniel hates the beta function, he will choose the teleportation with the minimum cost at each step. Daniel can use multiple teleportations to reach the safe area, but he will always use the same number $K$. Before leaving, Daniel wonders:
1) What are the even values of $K$ he can choose to reach the safe area using the teleportation device?
2) What is the minimum cost he will pay the vampire to reach the safe area if he optimally chooses the even number $K$?

## Input data

The input file `vampir.in` contains on the first line two natural numbers $C$ and $L$. $C$ can have the value $1$ or $2$, depending on the question you need to answer, and $L$ has the above-mentioned significance.

## Output data

If there is no even value $K$ that Daniel can choose to reach the safe area using the teleportation device, then the output file `vampir.out` will contain on the first line the number $-1$, regardless of the value of $C$. Otherwise:
If $C$ is $1$ the output file `vampir.out` will contain on the first line the number of even values $K$ that Daniel can choose to reach the safe area using the teleportation device. On the second line, the file will contain in ascending order the even values of $K$ with the above property.
If $C$ is $2$ the output file `vampir.out` will contain on the first line a single number, representing the minimum cost that Daniel will pay the vampire to reach the safe area. It is guaranteed that this number can be written as an irreducible fraction of the form $\frac{P}{Q}$. You are required to display the value $P * Q^{-1}$ modulo $1000000007$, where $Q^{-1}$ represents the modular inverse of $Q$ with respect to $1000000007$.

## Constraints

$L$ is an even number

$2 \leq L \leq 10^7$

For tests worth $50$ points $C = 1$

For other tests worth $50$ points $C = 2$

The result for the second task must be displayed modulo $1000000007$.

## Example

`vampir.in`
```
1 8
```
`vampir.out`
```
2
2 4
```
`vampir.in`
```
2 8
```
`vampir.out`
```
166666668
```
In the first example, 2 and 4 are the only $K$ values with which one can reach the safe area; with $K = 2$ a possible path is: $(0,0) \rightarrow (1,1) \rightarrow (2,2)$.
In the second example, a possible minimum cost path is with $K = 4$ and the path $(0,0) \rightarrow (-2, -2)$, which has the cost $\frac{1}{6}$, so it will display $1*6^{-1}$ modulo $1000000007$.
In the drawing below, the first example is illustrated. The sunlit area is drawn in red, and the path taken by Daniel is drawn in green.