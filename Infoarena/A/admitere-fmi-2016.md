# Admission FMI 2016

The original version of this problem was proposed during the admission exam for the Faculty of Mathematics and Informatics, University of Bucharest. The current version is published with the permission of the exam organizers, but they are not responsible for modifications made to the problem for the purpose of adapting to automated evaluation. Solving this problem might differ substantially from the real exam experience. Specifically, the score obtained on this problem cannot be correlated with the official grading. Official information about the admission exam for the Faculty of Mathematics and Informatics, as well as official preparations for the exam, can be found here.

Ionuț has just finished high school and is taking the college admission exam. Knowing that he has prepared very well for the exam, he wishes to announce his success after the exam through a post on Facebook.

Ionuț knows $n$ users represented by numbers from $1$ to $n$, between whom there are $m$ friendship relations of the form $i \ j$, where $i$ and $j$ are users, and $n$ and $m$ are non-zero natural numbers. A user cannot be friends with themselves, and a friendship relation between two users means that each of them is friends with the other.

Since he wants his post to be as widespread as possible, Ionuț wants to find out who are the most well-connected users among his acquaintances, so he can eventually ask them to be friends. For this, Ionuț needs to find the largest subset of known users, in which each user in this subset has at least $k$ friends who are also in the subset, where $k$ is a non-zero natural number.

Help Ionuț find a solution to his problem by solving the following points:
a) Determine and display, in order from $1$ to $n$, the number of friends of each of the $n$ users, according to the given friendship relations.
b) Determine and display, using the most time-efficient solution based on the input data, the members of the largest subset of users, with the property that each user in this subset has at least $k$ friends who are also in the subset. If there is no such subset for the given $k$, the answer will be the word `NU`.

## Input data

The input file `admitere-fmi-2016.in` contains the numbers $n$, $m$ and $k$, on the same line, separated by spaces, as well as $2m$ natural numbers ranging between $1$ and $n$, on a new line, separated by spaces, representing in order the $m$ friendship relations between the $n$ users.

## Output data

The first line of the file `admitere-fmi-2016.out` contains $n$ numbers, representing the number of friends of each of the $n$ users. The next line contains space-separated numbers, representing the users in the required subset, or the string `NU` if such a subset does not exist.

## Constraints and clarifications

$1 \leq n \leq 100\000$

$1 \leq m \leq 200\000$

$1 \leq k < n$

Subsets formed by a single user with $k$ friends are not considered.

## Example

`admitere-fmi-2016.in`
```
5 5 2 1 2 5 1 3 2 4 5 1 4
```

`admitere-fmi-2016.out`
```
3 2 2 1 2
1 2 5
```

`admitere-fmi-2016.in`
```
5 5 3 1 2 5 1 3 2 4 5 1 4
```

`admitere-fmi-2016.out`
```
3 2 2 1 2
NU
```

`admitere-fmi-2016.in`
```
11 18 3 1 8 4 7 7 10 11 10 2 1 2 3 8 9 8 3 9 3 9 2 5 6 5 11 1 4 10 6 7 6 2 8 11 7 11 6 3 4 3 2 2 4 4 4 3 3 4 2 3 6 7 8 9 10 11
```

## Explanation

In the first example, we have a set consisting of $5$ acquaintances. Users $1$, $4$, and $5$ form a subset with the required property.

In the second example, we have the same friendship relations, but $1$ is the only one who has at least three other friends.

In the third example, we have the situation represented below: