\begin{document}
When we run instance we get the output :


----------------------TOPIC TO BE DICUSSED----------------------
RSA Algorithm :

1. Workflow:
    There are two keys, public key and private key  
    Public key is exposed to everyone, and is used for encrypting the data
    Private key isnt exposed to everyone, and is used for decrypting the data

2. How it works:
    1.Public key generation:
        Lets take two prime numbers, p and q
        Calculate N = p*q
        Calculate the euler's totient function

NOTE: Euler's totient function?
= > It is a function that takes in ONE value and outputs all the coprimes with that number
= > It is represented by phi(n)


\end{document}



# [Challenge Name] — [CTF Name]

## Challenge Info

| Field      | Details              |
|------------|----------------------|
| Category   | Cryptography         |
| Difficulty | Easy                 |
| Points     | 000                  |
| Author     | Michael Crotty       |
| Flag       | `picoCTF{...}`       |

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
3. 

---

## Solution

Step-by-step breakdown of what actually worked.

```python

N=22228565033374419386210276060739184651381287303738904053191115893339305990558340889505285285022750369440873429421146749316596107826222950220702588186290402
e= 65537
cyphertext=1022893869467190125893616050649983079453974246030359744888315506373350012868214118150105481709393824756730226746131217968200877521599249821181121929741163

/*Factor of N*/
p = 2
q = N/2

/*Since the message is already encrypted, and we have got the e, we would just find the deccryption key or d*/

/*
For finding the decryption key, Extended Euclidean Algorithm is used
*/


```

**Output:**
```
picoCTF{...}
```

---

## Flag

```
picoCTF{example_flag_here}
```

---

## Lessons Learned

- What concept this challenge tested
- What you'd do faster next time
- Any tool or trick you learned