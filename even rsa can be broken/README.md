

## Challenge Info

| Field      | Details                               |
|------------|---------------------------------------|
| Category   | Cryptography                          |
| Difficulty | Easy                                  |
| Points     | 000                                   |
| Author     | Michael Crotty                        |
| Flag       | `picoCTF{tw0_1$_pr!m341c6ed35}`       |

---

## Description

> This service provides you an encrypted flag. Can you decrypt it with just N & e?

Additional details will be available after launching your challenge instance.

**Attachments:** `encrypt.py`

---


## Recon

Notice how the value of N is even ?

That means one of the factors of N is 2, 
Because 2 is the only even prime number
and N is a product of 2 prime numbers

Hints given :
How much do we trust randomness?
Notice anything interesting about N?
Notice anything interesting about N?

```
Run the instance 
You will find 3 values :
N: 22228565033374419386210276060739184651381287303738904053191115893339305990558340889505285285022750369440873429421146749316596107826222950220702588186290402
e: 65537
cyphertext: 1022893869467190125893616050649983079453974246030359744888315506373350012868214118150105481709393824756730226746131217968200877521599249821181121929741163

```

---

## Approach

1. Noticed the encryption used small even prime number 2 
2. Divided N by 2 to get the other number

---

## Solution

Step-by-step breakdown of what actually worked.

```python


print("Note : This only works for picoCTF puzxzle not for real RSA systems")
n =int(input("Enter the value of N " )) 
e = int(input("Enter the value of e "))

cyphertext= int(input("Enter the value for cyphertext "))
def decode(n,e,cypertext):
    #Factors of N
    p = 2
    q = n//2

    #Since the message is already encrypted, and we have got the e, we would just find the deccryption key or d

    #For finding the decryption key

    # Calculate Euler's totient function phi(n)= (p - 1) * (q - 1).

    phi = (p-1)*(q-1)
    phi = int(phi)

    d = pow(e, -1, phi)

    #Decrypting the message's to a number

    decrypted_cyperNo = pow(cyphertext,d,n)


    #converting the decrypted message into binary number format 

    binary_decryptedNo = format(decrypted_cyperNo, 'b')

    #Chunking the binary bits to grps of 8

    # for that chunking we need how many grps, so to calculate how many grps we give this command

    num_bytes = (decrypted_cyperNo.bit_length() + 7) // 8

    # variable.to_bytes(num , 'big') = >  converts variables into num bytes using big-endian order.

    #big endian order = > it reads stuff from high to low, i.e desending order

    #other parameter is little endian order = > it reads stuff from low to high

    result_bytes = decrypted_cyperNo.to_bytes(num_bytes, 'big')

    # decode() = > it decodes the result_bytes, which are in decimal number format
    # like 112 to 'p'
    print(result_bytes.decode())


decode(n,e,cyphertext)

```

**Output:**
```
picoCTF{tw0_1$_pr!m341c6ed35}
```

---

## Flag

```
picoCTF{tw0_1$_pr!m341c6ed35}
```

---

## Lessons Learned

- RSA encryption decryption