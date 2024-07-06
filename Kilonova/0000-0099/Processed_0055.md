The latest expedition to Mars has discovered an unknown organic compound. This compound is now being studied in NASA laboratories. Researchers have discovered that this compound is composed only of hydrogen (`H`), oxygen (`I`), and carbon (`C`) atoms and has a molecular mass of $M$.

It is known that the rules for forming organic compounds on Mars are as follows:

- A carbon atom can bond with any of the `C`, `H`, and `I` atoms with any of its $4$ bonds (thus, in the combination `H–C=C`, the first carbon atom bonds with another carbon atom through two bonds and with a hydrogen atom through one bond)
- A hydrogen atom can bond only with a carbon atom with its single bond
- An oxygen atom can bond only with carbon atoms with its two bonds
- A compound is a structure with the property that there is no atom with one or more free bonds (not bonded to another atom).

The combination `H–C=C` is not a compound because the carbon atoms still have free bonds.

Researchers are studying categories of compounds by making distinctions only if they differ in the number of carbon, oxygen, or hydrogen atoms.

# Task

Write a program that determines how many distinct compounds are formed from carbon, hydrogen, and oxygen atoms (at least one of each) and that have a molecular mass $M$.

# Input data

The input file `compus.in` contains the molecular mass of the compound on the first line.

# Output data

The output file `compus.out` contains a single line that contains the number of determined compounds.

# Constraints and clarifications

* $30 \leq M \leq 1 \ 000 \ 000$
* The mass of a `H` atom is $1$, the mass of a `C` atom is $5$, and the mass of a `I` atom is $3$. The molecular mass of a compound is equal to the sum of the masses of the atoms that constitute that compound.
* The order in which the bonds of an atom are “used” does not matter. Similarly, neither the order of the atoms nor their internal bonds matter as long as they comply with the stated formation rules.

# Examples

There is only one compound with a molecular mass of $10$: the compound formed with one `C` atom, two `H` atoms, and one `I` atom ($5+2 \times 1+3=10$), whose bonds can be represented as:
 ```
 H–C=I
   |
   H
```

There are $3$ compounds with a molecular mass of $40$: (`5C, 6H, 3I`), (`6C, 4H, 2I`), (`7C, 2H, 1I`):
~[compounds.png]
Representation with bonds for any of the compounds is not unique. Any other combination corresponding to the same triplet is not considered a distinct compound.

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