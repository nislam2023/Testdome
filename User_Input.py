class TextInput:

    def __init__(self):
        self.concatenated_value = ""

    def add(self, char_to_add=None):
        if char_to_add is not None:
            self.concatenated_value += str(char_to_add)

    def get_value(self):
        return self.concatenated_value


# inp = TextInput()
# print(inp.add(2))
# print(inp.add('a'))
# print(inp.add('!'))
# print(inp.get_value())


class NumericInput(TextInput):

    def add(self, char_to_add=None):
        if char_to_add is not None and char_to_add.isnumeric():
            self.concatenated_value += str(char_to_add)

    def get_value(self):
        return self.concatenated_value



# input = NumericInput()
# input.add("1")
# input.add("a")
# input.add("0")
# print(input.get_value())

if __name__ == '__scratch_2__':
   input = NumericInput()
   input.add("1")
   input.add("a")
   input.add("0")
   print(input.get_value())
