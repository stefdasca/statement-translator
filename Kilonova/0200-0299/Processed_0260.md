# Converting an ASCII Text to Base64

~[ascii_table.png]

Let's take the string `aB` as an example. We need to transform each character from this string into the binary representation of their ASCII codes (the table above). The character `a` has the ASCII code `97`, so its representation in base 2 is `01100001`. For the character `B`, the representation in base 2 is `01000010`. Now, we form a string from these representations by concatenating them in order: `0110000101000010`.
\
The next step is to split the new string into groups of 6 bits. If the last group has fewer than 6 bits, we add zeros at the end until we get 6 bits. The groups are `011000`, `010100`, `001000`.

The next step is to transform these numbers into base 10, and then transform them into characters from the Base64 encoding using the table below. The first group ($24$) transforms into the character `Y`, the second group ($20$) transforms into the character `U`, and the last group into the character `I`. We combine the results and get the string `YUI`.

The next and final step is to add characters `=` at the end of this string until its length becomes a multiple of $4$. This step is not followed in some cases, as the string remains in the form `YUI` instead of `YUI=`, but **for this problem, we will add characters `=` at the end**.

For clarifications, consult [this site](https://base64.guru/learn/base64-algorithm/encode).

~[base64_table.png]

# Task
Implement two functions that transform a text written in `ASCII` encoding into a text written in `Base64` encoding and vice versa.
The functions have the following signatures:
```cpp
std::string ASCII_to_Base64(std::string s);
std::string Base64_to_ASCII(std::string s);
```

# Constraints and clarifications
* The length of the string $s$ is strictly less than $100\ 001$.
* For 50 points, you need to correctly implement the function `ASCII_to_Base64()`, and for another 50 points, the function `Base64_to_ASCII()`.
* It is guaranteed that $s$ contains only characters that belong to the respective encoding (for `ASCII` encoding, the characters in the first table, and for `Base64` encoding, the characters in the second table, plus `=`).
* It is guaranteed that the text written in `Base64` encoding contains only valid characters for `ASCII` encoding when transformed.
* **Attention!** The task is to implement the aforementioned functions. The code you submit will not contain the `main()` function — it will be replaced by the two functions. Here is an example of a valid program:
```cpp
#include <string>
using namespace std;
string ASCII_to_Base64(string s) { return "QSB2ZW5pdCBBbGV4IQ=="; }
string Base64_to_ASCII(string s) { return ":))"; }
```