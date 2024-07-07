On Mars, an intense war is taking place between the troops of Earth colonists and the native reptilian tribes.

To gain decisive control of the planet, the Earthlings have sent commando troops into the underground gallery system on Mars, represented as a configuration of $n$ caves connected by $m$ one-way channels. Their mission is to get from the colonists' underground base located in gallery $1$ to the reptilians' underground city placed in gallery $n$ to destroy the extraterrestrial resistance.

Knowing that each of the $m$ channels between the galleries is protected by a certain number of reptilian soldiers, the commando troops need to choose the routes that are the most vulnerable to an assault, protected by a **minimum number** of enemies.

The task is to find the set of galleries that will be **necessarily traversed** by the Earthlings during the mission, using **any** route that is protected by a **minimum number** of enemies.

# Input data
The values $n$ (number of galleries) and $m$ (number of underground channels) will be read from the keyboard, then $m$ triplets of the form $u$, $v$, $w$, with the property that there is a one-way channel between cave $u$ and cave $v$, protected by exactly $w$ soldiers.

# Output data
Print on the first line the value $k$ (the number of galleries that will be necessarily traversed by the colonists), and on the next line the $k$ galleries in increasing order.

# Constraints and clarifications
* It is guaranteed that there is an optimal route between galleries $1$ and $n$ for each test.
* $1 \leq n \leq 100 \ 000$;
* $1 \leq m \leq 200 \ 000$;
* $1 \leq u, v \leq n$;
* $1 \leq w \leq 1 \ 000 \ 000 \ 000$.

# Example

`stdin`
```
5 6
1 2 3
1 3 4
2 3 1
2 4 5
3 4 1
4 5 8
```

`stdout`
```
4
1 3 4 5
