# The Path to Success. All Roads Lead to Rome

One evening, Raul had an unusual idea: to organize a CS2 LAN party with his friends.

As we know that "All roads lead to Rome," we can say that each city in Europe forms a tree, with Rome being the root of the tree. Each of Raul's $F$ friends is located in a different city in Europe. To save money, each friend will travel for free using the *Pick Me Up* method.

However, there's a problem. Every time a friend arrives in a new city, they get hungry. Since the *driver* does not enter the city, they drop the friend at the city entrance, and the friend must take a taxi to reach a restaurant. After eating, they will take another taxi to leave the city. If two or more friends meet at the entrance of a city, they can share the same taxi and eat from the same dish at the restaurant. Unfortunately, it is not allowed to sneak out food from the restaurant for the road :(((((.

For each city, the cost of a taxi and the restaurant meal is known. A friend can choose to wait outside the city to meet other friends passing through the same city or to ride alone in a taxi and dine alone.

~[LAN party.jpg|align=center|width=45%]

# Task

Unfortunately, not all friends can come to this LAN party, so you are given $Q$ scenarios. For each scenario, you need to find the minimum cost that friends from the range $[l, r]$ will spend to meet.

# Input data

The first line contains three numbers: $N, Q$, and $F$. $N$ is the number of cities in Europe, $Q$ is the number of queries, and $F$ is the number of friends.  
The second line contains specific costs for these $N$ cities, from $1$ to $N$.  
The third line contains the array $t$, ($t_i$, $i=\\overline{2,N}$), representing the city that can be directly reached from city $i$ and vice versa.  
The fourth line contains the cities where Raul's $F$ friends are located.  
The next $Q$ lines contain two numbers, $l$ and $r$, representing the range of friends who will meet Raul.

# Output data

On $Q$ lines, print the minimum cost incurred by Raul's friends to meet. Since the cost can be very large, it needs to be displayed modulo $10^9+7$.

# Constraints and clarifications

* $1 \leq Q \leq 1 \ 000 \ 000$
* $1 \leq N, F \leq 400 \ 000$
* The number of friends in the $Q$ scenarios $\leq 1 \ 000 \ 000$ 
* Specific cost for each city $\leq 2^{63}-1$
* The LAN party can be organized in any city, provided the friends' expenses are minimized.
* If in the same restaurant, two or more friends arrive at the same time, they will eat from only one dish. The quantity is infinite.
* Raul can reach any city for free.

# Example 1

`stdin`
```
12 6 6
1 1 1 1 1 1 1 1 1 1 1 1
1 1 2 2 2 3 5 5 6 9 9
4 8 9 10 12 7
1 2
1 3
1 4
3 4
1 6
4 5
```

`stdout`
```
4
5
7
5
11
6
```

## Explanation

Trust me, the answers are correct.