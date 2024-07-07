**The Occult Information Service of the National Commission (SOICN)** consists of $n$ occult agents, with distinct code numbers from $1$ to $n$ and a chief agent coded $0$. For security reasons, not any two occult agents have direct (informational!) contacts, but through the existing direct contacts, any two occult agents can communicate information. An occult service is considered *strong* if and only if it doesn't contain any agent whose removal compromises communication (and, as a result, there are agents who can no longer transmit information).

# Task
Write a program that checks if **SOICN** is *strong*. Additionally, if **SOICN** is not *strong*, the program should determine:
- the weak links of **SOICN** (all agents whose removal compromises communication);
- all groups of agents that are *strong* within **SOICN**, maximal with this property.

# Input data
The input file is named `soicn.in` and contains on the first line $n$, the number of occult agents in **SOICN** (excluding the chief), and on each of the following lines a pair of numbers $x\\ y$ where $x, y \\in \\{0,1,2,\\dots,n\\}$, separated by spaces and indicating "$x$ and $y$ have direct contact".

# Output data
The output file, named `soicn.out`, will contain the message `SOICN este forte` or:
- on the first line, the message `SOICN nu este forte`;
- on the second line, the code numbers of the agents constituting the weak links of the service, separated by spaces;
- on the third line, $m$ – the number of *strong* groups of agents within **SOICN**;
- on each of the following $m$ lines, the code numbers of the agents of each *strong* group, separated by spaces.

# Constraints and clarifications
- $1 \\le n \\le 150$

# Example 1
`soicn.in`
```
2
0 2
0 1
2 1
```
`soicn.out`
```
SOICN este forte
```
# Example 2
`soicn.in`
```
3
0 1
0 3
2 1
```
`soicn.out`
```
SOICN nu este forte
0 1
3
0 3
1 2
0 1
