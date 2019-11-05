# A first-in, first-out list of data
# Can add items to the top. Must remove the top item first before you can get anything below.
# Can imagine a stack of porcelain plates, where you can only grab the top-most plate...
# without risking damaging them or making a ton of unwanted, deafening noise.


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []


def is_balanced(str):  # O(n), linear-time
    s = Stack()  # create empty stack

    for char in str:
        # if closing paren, the previous should be a match to even out.
        if char == '}' and s.peek() == '{':
            s.pop()
        elif char == ')' and s.peek() == '(':
            s.pop()
        elif char == ']' and s.peek() == '[':
            s.pop()
        else:
            s.push(char)  # else, add to the stack.

    return s.is_empty()  # if balanced, stack should be empty


test_case_1 = '{}'  # balanced
test_case_2 = '{{[]}()}'  # balanced
test_case_3 = '{{[}'  # unbalanced
test_case_4 = '{[}]}'  # unbalanced
test_case_5 = '{()(){()(){}}}'  # balanced


assert is_balanced(test_case_1) == True
assert is_balanced(test_case_2) == True
assert is_balanced(test_case_3) == False
assert is_balanced(test_case_4) == False
assert is_balanced(test_case_5) == True
print('All test cases passed.')
