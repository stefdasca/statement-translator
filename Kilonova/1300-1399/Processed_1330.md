**CERN** is an acronym used to designate the European Organization for Nuclear Research. The acronym has been preserved from the old name in French, namely **Conseil Européen pour la Recherche Nucléaire**. It is the largest elementary particle research laboratory in the world, located in the northwestern suburbs of Geneva, right on the border between Switzerland and France. The primary function of the CERN complex is to provide elementary particle accelerators and other types of infrastructure needed for high-energy particle physics. ~[imag1.png|align=right]

The CERN particle accelerator is in the form of $3$ circles with the same radius, tangent externally pairwise, numbered $1$, $2$, $3$ on the figure. The trajectory of an elementary particle starts from one of the points marked on the figure with $A, B, C, D, E, F$ and moves with a constant speed of ${1^\circ}$/time unit only on the circumferences of the circles. When passing through a tangent point between two circles, the particle changes both the direction of movement and the circle it moves on. Thus, if the direction of movement was at some point counterclockwise, when passing through a tangent point it becomes clockwise and if the direction of movement was clockwise, when passing through a tangent point it becomes counterclockwise.
~[imag2.png|align=right]

# Task

Knowing that the circles forming the accelerator are marked degree by degree starting from ${0^\circ}$, counterclockwise (as indicated in the adjacent figure), write a program that, knowing the initial point and the direction of movement of a particle, determines the position of the particle in the accelerator after a given number of time units.

## Input data

The first line of the input file `cern.in` contains a character $p$ indicating the starting point of the particle.
The second line of the input file contains two integers $s$ and $t$, separated by a space, indicating the direction of movement ($1$ for counterclockwise and $-1$ for clockwise) and the number of time units the movement lasts.

## Output data

The first line of the output file `cern.out` will contain two natural numbers $g$ and $c$, separated by a space, representing the number of degrees, counterclockwise, and the circle corresponding to the final position where the particle will be found after $t$ time units.

## Constraints and clarifications

* $p$ ∈ \\{'$A$', '$B$', '$C$', '$D$', '$E$', '$F$'\\}
* $s$ ∈ \\{$-1$, $1$\\}
* $0 \leq t \leq 1\ 000\ 000\ 000$
* $0 \leq g \leq 359$
* $c$ ∈ \\{$1$, $2$, $3$\\}
* For all input data sets, the final position of the particle does not coincide with one of the tangent points between the circles.

## Example

`cern.in`
```
A
1 320
```

`cern.out`
```
200 3
```

## Explanation

The particle starts from point $A$ moving counterclockwise and has the following path:
* $180^\circ$ on circle $1$ counterclockwise
* $60^\circ$  on circle $2$ clockwise
* $80^\circ$  on circle $3$  counterclockwise
The final position is at $200^\circ$ on circle $3$