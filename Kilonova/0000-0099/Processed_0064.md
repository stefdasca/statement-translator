Bored with philanthropy and chip production, William Poartă has found a new passion: epidemiological investigations. Thus, he thought of researching the spread of a virus from the past on humanity, composed of `N` people.

William knows the final state of each person (infected or not infected), but he does not know which of the people were initially infected and which were infected by others. Additionally, he found out from his friend Marcel Zahăr about a series of meetings (in chronological order) that took place between pairs of `2` people through which the virus spread, as follows: if one of the two comes to the meeting infected, then he will infect the other (if the latter was not already infected).

Now William asks the following questions:
1. For each person, can he be one of the **initially infected**?
2. For each person, can he be one of the **initially uninfected**?

# Input data
The first line contains an integer `C`, representing the requirement number to be solved.
The second line contains two integers `N, M`, representing the number of people and the number of meetings that take place.
The third line contains `N` numbers (ranging between `0` and `1`) **separated** by spaces, representing the final state of each person (`0` - not infected, `1` - infected).
The next `M` lines each represent a meeting (in chronological order), having `2` distinct integers (between `1` and `N`) representing the `2` people who meet.

# Output data
Print a single line containing N binary digits **not separated** by spaces, representing the answer for the respective test.

If `C = 1`, solve the first task, and the `i-th` character will be `1` if and only if there is an initial scenario in which the person `i` is **infected** that leads to the given final scenario, otherwise it will be `0`.

If `C = 2`, solve the second task, and the `i-th` character will be `1` if and only if there is an initial scenario in which the person `i` is **uninfected** that leads to the given final scenario, otherwise it will be `0`.

# Constraints and clarifications
* `1 \leq C \leq 2`
* `1 \leq N \leq 100 000`
* `0 \leq M \leq 100 000`
* It is guaranteed that for each test there is a possible initial scenario that leads to the final scenario.
* People cannot become spontaneously infected. They can only be infected at the end if they were initially infected or were infected by another person in a meeting.

## Subtask 1 (3 points)
* `C = 1`
* It is guaranteed that all people have the same final state (all are infected or all are uninfected).
## Subtask 2 (8 points)
* `C = 1, 1 \leq N \leq 18, 0 \leq M \leq 100`
## Subtask 3 (9 points)
* `C = 1, 1 \leq N \leq 100, 0 \leq M \leq 100`
* Number of people finally infected `\leq 18`
## Subtask 4 (27 points)
* `C = 1, 1 \leq N \leq 5 000, 0 \leq M \leq 5 000`
## Subtask 5 (28 points)
* `C = 1, 1 \leq N \leq 100 000, 0 \leq M \leq 100 000`
## Subtask 6 (3 points)
* `C = 2, 1 \leq N \leq 18, 0 \leq M \leq 100`
## Subtask 7 (4 points)
* `C = 2, 1 \leq N \leq 100, 0 \leq M \leq 100`
* Number of people finally infected `\leq 18`
## Subtask 8 (7 points)
* `C = 2, 1 \leq N \leq 5 000, 0 \leq M \leq 5 000`
## Subtask 9 (11 points)
* `C = 2, 1 \leq N \leq 100 000, 0 \leq M \leq 100 000`

# Examples

`stdin`

```
1
6 5
1 1 0 0 1 1
4 3
3 6
1 2
5 6
3 4
```

`stdout`

```
110010
```

`stdin`

```
2
6 5
1 1 0 0 1 1
4 3
3 6
1 2
5 6
3 4
```

`stdout`

```
111101
```

Explanations
---

Consider the following two initial scenarios: `010010`, `100010`. It can easily be seen that both scenarios lead to the final state `110011` after the meetings.

For people `1, 2` and `5` there are scenarios in which they are initially infected, and it can be demonstrated that for none of the people `3, 4` and `6` there is an initial scenario in which they are infected.

For people `1, 2, 3, 4` and `6` there are scenarios in which they are initially uninfected, and it can be demonstrated that for person `5` there is no initial scenario in which he is uninfected.