
Each of us would like to know our lucky number that will influence us throughout our life. This non-zero number consisting of a single digit can be determined based on each person's name.

To find this number, there is an ancient technique, thousands of years old, that involves building the pyramid of luck by performing only addition operations in the set of digits. Thus, each letter of the alphabet is associated with a non-zero digit according to the adjacent table.

The lucky digit is determined as follows: the corresponding digit is noted to the right of each letter and two neighboring digits are added, obtaining a new sequence of digits with which the process is repeated until a single digit is obtained.

Each time the result of an addition between two digits will still be a non-zero number less than or equal to $9$. For larger results, the addition operation of the digits that make up this result is applied again, finally obtaining a single digit.

~[piramida.png]

# Task

Given a string of characters representing a person's name, display the pyramid of luck and determine the corresponding lucky digit.

# Input data

The input file `piramida.in` contains a string of characters on the first line representing a person's name. This string of characters is correctly entered and contains only letters; it does not matter if they are uppercase or lowercase.

# Output data

The output file `piramida.out` will contain the person's name written in lowercase on the first line. On the following lines, the pyramid of luck will be displayed as follows:
- The digits of a row of the pyramid will be displayed separated by a single space;
- The first row of digits of the pyramid will be aligned to the left margin, and the other rows will be displayed such that they shape the pyramid as shown in the example below.

# Constraints and clarifications

* The given string of characters will not exceed $80$ characters.

# Example

`piramida.in`
```
Sonia
```

`piramida.out`
```
sonia
1 6 5 9 1
 7 2 5 1
  9 7 6
   7 4
    2
```

## Explanation

$1+6=7$;
$6+5=11=1+1=2$;
$5+9=14=1+4=5$;
$9+1=10=1+0=1$;
