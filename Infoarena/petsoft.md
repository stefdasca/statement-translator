# PetSoft

Petrica owns a software company named PETSOFT which is a leader in the field. The secret of success lies in the internal organization of this company. Each employee is assigned a distinct number from $1$ to $N$ and it is known for each employee who their direct boss is (employee number $1$ is Petrica himself and has no boss). More precisely, the relationships between the company's employees form a tree rooted at node $1$. The company is invited to an international software fair where it will present its offer. At the conference, a number of teams (set by Petrica) of two employees each will be presented on behalf of the company. Petrica is not interested in the number of teams but in their value. For this, he establishes the following rule: employees $x$ and $y$ can be sent to the conference together if $x$ is the direct boss of $y$ or if $x$ and $y$ have the same boss and the value of the team formed by the two is $|x - y|$. It is also known that Petrica (employee number $1$) will not be included in any team, as he is the manager of the company. The total value of the teams will be the sum of the values of all the teams.

## Task

A programmer capable of determining the formation of teams in such a way that the total value of the teams is maximized is sought. Once found, he will be hired directly into a top position in the company's hierarchy. You could be that programmer, but you need to prove you are the right choice by developing a program that can calculate the maximum total value of the teams that the company will send to the conference.

## Input data

The first line in the input file `petsoft.in` contains an integer $N$ representing the number of employees of the company.
The next $N-1$ lines contain information about the company's hierarchy: on line $i$ it contains the boss of the employee numbered $i$.

## Output data

The first line of the output file `petsoft.out` will contain an integer representing the maximum total value of the teams that will be sent to the conference.

## Constraints and clarifications

$1 \leq N \leq 1000$

Each employee can be included in at most one team.

## Example

`petsoft.in`

```
5
1
4
2
4
4
```

`petsoft.out`

```
4
```

## Explanation

Teams will be formed as $2-4$ and $3-5$.