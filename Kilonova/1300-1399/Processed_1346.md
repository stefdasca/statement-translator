```markdown
Neurological researchers have identified in the human retina an area of bipolar neurons, which have exactly two branches, arranged in a pyramidal structure. The neuron structure is arranged on $n$ levels such that on a level $k$ there exist $k$ neurons $(k = 1, 2, \dots, n)$. It was found that a neuron in this structure can transmit nerve impulses only to the two neurons, corresponding to the two branches, located on the next level.

Upon receiving the first impulse by a neuron in the network, it forwards the impulse as follows: if it is on an even level, it sends it to the left neuron, and if it is on an odd level, it sends it to the right neuron on the next level.

Impulse transmission between neurons works alternatively. Thus, after an impulse is transmitted to the neuron on the left branch, the next impulse will be transmitted to the neuron on the right branch and vice versa.

The neurons on the last level of the structure, also called receptor neurons, receive the impulses from this network. All impulses come from the neuron located at level $1$.

~[image.png|align=left]

# Task

Knowing the number $n$ of levels on which the neurons are arranged and the number $m$ of impulses transmitted in the network, write a program to determine the number of impulses received by each neuron on level $n$.

# Input data

The first line of the input file `neuroni.in` contains two natural numbers $n$ and $m$ separated by a space, having the meaning described above.

# Output data

The first line of the output file `neuroni.out` will contain the number of impulses received by each neuron on level $n$, written from left to right, separated by a space.

# Constraints and clarifications

* $2 \leq n \leq 100$
* $1 \leq m \leq 100\ 000$
* The thickened branches in the figure show the direction of transmission of the first impulse.

# Example

`neuroni.in`
```
3 5
```

`neuroni.out`
```
1 3 1
```

## Explanation

The path of the $5$ impulses and the number of impulses received at level $3$ will be as follows:
$1:$ right – left $(0,1,0)$
$2:$ left – left $(1,1,0)$
$3:$ right – right $(1,1,1)$
$4:$ left – right $(1,2,1)$
$5:$ right – left $(1,3,1)$
```
