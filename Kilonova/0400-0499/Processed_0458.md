```markdown
# Task

After Hayley realized that Essex is in fact not a continent, but a county, she decided to start a love journal with one of the fellow Love Islanders. Since they are not remarkably smart by nature, they forgot to add the spaces in between their daily entries in their journal and they now need your help to figure out how did their journal look in fact.

More formally, we are given a string of length $n$ which contains only lowercase letters, digits and the character '.' (the dot).

We define a journal as a sequence of substrings which begin with a certain date (the format of the date is dd.mm), for example 01.01 or 16.11 are valid dates, contain a non-empty text and they end either at the end of the string, or when a new daily entry is added, which is the day after the day in which the previous entry started (for example, 15.03 is after 14.03 and 01.01 is after 31.12). The journal entry doesn't have to end the first time we find a new date in it.

Since the answer can be big, Hayley wants it printed modulo $666013$ (she can't read big numbers).

# Input

The input will contain on the first line $n$, the length of the string ($1 \le n \le 10^6$).

The second line will contain the string $s$, ($|s| = n$).

For tests worth $20$ points, ($1 \le n \le 50$).

For tests worth $30$ more points, ($1 \le n \le 5000$).

February is always considered to have $28$ days in length.

Any pattern of type dd.mm will be followed by at least one letter, even if it can't be part of any valid date according to the journal chronology.

The string will start with a valid date.

# Output

The output will contain on the first line the answer requested by Hayley.

# Example
`stdin`
```plaintext
35
01.01ily02.01ily02.01xxox03.01acasa
```

`stdout`
```plaintext
5
```

# Explanation

The journals we can form are

[01.01ily02.01ily02.01xxox03.01acasa]

[01.01ily; 02.01ily02.01xxox03.01acasa]

[01.01ily; 02.01ily02.01xxox; 03.01acasa]

[01.01ily02.01ily; 02.01xxox03.01acasa]

[01.01ily02.01ily; 02.01xxox; 03.01acasa]
```
