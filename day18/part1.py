# Smells like binary trees.

class DataReader:
    def __init__(self, data: str):
        self.data = data
        self.index = 0

    def next_token(self):
        c = self.data[self.index]
        self.index += 1
        if c == '[' or c == ']' or c == ',':
            return c
        else:
            # Input numbers are <= 9
            return int(c)


class SnailNumber:
    def __init__(self, data: DataReader = None, parent = None):
        self.parent = parent
        if data != None:
            c = data.next_token()
            if c == '[':
                self.type = 'p'
                self.left = SnailNumber(data, self)
                assert data.next_token() == ','
                self.right = SnailNumber(data, self)
                assert data.next_token() == ']'
            else:
                self.type = 'n'
                self.value = c

    def __repr__(self):
        if self.type == 'n':
            return str(self.value)
        else:
            return f'[{self.left},{self.right}]'

    def left_neighbour(self):
        node = self
        # Go up until you're the right child.
        while True:
            # If you've gone beyond the root of the tree, there is no left neighbour.
            if node.parent == None:
                return None
            # Otherwise, keep going.
            if node.parent.left == node:
                node = node.parent
            else:
                break

        # Use the left child.
        node = node.parent.left

        # Then follow right children until you hit a value.
        while node.type == 'p':
            node = node.right

        return node

    def right_neighbour(self):
        node = self
        # Go up until you're the left child.
        while True:
            # If you've gone beyond the root of the tree, there is no right neighbour.
            if node.parent == None:
                return None
            # Otherwise, keep going.
            if node.parent.right == node:
                node = node.parent
            else:
                break

        # Use the right child.
        node = node.parent.right
        
        # Then follow left children until you hit a value.
        while node.type == 'p':
            node = node.left

        return node

    def plus(self, other):
        result = SnailNumber()
        result.set_children(self, other)
        return result

    def set_value(self, value: int):
        self.type = 'n'
        self.value = value

    def set_children(self, left, right):
        self.type = 'p'
        self.left = left
        left.parent = self
        self.right = right
        right.parent = self

    def find_deep_pair(self, depth):
        if self.type == 'p':
            if depth == 4:
                return self

            retval = self.left.find_deep_pair(depth + 1)
            if retval != None:
                return retval

            return self.right.find_deep_pair(depth + 1)
        else:
            return None

    def explode(self):
        left_neighbour = self.left_neighbour()
        if left_neighbour != None:
            left_neighbour.value += self.left.value

        right_neighbour = self.right_neighbour()
        if right_neighbour != None:
            right_neighbour.value += self.right.value

        replacement = SnailNumber()
        replacement.set_value(0)

        replacement.parent = self.parent        
        if self.parent.right == self:
            self.parent.right = replacement
        else:
            self.parent.left = replacement
                
    def find_split(self):
        if self.type == 'n':
            if self.value > 9:
                return self
            return None
        else:
            retval = self.left.find_split()
            if retval != None:
                return retval
            return self.right.find_split()

    def split(self):
        left = SnailNumber()
        left.set_value(self.value // 2)
        right = SnailNumber()
        right.set_value((self.value + 1) // 2)

        replacement = SnailNumber()
        replacement.set_children(left, right)

        replacement.parent = self.parent
        if self.parent.right == self:
            self.parent.right = replacement
        else:
            self.parent.left = replacement

    def magnitude(self):
        if self.type == 'n':
            return self.value
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()


with open('day18/input.txt', 'r') as f:
    number = SnailNumber(DataReader(f.readline().strip()))
    for line in f:
        number = number.plus(SnailNumber(DataReader(line.strip())))
        action_taken = True
        while action_taken:
            action_taken = False
            explode_node = number.find_deep_pair(0)
            if explode_node != None:
                # Figure out exploding.
                explode_node.explode()
                action_taken = True
            else:
                # Note: This code is wrong; it'll split everything, and it doesn't update action_taken.
                split_node = number.find_split()
                if split_node != None:
                    split_node.split()
                    action_taken = True
        
    print(number.magnitude())
