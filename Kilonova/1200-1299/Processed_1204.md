Below is the translated version of the given competitive programming problem statement from Romanian to English, following the provided instructions:

---

Chucky the Hen $767$ needs to traverse the yard by jumping from one coop to another or flying over coops, from the first to the last coop. The coops are represented by rectangles with a width of $1 \ m$ and given heights, and they are numbered in order from left to right with numbers from $1$ to $n$. Two consecutively numbered coops are adjacent. Initially, Chucky has a number of energy units. If at any point Chucky’s energy becomes **strictly negative** or she is **unable to make another move** (encounters a coop higher than the one she is on), **she can no longer continue** on that path.

Chucky can move using the following types of movements:

* **Step**. The hen steps horizontally from a coop of height $H$ to the next coop of the same height (in the illustration: from position $h$ to $i$). In this case, **neither energy is lost nor gained**.
* **Landing**. The hen lands on a coop of height $H$, coming from flying at the same height $H$ (example in the illustration: from $g$ to $h$). In this case, **neither energy is lost nor gained**.
* **Take-off**. The hen flies $1 \ m$ horizontally from a coop (example in the illustration: from $x$ to $a$). In this case, the hen **loses one energy unit**.
* **Horizontal flight**. The hen flies horizontally (example in the illustration: from $a$ to $b$, from $b$ to $c$, $\\dots$). In this case, the hen **loses one energy unit** for each meter traveled horizontally.
* **Descent**. The hen descends vertically (example in the illustration: from $a$ to $d$, or from $d$ to $g$). In this case, the hen **gains one energy unit** for each meter descended.

Below, we have a path consisting of $4$ coops with heights $4$, $1$, $2$, $2$. We illustrate different types of movements from position $x$ (which does not represent a complete path):

~[gaina.png]

# Task

Determine the **minimum energy** (a natural number) that Chucky must have at the beginning of the journey (when she is on the first coop), so that she can reach coop $n$, **having energy always greater than or equal to $0$**.

# Input data

The input file `gaina.in` contains two lines. The first line contains the natural number $n$. The second line contains $n$ natural numbers $h_1$, $h_2$, $\\dots$, $h_n$ (where $h_i$ represents the height of coop $i$), separated by a space.

# Output data

The output file `gaina.out` contains a single line which contains a natural number $K$ representing the **initial minimum energy** with which Chucky the Hen can reach coop $n$, always having energy greater than or equal to $0$.

# Constraints and clarifications

* $0 < n < 10\ 001$
* $0 \leq h_i \leq 30\ 000$
* For the test data, there is always a solution (the first coop has a height greater than or equal to the height of any other coop).

# Example 1

`gaina.in`
```
3
2 2 0
```

`gaina.out`
```
1
```

# Example 2

`gaina.in`
```
6
3 0 0 2 1 1
```

`gaina.out`
```
2
```

---

If you notice any grammatical or syntactical errors, please point them out for correction.