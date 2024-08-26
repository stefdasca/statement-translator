## Task

At the ABC Faculty, there are two alternatives for students to have time to assimilate knowledge: increasing the day to $30$ hours or reducing the study of certain subjects. Since the first option is not convenient at all, Farfurel, our student, opts for option $2$, for which the Student League introduces a program platform that:
1. Determines which subjects are necessary to be able to study a new subject. For example, to study the course "Management" it is necessary to take the course "Economic Theory" and the course "Marketing", just to give an example closely related to the profile of the ABC Faculty.
2. Determines which subjects are truly useful among all the subjects studied at the faculty. For example, the course of $\dots$ (we do not give names, but it can be filled in randomly with a good chance of giving the correct answer) is not useful for anything at all.
3. Requests to remove from the curriculum the subjects that are neither useful nor serve (directly or indirectly) to learn useful subjects. See the example.
4. Requests to indicate which subjects cannot be taught in any order. For example, the course "Mechanics" heavily relies on the course "Differential Equations", but the course "Differential Equations" takes its examples from "Mechanics". Vicious circle, hence the subjects cannot be taught in any order without "cramming" knowledge.

## Input data

The first line of the input file contains three natural numbers: $N$, $M$, $P$, the number of subjects (each subject is assigned a number from the interval $[1, N]$), the number of links between subjects, and the useful subjects in the faculty. 
The next $M$ lines contain a pair $X\ Y$, indicating that subject $X$ is necessary for learning subject $Y$. 
The last line contains $P$ numbers, representing the codes of useful subjects.

## Output data

The first line of the output file contains the numbers of the completely useless subjects in ascending order (see definition at point $3$); if there are no such subjects, print $0$. 
The second line will contain in ascending order the subjects that cannot be taught due to cyclic dependencies; if there are no such subjects, print $0$.

## Constraints and clarifications

$1 \leq P \leq N \leq 300$ 

## Example

`examene.in`
```
8 6 1
1 3
5 4
6 7
3 6
7 8
6 3
7
```

`examene.out`
```
2 4 5 8
3 6
```