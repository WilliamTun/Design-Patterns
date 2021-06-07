
'''
Unfinished
'''
class Node:
    def __init__(self, value, left=None, right=None):
        self.value
        self.left = left
        self.right = right

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

class InOrderIterator:
    def __init__(self, root):
        self.root = self.current = root
        self.yielded_start = False

        while self.current.left:
            self.current = self.current.left



if __name__ == '__main__':
    '''
    1 
   / \ 
  2   3
    '''

    # in-order: 213
    # preorder: 123
    # postorder: 231

    root = Node(1, left=Node(2),right=Node(3))
