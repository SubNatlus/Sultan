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

    def get_input(self):
        """
        Get validated user input.
        :return: Two positive integers.
        """
        while True:
            try:
                a = int(input("Enter the first positive integer: "))
                b = int(input("Enter the second positive integer: "))
                if a > 0 and b > 0:
                    return a, b
                else:
                    print("Both numbers must be positive integers. Please try again.")
            except ValueError:
                print("Invalid input. Please enter positive integers only.")
