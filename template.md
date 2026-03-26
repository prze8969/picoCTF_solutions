# [Challenge Name] — [CTF Name]

## Challenge Info

| Field      | Details              |
|------------|----------------------|
| Category   | Cryptography         |
| Difficulty | Easy / Medium / Hard |
| Points     | 100                  |
| Author     | challenge_author     |
| Flag       | `picoCTF{...}`       |

---

## Description

> Paste the challenge description here exactly as given.

**Attachments:** `file1.py`, `file2.txt` *(if any)*

---

## Recon

What you noticed first. File types, hints in the description, tools you opened it with.

```
# Example: checking the file
file attachment.txt
strings attachment.bin
```

---

## Approach

Walk through your thought process — what you tried, what failed, what led you to the solution.

1. Noticed the encryption used small public exponent `e`
2. Suspected small message attack since `m^e < n`
3. Tried taking the integer cube root of ciphertext directly

---

## Solution

Step-by-step breakdown of what actually worked.

```python
from sympy import integer_nthroot

c = 0xDEADBEEF  # ciphertext
e = 3

m, is_perfect = integer_nthroot(c, e)
print(bytes.fromhex(hex(m)[2:]).decode())
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