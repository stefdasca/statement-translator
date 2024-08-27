# The Moon

In the year $2507$, the colonization of the Moon has been completed, with each country owning several plots of territory on the planet. Companies on Earth want to build rectangular buildings on the Moon. Obviously, each company will only be able to build on the territory owned by its country of origin.

## Task

Determine for each company whether their building request can be fulfilled!

## Input data

The first line of the file `luna.in` contains two natural numbers $N$ and $M$, which represent the number of rows and columns, respectively, of the matrix that describes the map of the Moon. On each of the next $N$ lines, there are $M$ numbers indicating the country number that owns the plot at that line and column on the map. On the next line, there is the number $K$ of companies on Earth that want to build on the Moon. In the following $K$ lines, there are written triplets of numbers, representing the companies' requests. The first number in the triplet represents the country of origin of the company. The second and third numbers represent the dimensions of the building that, according to the request, the company would like to build.

## Output data

The output file `luna.out` will contain exactly $K$ lines. If the $i$-th request can be fulfilled, the $i$-th line will contain the message `Cererea poate fi satisfacuta`. If the company’s country of origin does not have plots on the Moon, the output file will contain the message `Tara de provenienta nu are parcele pe Luna!`. If it is not possible to build a building with the given dimensions using only the plots of the company’s country of origin, the output file will contain the message `Cererea nu poate fi satisfacuta!`.

## Constraints and clarifications

$1 \leq N, M \leq 50$

The country number is a natural number between $1$ and $2500$

$1 \leq K \leq 100\ 000$

The country number of a company's origin is a natural number between $1$ and $5000$

The dimensions of a building are natural numbers between $1$ and $100$

## Example

`luna.in`
```
5 10 
1 1 1 2 2 2 2 3 3 4 
1 1 1 2 2 2 2 3 3 4 
5 5 5 2 2 2 2 7 7 4 
5 5 5 6 6 6 6 7 7 4 
5 5 5 6 6 6 6 7 7 4 
6 
1 2 3 
2 3 4 
3 2 3 
1 3 2 
7 20 20 
8 4 4
```

`luna.out`
```
Cererea poate fi satisfacuta! 
Cererea poate fi satisfacuta! 
Cererea nu poate fi satisfacuta! 
Cererea poate fi satisfacuta! 
Cererea nu poate fi satisfacuta! 
Tara de provenienta nu are parcele pe Luna!
```