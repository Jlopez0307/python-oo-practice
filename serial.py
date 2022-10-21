"""Python serial number generator."""




class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = self.next = start

    def reset(self):
        """Holds initial start value to reset generator"""
        self.next = self.start
    
    def generate(self):
        self.next += 1
        return self.next - 1


