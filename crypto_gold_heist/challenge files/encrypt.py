from os import environ

from Crypto.Util.number import bytes_to_long, getPrime, getRandomRange, isPrime

flag = environ['flag']
bits = 1420


def generate_pub_key():
    p = getPrime(bits)
    q = p + 1
    while not isPrime(q):
        q += 1
    n = p**2 * q
    g = getRandomRange(2, n)
    h = pow(g, n, n)

    assert pow(g, p - 1, p**2) != 1

    return n, g, h


def encrypt(message, key):
    n, g, h = key
    r = getRandomRange(1, n)
    return (pow(g, bytes_to_long(bytes(message, 'utf-8')), n) *
            pow(h, r, n)) % n


key = generate_pub_key()
with open("out.txt", "w") as f:
    f.write(f"key (n, g, h) = {key}\nc = {encrypt(flag, key)}")