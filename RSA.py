import gmpy2
from gmpy2  import mpz
random_state = gmpy2.random_state(42)
#def prime_generator(bits):
 #   temp = gmpy2.mpz_rrandomb(random_state, 1538)
  #  return gmpy2.next_prime(temp)



print("-----KEY GENERATION-----")
bit_size=1538
"""p=0 #Random p and q value generator
q=0
while(p==q):
    p= prime_generator(bit_size)
    q= prime_generator(bit_size)"""

#To input value of p and q
p= int(input("Enter value of p"))
q= int(input("Enter value of q"))

n= gmpy2.mul(p,q);
phi= gmpy2.mul(p-1,q-1);

print("\nThe first prime is p =  ",p)
print("\nThe second prime is q =  ", q)
print("\nThe composite module n =",n)

e=0
while(e<=1 or gmpy2.gcd(phi,e)!=1):
    e=gmpy2.mpz_random(random_state, phi)

print("\nThe encryption exponent e = ", e)

d= gmpy2.invert(e, phi)

print("\nThe decryption exponent d =", d)
print("\n-------------------------------------------------------------")

print("\nPlease Enter the options: ")
print("\n1 to Encrypt")
print("\n2 to Decrypt")
option= int(input("\nYour Option: "))

print("-------------------------------------------------------------")

if(option == 1):
    print("\nEncryption: ")
    m = gmpy2.mpz_random(random_state, 1538)#taking message size of 512 bits'
    print("Plaintext to be encrypted is m = ",m)
    c= gmpy2.powmod(m , e , n)
    print("\nCiphertext is c = ", c)
    
elif(option == 2):
    print("\nDecryption: ")
    c = int(input("\nCiphertext to be decrypted is c = "))
    m = gmpy2.powmod(c, d, n)
    print("\nDecrypted plaintext is m = ", m)
