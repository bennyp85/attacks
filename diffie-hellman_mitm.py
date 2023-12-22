import random

# public keys are taken
# p is a prime number
# g is a primitive root of p
p = int(input('Enter a prime number : '))
g = int(input('Enter a number : '))

class A:
    """
    Class representing a participant in the Diffie-Hellman key exchange protocol.

    Attributes:
        n (int): The private number selected by Alice.

    Methods:
        publish(): Generates and returns the public value.
        compute_secret(gb): Computes and returns the secret key using the received public value.
    """

    def __init__(self):
        self.n = random.randint(1, p)

    def publish(self):
        return (g**self.n) % p

    def compute_secret(self, gb):
        return (gb**self.n) % p

class B:
    """
    Class representing a participant in the Diffie-Hellman key exchange protocol.

    Attributes:
        a (int): Random private number selected for Alice.
        b (int): Random private number selected for Bob.
        arr (list): List containing the private numbers of Alice and Bob.

    Methods:
        publish(i): Generates and returns the public value for the given participant index.
        compute_secret(ga, i): Computes and returns the secret key for the given participant index.

    """

    def __init__(self):
        self.a = random.randint(1, p)
        self.b = random.randint(1, p)
        self.arr = [self.a, self.b]

    def publish(self, i):
        """
        Generates and returns the public value for the given participant index.

        Args:
            i (int): Index of the participant.

        Returns:
            int: The computed public value.

        """
        return (g**self.arr[i]) % p

    def compute_secret(self, ga, i):
        """
        Computes and returns the secret key for the given participant index.

        Args:
            ga (int): The public value received from the other participant.
            i (int): Index of the participant.

        Returns:
            int: The computed secret key.

        """
        return (ga**self.arr[i]) % p

alice = A()
bob = A()
eve = B()

# Printing out the private selected number by Alice and Bob
print(f'Alice selected (a) : {alice.n}')
print(f'Bob selected (b) : {bob.n}')

# Generating public values 
ga = alice.publish()
gb = bob.publish()
gea = eve.publish(0)
geb = eve.publish(1)

print(f'Alice published (ga): {ga}')
print(f'Bob published (gb): {gb}')
print(f'Eve published value for Alice (gc): {gea}')
print(f'Eve published value for Bob (gd): {geb}')

# Computing the secret key
sa = alice.compute_secret(gea)
sea = eve.compute_secret(ga, 0)
sb = bob.compute_secret(geb)
seb = eve.compute_secret(gb, 1)

print(f'Alice computed (S1) : {sa}')
print(f'Eve computed key for Alice (S1) : {sea}')
print(f'Bob computed (S2) : {sb}')
print(f'Eve computed key for Bob (S2) : {seb}')
