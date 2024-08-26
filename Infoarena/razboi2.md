## War 2

During the war, food distribution can create numerous problems. It is known that each soldier can carry a certain number of food packages. To avoid conflicts, the soldiers must be divided into $b$ bastions, such that, in the event of the destruction of the first $d$ bastions (for any $d$ from $0$ to $b-1$), the food supplies in bastion $d+1$ can be divided exactly by the number of remaining soldiers.

## Task

Given $N$ soldiers, they need to be divided into $b$ bastions, bastions that will be placed along the battlefront.

## Input data

In the file `razboi2.in`, the first line contains $N$, and the next line contains $N$ values representing the number of food packages carried by each soldier.

## Output data

The file `razboi2.out` will contain $b$ lines ($b$ being the number of bastions). On line $i$ the data about bastion $i$ will be written. The data about a bastion will be in the form $x_{i1}$, $x_{i2}$, $\dots$, $x_{ir}$, where $i1$, $i2$, $\dots$, $ir$ are the soldiers grouped in that bastion.

## Constraints

$1 \leq N \leq 1000$ 

A soldier will carry at least one food package

and at most $1000$ food packages

## Example

`razboi2.in`

```
6 
4 2 3 9 10 3 
```

`razboi2.out`

```
9 3 
4 
10 2 
3 
```

## Explanation

We have $6$ soldiers who carry the quantities $4$, $7$, $3$, $9$, $10$ and respectively $3$ food packages. They were divided into $4$ bastions as follows: In the first bastion, there are $2$ soldiers, one carrying $9$ packages of food, and the other $3$ packages. Similarly, in bastion $2$, there is one soldier carrying $4$ packages, in bastion $3$, there are $2$ soldiers carrying $10$ and $2$ packages, respectively, and in bastion $4$, there is one soldier carrying $3$ packages.