

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