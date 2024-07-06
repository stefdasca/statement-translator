```markdown
The new rules in the healthcare system require doctors not to prescribe a specific medication but to mention the active substance. The prescription consists of $n$ prescriptions, one for each prescribed active substance.

The pharmacist from whom I buy my medicines gave me a list in which for each active substance on the prescription, the medicines containing that active substance and the prices of the prescribed pills are noted in the following form:

* active substance : $medicament_1 \\ preț_1, medicament_2 \\ preț_2, \dots, medicament_k \\ preț_k$

Unfortunately, among certain medications, there are incompatibilities, and as a result, they cannot be administered simultaneously, because it would cause adverse reactions. Therefore, my pharmacist also gave me a list of incompatibilities, specifying pairs of incompatible medicines in the form:

* $medicament_1 \\ / \\ medicament_2$

When buying the prescription, I need to take one medication for each active substance prescribed by the doctor and ensure that I do not purchase incompatible medicines. Of course, I will buy the prescribed pills for the complete treatment.

# Task

Knowing the list given by the pharmacist, as well as the incompatibilities between the medications, write a program to determine:

1. how many medications are available for each active substance;
2. the minimum amount of money that you need to spend to buy the prescription.

# Input data

The input file `farma.in` contains on the first line the natural number $c$, representing the task to be solved ($1$ or $2$). The second line contains the natural number $n$, representing the number of active substances prescribed by the doctor. On the next $n$ lines, there is the list given by the pharmacist, with each line specifying an active substance followed by the medications containing that substance and their prices, in the form specified in the statement. The next line contains a natural number $m$, representing the number of pairs of medicines in the incompatibility list. On the next $m$ lines, the incompatible medicine pairs are written, one pair per line, in the form specified in the statement.

# Output data

If the task is $1$, the output file `farma.out` will contain $n$ lines, on line $i$ ($1 \leq i \leq n$) will be written the number of available medications for the active substance described on line $i+1$ in the input file. If the task is $2$, the output file `farma.out` will contain a single line where a natural number representing the minimum amount of money to be spent to buy the prescription, under the conditions described in the statement, will be written.

# Constraints and clarifications

* $0 < n < 10$
* $0 \leq m \leq 1400$
* The names of active substances and medications are strings of at most $30$ lowercase English letters. A medication can appear on the list of only one active substance.
* The prices of the pills are non-zero natural numbers strictly less than $1000$.
* For each active substance, there are at most 9 medications containing that active substance.
* In each pair from the incompatibility list, there are medications containing different active substances.
* In the list of medications corresponding to each active substance, there can be any number of spaces, but the length of any line does not exceed $700$ characters.
* There is always a solution for the test data.
* For tests worth $10\%$ of the score, the task is $1$.

# Example 1

`farma.in`
```
1
3
metformin:siofor 10,glibomet 30,bidiab 60,gliformin 10
ibuprofen:nurofen 24,advil 35, ibusinus 9
 diclofenac : diclac 28 , voltaren 50, cambia 102
0
```

`farma.out`
```
4
3
3
```

## Explanation

There are $4$ medications for the first active substance, $3$ medications for the second one, and $3$ medications for the third one as well.

# Example 2

`farma.in`
```
2
3
metformin:siofor 10,glibomet 30,bidiab 60,gliformin 10
ibuprofen:nurofen 24,advil 35, ibusinus 9
 diclofenac : diclac 28 , voltaren 50, cambia 102
5
siofor/diclac
gliformin/diclac
ibusinus/siofor
ibusinus/voltaren
bidiab/diclac
```

`farma.out`
```
67
```

## Explanation

We pay the minimum amount $67$ if we buy glibomet (price $30$), ibusinus (price $9$), diclac (price $28$). Note that any two purchased drugs are compatible.
```