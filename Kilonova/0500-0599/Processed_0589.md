
RAU-Gigel is playing with his new train set, which he received as a birthday gift this year. The set contains $N$ distinct stations, numbered consecutively for simplicity from $1$ to $N$, and $N-1$ pieces of track that can connect any two given distinct stations (the connection is bidirectional) such that by using these tracks **there exists a unique path consisting of tracks between any two distinct stations**. Like any toy, each of the $N-1$ pieces of track has an associated danger level, a value expressed by a positive natural number (nobody is perfect after all, not even toys), to know from what age they would be safe for children to use, for example. Also, all pieces of track have the same constant length of one unit.

RAU-Gigel plays with his train set over the course of $Q$ days, and every day he is supervised by a family member to ensure his safety. Unfortunately for him, on each of the $Q$ days, the person supervising him complicates his plans a bit, allowing him to use only the tracks with a danger level of **at most $M$ (including $M$)**, a positive natural value chosen by the supervisor (it should be noted that all stations may always be used). Hence, by using **all the tracks at his disposal** to connect the corresponding stations, he will obtain one or more maximal connected layouts of stations (**there exists a unique path consisting of tracks between any two distinct stations in a layout**) which he will call **towns**. On each such day, our main character receives from the supervisor a positive natural number $K$ pieces of track considered perfectly safe for the child's play, which he can use to connect **any two** distinct stations he wants. Also, the tracks he receives are taken back at the end of the day (perhaps the supervisor needs to supervise other children on the following days and will need them).

RAU-Gigel considers that a chain is a sequence of **one or more distinct stations** such that any two **adjacent** stations in it are connected by **exactly one** track, and the chain of maximum length is the one formed by the maximum number of pieces of track (thus, the length of a chain is given by the number of pieces of track from which it is made up). His goal each day is to form **a single** chain as long as possible with the tracks received from the supervisor and at most one chain from each town he has created, at his choice (meaning that for each town he can choose exactly one chain from it (any he wants) or not use any chain from that town).

# Task

RAU-Gigel already knows all the details of $T$ such independent play scenarios and wants for each of them, based on the given information, to help him find out each day what the maximum length of a chain of tracks he can obtain in the manner described above (the first task), or the number of distinct ways to achieve this maximum (the second task), calculated modulo $10^9 + 7$. Two ways of achieving the maximum are considered distinct if the two subsets of towns from which he selected the chains of maximum length are different.

# Input data

The input file `cfr.in` contains on the first line a positive natural number $T$, representing the number of scenarios.
For each scenario, the first line contains a number $C$ which represents the task that needs to be solved.
The second line contains $N$, the number of stations, followed by $N - 1$ lines representing the descriptions of the train tracks: $3$ numbers $u_i$, $v_i$, $w_i$ on each line, which represent the stations connected, and the danger level for the track piece number $i$, $1 \leq i < N$.
The next line contains the number $Q$ followed by the descriptions of the $Q$ play days: $2$ numbers $M_i$, $K_i$ on each line, having the meaning from the statement, $1 \leq i \leq Q$.

# Output data

The output file `cfr.out` will contain the answers in the request order, i.e., the maximum length that can be obtained under the conditions of the corresponding day if $C = 1$ or the number of distinct ways to obtain this maximum length modulo $10^9 + 7$, if $C = 2$.

# Constraints and clarifications

* $1 \leq T \leq 3$;
* $1 \leq C \leq 2$;
* $1 \leq N, Q \leq 100 \ 000$;
* $1 \leq u_i, v_i \leq N$;
* $1 \leq w_i, M_i \leq 10^9$;
* $1 \leq K_i \leq N$;
* A chain can be formed by a single station or have at its $2$ ends a station.
* It is not mandatory to use all the received $K_i$ tracks in one day (especially since this might be impossible, as a received piece of track must connect exactly **two distinct stations** in a chain).
* For tests worth $10$ points, $C = 1$ for all scenarios and $1 \leq N, Q \leq 1 \ 000$.
* For other tests worth $10$ points, $C = 1$ for all scenarios and $M_i = 10^9$, $1 \leq i \leq Q$.
* For other tests worth $10$ points, $C = 1$ for all scenarios and $u_i=i, v_i=i+1$, $1 \leq i < N$.
* For other tests worth $10$ points, $C = 1$ for all scenarios and $K_i=1$, $1 \leq i \leq Q$.
* For other tests worth $10$ points, $C = 1$ for all scenarios and no additional constraints.
* For other tests worth $10$ points, $C = 2$ for all scenarios and $1 \leq N, Q \leq 1 \ 000$.
* For other tests worth $10$ points, $C = 2$ for all scenarios and $M_i=10^9$, $1 \leq i \leq Q$.
* For other tests worth $10$ points, $C = 2$ for all scenarios and $u_i=i, v_i=i+1$, $1 \leq i < N$.
* For other tests worth $10$ points, $C = 2$ for all scenarios and $K_i=1$, $1 \leq i \leq Q$.
* For other tests worth $10$ points, $C = 2$ for all scenarios and no additional constraints.

# Example 1

`cfr.in`
```
1
1
13
1 2 1
1 3 2
1 4 2
2 5 3
3 6 1
4 7 3
4 8 2
5 9 4
5 10 4
5 11 4
8 12 3
8 13 1
4
2 10
3 2
1 4
4 3
```

`cfr.out`
```
11
7
7
6
```

## Explanation

At the end there is a visual representation of the network of stations and the respective tracks corresponding to this example (the danger level is marked on the tracks, and as mentioned in the statement, all lengths are constant, one unit). Consider the first day. We only have the tracks with a danger level of at most $2$, so the formed layouts of stations are: $\\{1, 2, 3, 4, 6, 8, 13\\}$, $\\{5\\}$, $\\{7\\}$, $\\{9\\}$, $\\{10\\}$, $\\{11\\}$, $\\{12\\}$, in total $7$ layouts. RAU-Gigel can choose from the first layout the chain of stations $6 \xe2\x80\x93 3 \xe2\x80\x93 1 \xe2\x80\x93 4 \xe2\x80\x93 8 \xe2\x80\x93 13$, of length $5$ (tracks), and from the rest of the layouts there is always a single choice, which is always a chain made up of a single node, of length $0$ (tracks). We observe that RAU-Gigel has enough additional tracks to "link" all the chosen chains together, and so he can form the chain: $6 \xe2\x80\x93 3 \xe2\x80\x93 1 \xe2\x80\x93 4 \xe2\x80\x93 8 \xe2\x80\x93 13 \xe2\x80\x93 5 \xe2\x80\x93 7 \xe2\x80\x93 9 \xe2\x80\x93 10 \xe2\x80\x93 11 \xe2\x80\x93 12$, of length $11$ (tracks). No matter how other chains are chosen, RAU-Gigel cannot form a final chain of strictly greater length, so the answer for the first day is $11$. It is also noteworthy that not all received tracks were used, only $6$ of the $10$. RAU-Gigel cannot use the remaining tracks to extend the obtained chain (for example, to attach another track to one end of the chain, say $12$) because a track must join **exactly 2 distinct stations**.

# Example 2

`cfr.in`
```
1 
2
13
1 2 1
1 3 2
1 4 2
2 5 3
3 6 1
4 7 3
4 8 2
5 9 4
5 10 4
5 11 4
8 12 3
8 13 1
4
2 10
3 2
1 4
4 3
```

`cfr.out`
```
1
3
21
1
```

## Explanation

The visual representation of the network of stations and the respective tracks corresponding to this example is identical to the first example and is found at the end. Consider the second day. We only have the tracks with a danger level of at most $3$, so the formed layouts of stations are: $\\{1, 2, 3, 4, 5, 6, 7, 8, 12, 13\\}$, $\\{9\\}$, $\\{10\\}$, $\\{11\\}$, in total $4$ layouts, numbered from $1$ to $4$ in the order in which they are listed. We observe that the maximum length of a chain RAU-Gigel can obtain in the manner described in the statement is $7$ tracks. We also observe that in an optimal solution he is always obliged to choose a chain of length $5$ from the first layout (it doesn't matter which one even if there are several), and then he can choose any $2$ "chains" from the remaining layouts because all are formed of a single node and have a length of $0$ (tracks), thus RAU-Gigel forming a chain of length $7$ by using the two additional tracks received that day. Thus, the optimal solutions are: $\\{1, 2, 3\\}$, $\\{1, 2, 4\\}$, $\\{1, 3, 4\\}$, in number of $3$ (noting again that the â€œformâ€ of a solution is given by the layouts from which the chains are selected, not by the stations/tracks that make up the final chain).

# The network corresponding to the 2 examples

~[exemplu.png]
