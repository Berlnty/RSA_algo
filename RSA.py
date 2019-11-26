import binascii
import random
from math import gcd




def main():
    n = 9516311845790656153499716760847001433441357  # p*q = modulus
    e = 65537
    d = 5617843187844953170308463622230283376298685

    p = 199  # int(input("p: prime number "))
    q = 197  # int(input("q: prime number"))
    n = p * q

    phi = (p - 1) * (q - 1)

    e = get_e(phi)

    d = modinv(e, phi);

    message = 'l'


    print('message                 ', message)

    hex_data = binascii.hexlify(message.encode())
    print('hex data                ', hex_data)

    plain_text = int(hex_data, 16)
    print('plain text integer      ', plain_text)

    if plain_text > n:
        raise Exception('plain text too large for key')


    encrypted_text = pow(plain_text, e, n)
    print('encrypted text integer  ', encrypted_text)

    decrypted_text = pow(encrypted_text, d, n)
    print('decrypted text integer  ', decrypted_text)

    print('message                 ',
          binascii.unhexlify(hex(decrypted_text)[2:]).decode())  # [2:] slicing, to strip the 0x part

    r=2
    c_dash= encrypted_text*(r**e) %n
    m_dash= (c_dash**d) %n
    result =m_dash/r
    print('deciphered text integer  ', result)
    return


def get_e(phi):
    e=0
    check = True
    while(check):
        temp=random.randint(2,phi)
        if(gcd(temp, phi) == 1):
            check = False
            e = temp
    return e


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m



if __name__== "__main__":
    main()
