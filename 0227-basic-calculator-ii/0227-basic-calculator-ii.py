class Solution:
    def calculate(self, s: str) -> int:
        current_number = 0
        string_length = len(s)
        previous_operator = '+' 
        stack = []

        for index, char in enumerate(s):

            if char.isdigit():
                current_number = current_number * 10 + int(char)

            if index == string_length - 1 or char in '+-*/':
                if previous_operator == '+':
                    stack.append(current_number)
                elif previous_operator == '-':
                    stack.append(-current_number)
                elif previous_operator == '*':
                    stack.append(stack.pop() * current_number)
                elif previous_operator == '/':
                    stack.append(int(stack.pop() / current_number))
                previous_operator = char
                current_number = 0
                
        return sum(stack)

        