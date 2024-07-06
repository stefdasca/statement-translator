In the course of the operation "Storm in the Desert" due to a sandstorm, $n$ soldiers got separated from their platoons. After the storm passed, the problem arises of regrouping them into platoons. For this purpose, identification tags worn by the soldiers around their neck are used. These tags have numbers that can identify each soldier and the platoon they belong to. Thus, soldiers from the same platoon have identification numbers made up of the same digits, arranged in different orders, and the identification numbers are unique. For example, the identification numbers $78003433$, $83043073$, $33347008$ indicate that the three soldiers who wear them belong to the same platoon.

# Task
Given the $n$ numbers from the identification tags, regroup the $n$ soldiers into platoons, indicating the number of platoons found (a reconstituted platoon must have at least one soldier), the number of soldiers in the most numerous platoon, the number of platoons that have this maximum number of soldiers, as well as the composition of such a platoon (with the maximum number of regrouped soldiers).

# Input data
The input file `pluton.in` contains on the first line the number $n$ of recovered soldiers, and on each of the following $n$ lines one identification number of the $n$ soldiers.

# Output data
The output file `pluton.out` will contain on the first line the number of reconstituted platoons.
The second line will contain the number of soldiers in the most numerous reconstituted platoon.
The third line will contain the number of platoons that have the maximum number of recovered soldiers.
The fourth line will contain the composition of such a platoon, with the maximum number of recovered soldiers, with the identification numbers of the soldiers in the composition written one after the other separated by a space.

# Constraints and clarifications
- $0 < n \leq 4\ 000$
- $0 <$ identification number $< 2\ 000\ 000\ 000$
- Since the fourth line contains the identification numbers of the soldiers **of one** of the platoons with the maximum number of soldiers, there can be multiple correct solutions. Any of them can be chosen.
- Partial scores are awarded as follows: for the correct value on the first line $30\%$ of the score is awarded; for the correct values on the first and second lines, $50\%$ of the score is awarded, for the correct values on the first, second, and third lines, $70\%$ of the score is awarded, and for the correct solution of all the requirements, the full score for the test is awarded.

# Example
`pluton.in`
```
10
1223
123
666
321
7890
2213
312
655
1000
1322
```
`pluton.out`
```
6
3
2
321 312 123
```
## Explanation
Soldiers from $6$ distinct platoons have been recovered, the highest number of soldiers recovered from a platoon being $3$. There are $2$ platoons with the maximum number of recovered soldiers ($3$), one of them being formed by the soldiers with the numbers $321$, $312$, $123$. It is noteworthy that the solution $1223$, $2213$, $1322$ is also correct.