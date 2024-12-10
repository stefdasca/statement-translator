Lidorians and Senopictians are in conflict over the enchanted ron, arbitrated by the Orintians, chosen by the warring parties as judges. Orintia proposed: “The enchanted ron will be hidden among other $k$ rons with the same appearance but all made from a heavier material than the original, having a standard mass different from that of the enchanted ron. To discover it, think that you have a balance and all $k+1$ rons at your disposal. The Lidorians and then the Senopictians will each say a single number, representing the maximum number of weighings allowed to discover the enchanted ron. If neither party states the correct number, then the enchanted ron will remain in Orintia. If both parties state the correct number, the ron will also remain with the Orintians.”

# Task

Your task is to indicate the country that wins the enchanted ron: Lidoria - $L$, Senopictia – $S$, Orintia – $O$.

# Input data

The file `ron.in` contains on the first line the number $k$, and on the second line two numbers $RL$ and $RS$ separated by a space. $RL$ represents the response from the Lidorians, and $RS$ the response from the Senopictians.

# Output data

The file `ron.out` contains one of the letters $L, S$, and $O$.

# Constraints and clarifications

* $1 < k < 10 \ 000$;
* $RL, RS$ are natural numbers at most equal to $k$;
* the enchanted ron is a cuboid engraved with the fixed signs of power;
* the maximum allowable number of weighings is not achieved by weighing a ron multiple times nor by weighing the rons as many times as possible; the weighing implies that there is an equal number of rons on each arm of the balance ($1 - 1$, $2 - 2$, etc.)

# Example 1

`ron.in`
```
7
1 3
```

`ron.out`
```
O
```

## Explanation

The maximum allowed is $2$, so the enchanted ron remains in Orintia

# Example 2

`ron.in`
```
4
2 2
```

`ron.out`
```
O
```

## Explanation

The maximum allowed is $2$, but since it's a tie, the ron remains in Orintia