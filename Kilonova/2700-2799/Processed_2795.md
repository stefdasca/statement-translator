Sure! Here's the translated version of the text:

---

The source for this problem can be accessed [here](stolechain.cpp) or in the "Attachments" section on the side.

# Task

Several students at UNSTPB have gathered filled with ideas and enthusiasm to create AcadCoin, their digital currency. While working together on it, they noticed that one of them, named Andrei, seemed to be working on something extra behind their backs. Sebi, always being attentive to details, discovered that Andrei, using his genius thinking, found a hard-to-detect method of stealing coins. Before being excluded from the team, Andrei managed to steal the last slice of pizza and change the source code to give him control over the currency. Now, the team faces a challenging task, which is to neutralize the harmful effects of Andrei's code.

The Blockchain can be imagined as a kind of special notebook used to keep track of a currency's transactions (who paid whom, how much, and when), where anyone can propose transactions. However, for them to be accepted, they must be initiated by the one who wishes to transfer the amount of coins, not by the receiver or anyone else. Therefore, transactions also include a verification number (called a signature), which, through various hashing, encryption, and decryption methods, can confirm the identity of the initiator. Thus, each user will have a pair of keys, one public and one private. Only the user has access to the private key, and it is used for signing. The public key is known throughout the network. Anyone can use it to verify if an operation has been signed by the correct user.

In reality, since the blockchain is a distributed network, the "notebook" is stored by all entities in the network. A user can try to falsify an entry. Therefore, there must be a consensus algorithm where users need to communicate with each other to establish a single truth. The simplest consensus algorithm is decision by majority vote. A malicious user will not be able to introduce an invalid transaction into the blockchain because it will not be accepted by the rest.

In our case, if a transaction receives over $50\%$ confirmations from the network, the transaction is approved. Also, each computer in the network is considered an entity (meaning if a user has $5$ computers, they have $5$ votes). We want to prevent a user from monopolizing the network, so we do not allow anyone to have more than $50\%$ of the number of computers in the network. Thus, when someone tries to add their station to the network, the request can be refused if it endangers security. If the user had too many votes in the network, they could validate their fraudulent transactions from someone else to themselves.

Also, our network allows the change of private and public keys, for which the signature is again necessary.

Our problem views this concept from the perspective of a server receiving requests from users. The signature is already calculated by the user (which is why the `encrypt` function is not used in our program but is present in the `User` class).

Below, we will simulate a coin transfer request sent by a user (all types of requests a user can make follow the same path, so we will not treat them separately). We will observe that the server receives this along with the signature created by the user:
~[Block.png|width=80em]

# Input data
Read $n$, representing the number of users in the blockchain, and then $n$ users with the format `Name Balance Number_of_PCs Exponent Public_key Private_key`.

Next is a number $m$, representing the number of user requests, and then $m$ requests in the form:
   - `SEND Sender_Name Receiver_Name Amount Signature` — transfers `Amount` AcadCoin from `Sender_Name` to `Receiver_Name`'s account;
   - `CHANGE_PASSWORD Name New_Exponent New_Public_Key New_Private_Key Signature` — changes the encryption and decryption details of `Name`;
   - `ADD_PC Name` — adds a computer to `Name` (here the signature is no longer necessary, so it will not be verified by other users).

# Output data
For each of the above commands, the following will be displayed:
- `SEND`:
  - `Invalid signature` if the transaction was not initiated/signed by the sender;
  - `Sender_Name has insufficient balance` if the sender does not have the necessary amount for the transfer;
  - `Sender_Name sent Amount to Receiver_Name` if the transaction was successful;
- `CHANGE_PASSWORD`:
  - `Invalid signature` if the request was not initiated/signed by the one under which the change occurs;
  - `Password changed for Name` if the user's key pair has been changed;
- `ADD_PC`:
  - `PC added to Name` if the computer was added to the network;
  - `PC not added to Name` if the computer was not added to the network.

Then, the balance of each user will be displayed in the form `Name Balance`.

# Constraints and clarifications
   - The input requests will contain valid user names.
   - The signature for `SEND` comes from concatenating the following values into a string, separated by a space: `Sender_Name Receiver_Name Amount`.
   - The signature for `CHANGE_PASSWORD` comes from concatenating the following values into a string, separated by a space: `Name New_Exponent New_Public_Key New_Private_Key`.
   - The code in the `Hasher` class has no bugs.

# Example 1
`stdin`
```
2
Alice 1900 4 7 3262089553 2329982343
Bob 2000 4 7 3566775067 2547610983
10
SEND Alice Bob 200 2346129895
SEND Alice Bob 300 3112513739
SEND Alice Bob 200 2346129895
SEND Alice Bob 200 1234567890
CHANGE_PASSWORD Alice 7 3484061857 2488530883 1230990308
CHANGE_PASSWORD Alice 7 3484061857 2488530883 18090708
CHANGE_PASSWORD Alice 7 3484061857 2488530883 18090708
CHANGE_PASSWORD Alice 7 3484061857 2488530883 3298412722
SEND Alice Bob 200 775141743
SEND Alice Bob 1001 1428497737
```
`stdout`
```
Alice sent 200 to Bob
Alice sent 300 to Bob
Alice sent 200 to Bob
Invalid signature
Password changed for Alice
Password changed for Alice
Password changed for Alice
Invalid signature
Alice sent 200 to Bob
Alice has insufficient balance
Alice 1000
Bob 2900
```

# Example 2
`stdin`
```
4
Bjarne 7800 1 7 1490867669 425940127
Ada 6400 1 7 3524241173 2013783943
Carmack 3600 9 7 1659516809 948247783
Guido 0 10 7 2939108723 419857087
7
ADD_PC Guido
ADD_PC Guido
ADD_PC Carmack
ADD_PC Ada
ADD_PC Guido
ADD_PC Guido
ADD_PC Guido
```
`stdout`
```
PC added to Guido
PC not added to Guido
PC added to Carmack
PC added to Ada
PC added to Guido
PC added to Guido
PC not added to Guido
Bjarne 7800
Ada 6400
Carmack 3600
Guido 0
```
## Explanation
For the second example, in the second and seventh commands, Guido's computers would exceed half of the total, so the server does not allow adding the computer.