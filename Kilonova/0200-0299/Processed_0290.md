```markdown
## **!! YOU ARE NOT ALLOWED TO OPEN THE FILE `ez.out` !!**

*Ez* received a computer for their birthday, but it came defective from the factory: when *Ez* types a word on the keyboard, the computer replaces the vowels `aeiouAEIOU` respectively with the letters `qwrtyQWRTY`. If the words already contain the letters `qwrtyQWRTY`, the computer replaces them with the digits `1234512345` respectively to differentiate them; also, after these modifications, the computer replaces all consonants except `qwrtyQWRTY` in words of even length with the next letter in the alphabet. Words are separated only by spaces or newline characters (`\n`).

# Task
The string of characters entered by *Ez* is found in the file `ez.in`. ***Implement the function `solve()` which will change the content of this file with the string modified by the computer.***

# Example
`ez.in`
```
ana are mere
```
**`ez.in`**
```
qnq q3w nw3w
```

## Subtask 1 (70 points)
* The string has a maximum of $1\ 000$ characters.

## Subtask 2 (30 points)
* The string has a maximum of $500\ 000$ characters.

# Constraints and clarifications
* The ASCII codes of the characters in the string are between $32$ and $126$, including character $10$. Below is a table with the ASCII codes for each character.
* The next letter in the alphabet after `z` is considered to be the letter `a`, and the next letter in the alphabet after `Z` is considered to be the letter `A`.
* Although there is `1MB` of available memory, **declaring any array of $500\ 000$ elements will not result in the maximum score!**
* ***Make sure that when exiting the `solve()` function all streams to the file `ez.in` are closed!***
* **Attention!** The task is to implement the `solve()` function. The code you submit will not contain the `main()` function — it will be replaced by the `solve()` function. Here is an example of a valid program:
```cpp
#include <fstream>
void solve() {
   std::ofstream fout("ez.in");
   fout << "qnq q3w nw3w";
   fout.close();
}
```

~[ascii_table.png]
```
