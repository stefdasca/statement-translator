> "You solve the problem, you don't solve the problem, you still eat the shawarma afterward"

We know two things about the festive dinner: the fact that shawarma will be served and the seating arrangement of the guests. There will be $N$ people numbered from $1$ to $N$ and a room with a round table that has exactly $N$ seats, each person has a distinct reserved seat that is not yet revealed.

To discover the reserved seat of each person, $Q$ meetings of the $N$ guests can be organized in the dining room. Before each meeting, you can establish the order in which the people will come to it. At the end of each meeting, you are given the list of guests who arrived at the meeting before both of their neighbors in the secret seating arrangement at the table.

# Task
Determine the reserved seats for each guest based on the information obtained from the $Q$ meetings.

# Implementation details

You need to implement the following function:

```cpp
std::vector<int> find_places(int N);
```

This function must return the answer, which represents the seating arrangement of the guests at the table. Any solution in which each of the guests has the same neighbors as in the arrangement chosen by the committee will be considered correct. **The array returned by the function is zero-indexed**.

You can use the following function in the implementation of your solution:

```cpp
std::vector<int> query(std::vector<int> order);
```

This function will return for the established meeting (given by the order in which the $N$ people arrive at the meeting) an array containing the numbers of the people who arrived at the meeting before both of their neighbors in the secret seating arrangement at the table.

This function receives as a parameter the indices of the people in the order in which they sit at the table during a meeting. This function will return the array of numbers of the people who arrived at the meeting before both of their neighbors in the secret seating arrangement at the table. **The array given as a parameter must be a permutation of numbers from $1$ to $N$ and must be zero-indexed**.

Don't forget to include the header `gurgerbrill.h`!

# Constraints and clarifications

**The interactor is not adaptive. The permutation does not change regardless of the meetings established by the contestant**.

| # | Points | $N$ | $Q_{\text{min}}$ | $Q_{\text{max}}$ |
| - | - | - | - | - |
| 1 | 3 | $3$ | $100$ | $100$ |
| 2 | 4 | $4$ | $100$ | $100$ |
| 3 | 5 | $50$ | $1\ 250$ | $2\ 500$ |
| 4 | 13 | $1\ 000$ | $2\ 000$ | $3\ 000$ |
| 5 | 15 | $2\ 000$ | $100$ | $200$ |
| 6 | 60 | $100\ 000$ | $60$ | $100$ |

## Scoring formula

Let $Q_{\text{conc}}$ be the number of queries made by the contestant. Let $P$ be the score associated with the test group.

* If $Q_{\text{conc}} \leq Q_{\text{min}}$, then $P$ points are awarded per test.
* If $Q_{\text{conc}} > Q_{\text{max}}$ then 0 points are awarded per test.
* Otherwise, the contestant's score is $ \displaystyle \frac{P}{3} \left( 1 + 2 \frac{Q_{\text{max}} - Q_{\text{conc}}}{Q_{\text{max}} - Q_{\text{min}}} \right)$

# Example 

The function `find_places` is called with $N = 7$:
Contestant: `query({6, 1, 5, 7, 4, 3, 2})`
Grader: `{2, 6, 5}`
Contestant: `query({1, 5, 7, 4, 3, 2, 6})`
Grader: `{2, 1, 5}`
Contestant: `query({5, 7, 4, 3, 2, 6, 1})`
Grader: `{2, 5, 4}`
Contestant: `query({7, 4, 3, 2, 6, 1, 5})`
Grader: `{3, 7, 4, 3}`
Contestant: `query({4, 3, 2, 6, 1, 5, 7})`
Grader: `{2, 4, 3}`
Contestant: `query({3, 2, 6, 1, 5, 7, 4})`
Grader: `{2, 3, 2}`
Contestant: `query({2, 6, 1, 5, 7, 4, 3})`
Grader: `{3, 2, 6, 5}`
`find_places` returns `{1, 6, 3, 5, 7, 2, 4}`