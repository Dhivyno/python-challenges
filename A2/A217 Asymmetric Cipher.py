import random

def generate_keys():
    p = get_random_prime()
    q = get_random_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = get_coprime(phi)
    d = get_inverse(e, phi)
    return ((e, n), (d, n))

def get_random_prime():
    while True:
        p = random.randint(2, 100)
        if is_prime(p):
            return p

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_coprime(n):
    while True:
        e = random.randint(2, n)
        if gcd(e, n) == 1:
            return e

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def get_inverse(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return x

def encrypt(plaintext, key):
    e, n = key
    return [(ord(c) ** e) % n for c in plaintext]

def decrypt(ciphertext, key):
    d, n = key
    return ''.join(chr(int((c ** d) % n)) for c in ciphertext)

plaintext = 'hello world'
public_key, private_key = generate_keys()
print(public_key)
print(private_key)
ciphertext = encrypt(plaintext, public_key)
print(ciphertext)
decrypted = decrypt(ciphertext, private_key)
print(decrypted)
