Neo, the hero from the movie Matrix, needs energy to defeat his adversaries. He discovered a zone in the matrix comprising consecutive locations numbered from $1$ to $N$, each generating a certain amount of energy, either positive or negative, known beforehand. Neo can enter this zone through a single location and can exit the zone only once. Once he has entered the energy zone, he must traverse the locations in increasing order of their numbers, and the energy accumulated in a location multiplies the energy already accumulated by Neo. Furthermore, if a location contains negative energy and Neo has accumulated positive energy up to that location, all his energy transforms into negative energy. However, if Neo encounters another location with negative energy while his energy is still negative, all his energy becomes positive. Neo's initial energy value is $1$.

# Task

Help Neo discover the location where he should enter and the location where he should exit the energy zone to accumulate the highest possible amount of positive energy.

# Input data

From the file `neo.in`, read:
- The first line contains the number of energy locations
- The second line contains a list of integers representing the amount of energy of each location, values separated by a space

# Output data

To the file `neo.out`, print:
- On the first line, the amount of energy accumulated by NEO
- On the second line, two values separated by a space: the order number of the location where NEO enters the energy zone and the order number of the location where NEO exits the energy zone. If it is not possible to obtain positive energy, both the accumulated energy and the order numbers of the locations will be $0$.

# Constraints and clarifications

* $1 \leq N \leq 100$;
* $-3 \leq$ the value of the energy in a location $\leq 3$
* $-2 \ 000 \ 000 \ 000 \leq $ the product of all energies $\leq 2 \ 000 \ 000 \ 000$
* If there are multiple solutions for the input data, only one will be displayed.

# Example 1

`neo.in`
```
4
-3 -2 2 -3 
```

`neo.out`
```
12
2 4
```

# Example 2

`neo.in`
```
1
-2
```

`neo.out`
```
0
0 0
