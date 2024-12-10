The last expedition to Mars discovered an unknown organic compound. This compound is now being studied in NASA's laboratories. Researchers found that this compound consists only of hydrogen (`H`), oxygen (`I`), and carbon (`C`) atoms and has a molecular mass of $M$.

It is known that the rules for forming organic compounds on Mars are as follows:

- A carbon atom can bond with any of the atoms `C`, `H`, and `I` using any of its $4$ bonds (for instance, in the combination `H–C=C`, the first carbon atom is bonded through two bonds to another carbon atom and with one bond to a hydrogen atom).
- A hydrogen atom can only bond with a carbon atom using the single bond it has.
- An oxygen atom can only bond with carbon atoms using the two bonds it has.
- A compound is an assembly with the property that there is no atom with one or more free bonds (unconnected to another atom).

The combination `H–C=C` is not a compound because carbon atoms have free bonds.

Researchers consider studying categories of compounds, making a **distinction** between two compounds only if they differ in the number of carbon, oxygen, or hydrogen atoms.

# Task

Write a program to determine how many distinct compounds formed from carbon, hydrogen, and oxygen atoms (at least one of each) and with a molecular mass of $M$ exist.

# Input data

The input file `compus.in` contains on the first line the molecular mass of the compound.

# Output data

The output file `compus.out` contains a single line with the number of determined compounds.

# Constraints and clarifications

* $30 \leq M \leq 1 \ 000 \ 000$
* The mass of a `H` atom is $1$, the mass of a `C` atom is $5$, and the mass of an `I` atom is $3$. The molecular mass of a compound is equal to the sum of the masses of the atoms that constitute that compound.
* The order in which the bonds of an atom are "used" does not matter. Likewise, neither the order of atoms nor the internal bonds between them matter as long as they respect the stated formation rules.

# Examples

There is a single compound with a molecular mass of $10$: the one formed with one `C` atom, two `H` atoms, and one `I` atom ($5+2 \times 1+3=10$), a compound whose bonds can be represented as follows:
```
H–C=I
  |
  H
```

Three compounds can be obtained with a molecular mass of $40$: (`5C, 6H, 3I`), (`6C, 4H, 2I`), (`7C, 2H, 1I`):
\
~[compus.png]
\
The bond representation of any of the compounds is not unique. Any other combination corresponding to the same triplet is not considered a distinct compound.

`compus.in`
```
40
```

`compus.out`
```
3
```

`compus.in`
```
125
```

`compus.out`
```
28
```