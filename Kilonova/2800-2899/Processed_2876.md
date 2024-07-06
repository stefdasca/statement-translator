The network formed by $n$ spies, numbered from $1$ to $n$, located in different places, have a convening convention. They will be called telephonically to a fixed location called base. The convening transmission convention includes the following rules:
- Except for a few, each spy knows which people need to contact him/her via phone call; to consider the convening valid and respond to it, he/she must receive the convening signal from **all** contact persons;
- The few spies who are expecting no convening know that they all need to take off **simultaneously**, at the so-called hour $0$, towards the base;
- Each person, as soon as they arrive at the base, receives the list of people they need to call, transmitting them the convening;
- The duration of a phone call is negligible;
- Only when **all** $n$ persons are present at the base can the meeting start.

# Task
Given, for each spy, the time required to travel to the base (expressed in hours) and the list of persons that need to contact him/her, write a program that determines if convening **all** persons is possible. If possible, determine:
1. The minimum number of hours until the meeting can start;
2. The minimum number of persons that need to be transported urgently so that the meeting can start at least one hour earlier; we call urgent transport a transport that shortens the required time by at least one hour;
3. The order numbers of the persons who will be transported urgently, displayed in ascending order.

# Input data
The input file `spioni.in` contains:
- The first line contains the number $n$ of spies;
- The second line contains $n$ natural numbers $t_1, t_2, \dots, t_n$, separated by a space, representing the travel duration of each spy to the base (under normal conditions), expressed in hours;
- Each of the following $n$ lines contains the number of persons $m$ that need to call the person with the number $i$ for him/her to start heading to the base, followed by the $m$ persons.

# Output data
The first line of the output file `spioni.out` contains the number $-1$ if convening is not possible, or the number of hours after which the meeting can start, otherwise.

If convening is possible, the file also contains:
- The second line contains a number $p$, representing the number of persons who, if transported urgently, can advance the meeting start time by at least one hour;
- The third line contains the order numbers of the persons who need to be transported urgently to make the meeting start earlier, separated by a space. These numbers must be displayed in ascending order.

# Constraints and clarifications
- $1 \le n \le 7\ 500$
- $\sum m \le 200\ 000$
- $2 \le t_i \le 10^9$
- The problem has been modified.
- One-third of the points are awarded for the first task and the rest for the last two tasks.

# Example
`spioni.in`
```
5
9 8 3 9 2
0
0
0
3 1 3 5
2 2 3
```
`spioni.out`
```
19
1
5
```