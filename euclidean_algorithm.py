class EuclideanAlgorithm:
    """
    Class to encapsulate the Euclidean Algorithm.
    """

    def gcd(self, a, b):
        """
        Compute the greatest common divisor (GCD) of two positive integers.
        :param a: First positive integer.
        :param b: Second positive integer.
        :return: GCD of a and b.
        """
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a

