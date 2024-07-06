```markdown
As any civilized country, Romania imports various products from other countries. To achieve this, $M$ transports are made, each transport starting from a city outside the country and having a city in Romania as the final destination. Each transport is carried out by a truck belonging to either the company Alfatrans or the company Betatrans.

We can assume that the cities are numbered from $1$ to $N$, the cities from $1..K$ being in Romania, and the cities from $K+1..N$ being in other countries. Between these cities, there are $N-1$ bidirectional roads such that between any $2$ cities there is exactly one route (composed of one or more roads), and every route from a city in Romania to a city in another country passes through city $1$, where the customs are located.

On the route of any transport, when passing through a city, the truck driver must pay certain taxes and sell part of the transported product, so that a profit set by the city hall of that city is obtained.

The Romanian government has established for each transport the minimum total profit that must be obtained. The total profit is obtained by summing the profits obtained in each city through which the truck passes from the starting city to the destination city (including the starting city and the destination city).

The owner of Alfatrans has numerous international relations and can manipulate the city hall of each city. Thus, he can set for each city $i$ the profit $P_i$ that must be obtained when a truck passes through that city.

To discredit the Betatrans company, the owner of Alfatrans wants to set $P_i$ for each city $i$ in such a way that any transport carried out by Alfatrans trucks brings a profit greater than or equal to the minimum profit set for that transport, and any transport carried out by Betatrans trucks brings a profit strictly less than the set profit.

# Task

For a considerable number of shares in Alfatrans and to obtain $100$ points, you must help the owner of Alfatrans set the profit imposed by the city hall for each city so that the Betatrans company is discredited.

# Input data

The first line of the input file `import.in` contains the natural numbers $N \\ M \\ K$ separated by a space, having the significance described in the statement. The next $N-1$ lines contain two natural numbers $a, b$ separated by a space, meaning that there is a bidirectional road from city $a$ to city $b$. The next $M$ lines describe the transports as follows. Each line contains $4$ numbers $a \\ b \\ c \\ d$ separated by a space with the meaning "a transport is made from city $a$ to city $b$ executed by company $x$, and the minimum profit that must be ensured for this transport is $c$". The company $x$ is Alfatrans if $d=0$ and respectively Betatrans if $d=1$. It is guaranteed that for any transport $a$ is a city outside the country, and $b$ is a city in Romania.

# Output data

The file `import.out` will contain a single line on which $n$ numbers are written separated by exactly one space. The $i$-th number on the line represents $P_i$, the profit set by the owner of Alfatrans for city $i$. If these values will cause the Betatrans company to not meet the government's requirements, and the Alfatrans company to fully meet these requirements, you will get the maximum score on the test.

# Constraints and clarifications

* $2 < N < 222$
* $1 < K < N$
* $0 < M < K \times (N-K)$
* The minimum profit that must be ensured for each transport is an integer between $-10^{9}$ and $10^{9}$
* The profits $P_i$ must be integers between $-100\ 000$ and $100\ 000$
* The existence of a solution is guaranteed.

# Example

`import.in`
```
7 4 4
1 3
3 2
3 4
1 5
1 6
6 7
6 2 10 0
6 3 5 1
7 4 7 0
5 4 -2 1
```

`import.out`
```
0 6 -6 3 0 10 0
```

## Explanation

The first transport passes through the cities $6 \ 1 \ 3$ and $2$ obtaining a profit of $10+0-6+6=10$ thus meeting the conditions in the statement.
The second transport passes through $6 \ 1 \ 3$ obtaining a profit of $10+0-6=4 < 5$ and also meets the conditions in the statement.
The third transport passes through the cities $7 \ 6 \ 1 \ 3 \ 4$, obtaining a profit of $0+10+0-6+3=7$, and the last transport passes through $5 \ 1 \ 3 \ 4$ with a profit of $0+0-6+3= -3 < -2`.

~[img1.png]
```