Intensity

Giugudel, tired of numerous repairs to electrical panels, decided to diversify his activities and found it appropriate to go to the theater. Said and done: he got tickets, eagerly awaited the day of the performance, but when he arrived at the theater, he was unpleasantly surprised to find that the main power generator was broken, so the performance had to be postponed. Being the only one who could do something and not wanting to give up easily, he committed to the theater management to use an auxiliary power generator to restart a minimum number of light bulbs so that the stage could be seen. It is known that the theater's electrical network, consisting of $N$ light bulbs, can be encoded as a circuit defined recursively: Lights $1$ and $N$ will be directly connected to the generator. An empty circuit is also considered a circuit. If $C$ is a circuit then $A-C-B$ is a circuit, where $A$ and $B$ are light bulbs. This means that $A , C$, and $B$ are grouped in series. See the figure below for details. If $C_1 ,C_2 \dots C_x$ are circuits and $A , B$ are light bulbs, then $A-\{C_1 ,C_2 \dots C_x\}-B$ is a circuit. In this case, we say that circuits $C_1 ,C_2 \dots C_x$ are grouped in parallel. See the figure below for details. By $I$ we refer to the intensity of the electric current. In the case of circuits in series, $I$ remains constant, while in the case of circuits in parallel, $I$ will be divided by the number of parallel circuits we use. The higher the intensity of the electric current passing through any light bulb, the brighter the light bulb will shine. We consider a light bulb to be lit if there is a path from $1$ to $N$ that passes through that bulb, and all bulbs on the path are lit (the intensity of the electric current is strictly positive). If there is no such path, then the light bulb will not shine. Since the installation has many light bulbs and Giugudel has very little time available, he asks for your help to restart the network as soon as possible. Moreover, he wants each light bulb to shine as brightly as possible, meaning the minimum intensity value of the electric current passing through any lit bulb is maximized.

## Task

Given a circuit defined above, you must find the maximized minimum value of the intensity of the electric current passing through a lit bulb, knowing that at least $K$ light bulbs need to be restarted!

## Input data

The first line of the input file `intensitate.in` contains three numbers $N, K$, and $M$ representing the total number of light bulbs, the minimum number of light bulbs that need to be lit, and the number of connections between light bulbs. The next $M$ lines contain a pair $(x,y)$ indicating that light bulb $x$ is adjacent to light bulb $y$, light bulb $x$ being to the left of light bulb $y$.

## Output data

The output file `intensitate.out` will contain on a single line two natural numbers $(p,q)$, the solution being determined by the fraction $p/q$, with $p$ and $q$ being coprime.

## Constraints and clarifications

$1 \leq K \leq N \leq 100$

$1 \leq M \leq 2 * N$

For $30\%$ of tests $N \leq 30$

For $70\%$ of tests the maximum number $x$ of subcircuits placed in parallel will be $7$

It is guaranteed that $p$ and $q$ will be signed 32-bit integers

We consider the intensity of the electric current entering the light bulb $1$ from the generator to be $1$

The direction of the electric current is from left to right

The circuit in the input file will always be valid

## Example

`intensitate.in` 
```
6 4 7 
1 2 
1 3 
1 4 
2 6 
3 6 
4 5 
5 6
```
`intensitate.out` 
```
1 1
```
`intensitate.in` 
```
6 5 7 
1 2 
1 3 
1 4 
2 6 
3 6 
4 5 
5 6
```
`intensitate.out` 
```
1 2
```

## Explanation

In the first case, the electric current will follow the path $1-4-5-6$, and light bulbs $2$ and $3$ will not be lit. Consequently, $1-4-5-6$ will be connected in series, the electric current intensity not changing. In the second example, an additional light bulb is needed to be added to the previous configuration, let it be $2$. Light bulb $2$ is connected in parallel with light bulbs $(4,5)$, so the intensity of the electric current entering light bulbs $2$ and $4$ is $1/2$. We observe that if we had chosen light bulb $3$, then the minimum intensity of the electric current passing through the circuit would not have been maximized, being equal to $1/3$.