Certainly! Here is the translated text:

---

Within the Commission for the 11th-12th grades, a social network has naturally emerged. Initially, there are `N` friendships among the members of the Commission. Every day, new friendships are formed according to the following rule: if member `A` is not yet friends with member `B`, but they have at least one mutual friend, then `A` and `B` will become friends the next day.

This intense socialization will, of course, give rise to many stories and anecdotes that will certainly enliven future meetings. Unfortunately, the author is indifferent to this humanistic aspect of the commission's activity and insists that the present situation is in fact just an opportunity for an algorithmic challenge. He wonders how many days it will take until any member of the commission becomes friends with any other member. Since the commission has many members this year, and the author does not have very high standards, he settles for an approximation of the result. More precisely, if the real answer is `X`, then the answers `X + 1` or `X - 1` are also considered acceptable.

# Task
Given the numbers `N` and `M`, as well as the `M` friendship relationships among the members of the commission, estimate how many days must pass until there is a friendship relationship between any two members of the commission.

# Input data
The first line of the file `amici.in` will contain the number `T`, representing the number of tests in the file, each test following the next format:

The first line contains two natural numbers `N` and `M`, with the meaning from the statement. The next `M` lines will contain two numbers `X` and `Y`, representing that `X` and `Y` are initially friends. A certain pair `X Y` may repeat within the input file.

# Output data
The file `amici.out` will display `T` lines, each containing the answer for a test in the order the tests are given.

# Constraints and clarifications
* `1 <= N <= 21000`
* `0 <= M <= 41000`
* `1 <= T <= 5`
* It is guaranteed that the answer is finite.
* Recall that the answer is considered correct even if it differs by one unit from the true answer.

# Example:

`amici.in`  

```
2
3 2
1 2
1 3
5 4
3 1
1 2
2 4
2 5
```

`amici.out`

```
1
2
```

Explanations
---

In the first case, members `2` and `3` become friends after one day, having member `1` as a mutual friend. Thus, all possible relationships appeared after a single day. In the second case, the following relationships appeared on the first day: `(1, 5), (3, 2), (1, 4), (4, 5)`. On the second day, the relationships `(3, 5)` and `(3, 4)` also appear, making the network complete.

---

Please let me know if you need any more assistance!