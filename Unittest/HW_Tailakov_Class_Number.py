
class Number:
    def __init__(self, value):
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def to_octal(self):
        return oct(self.value)

    def to_hexadecimal(self):
        return hex(self.value)

    def to_binary(self):
        return bin(self.value)


