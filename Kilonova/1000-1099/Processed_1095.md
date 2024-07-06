Sure, here is the translated text:

---

There are many viruses today that act in different ways on the information stored on a computer. Among these, there are some less dangerous ones that are content to only simulate a certain alteration of the information. Let's assume we want to write such a virus that acts only on text information on the computer screen. In text mode, the screen consists of $n$ lines each containing $m$ characters. The characters are stored in the computer's memory by their ASCII code, represented in binary on $8$ bits. The bits are numbered from $0$ to $7$ from right to left, with the leftmost bit being the most significant bit.

Every second, the virus simultaneously transforms all the characters on the screen according to the following rules:

1. The virus affects only the characters whose codes do not have all bits equal to $0$; the character whose code has all bits equal to $0$ is called unattackable;
2. Determine the characters whose codes have the maximum number of bits equal to $1$; for each such character **the 2 most significant bits** equal to $1$ in the code are transformed into $0$, and if it does not have $2$ bits equal to $1$ in the code, the only existing bit $1$ will be transformed into $0$;
3. For all other attackable characters, **the least significant bit** equal to $0$ in the code is transformed into $1$;
4. Some characters may generate errors in the execution of the virus because by successively transforming their codes, cycles can be obtained; these characters have ASCII codes $1$, $3$, $7$, $15$, $31$, $63$, $127$ and the virus immediately transforms them into $0$ (i.e., they become unattackable), regardless of when such a character appears (i.e., whether it initially exists on the screen or appears after a transformation).

# Task

Knowing the initial configuration of the screen, write a program that solves the following two tasks:

1. determine the number of unattackable characters obtained in the first second (i.e., after the first transformation);
2. determine after how many seconds all the characters on the screen are unattackable.

# Input data

The input file `virus.in` contains on the first line two natural numbers separated by a space $n$, $m$, representing the dimensions of the screen. Each of the following $n$ lines contains $m$ characters, representing the characters initially existing on the screen. The last line of the input file contains the task that needs to be solved ($1$ or $2$).

# Output data

The output file `virus.out` will contain a single line which will contain a natural number, representing the answer to the task specified in the input file.

# Constraints and clarifications

* $1 \leq n, m \leq 100$
* The characters initially on the screen have codes between $32$ and $127$.
* For tests worth $30$ points, the task is $1$.

# Example 1

`virus.in`
```
2 2
AA
AA
1
```

`virus.out`
```
4
```

## Explanation

The character $A$ has the code $01000001$, so the maximum number of bits equal to $1$ is $2$ (equal for all characters); after one second all the $4$ characters will have the code $00000000$ (hence they become unattackable).

# Example 2

`virus.in`
```
3 3
AAC
AAC
CCC
2
```

`virus.out`
```
2
```

## Explanation

In the first second:

- the maximum number of bits equal to $1$ in the characters' codes is $3$ ($C$ having the code $01000011$); after eliminating the two most significant bits $1$ the code of $C$ becomes $00000001$, so it becomes a character that generates errors and the virus immediately transforms it into $00000000$ (unattackable);
- the other characters $A$ (with the code $01000001$) become $C$ (code $01000011$).

In the second second the maximum number of bits equal to $1$ is $3$, the two most significant bits $1$ are eliminated, the code becomes $00000001$ resulting in a character that generates errors, so the virus transforms it into unattackable. Thus, after two seconds all the characters are unattackable.

---

If you need further changes or have specific questions, feel free to ask!