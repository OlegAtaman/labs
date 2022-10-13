def clearize(inp):
    switch = False
    first = ''
    second = ''
    for char in inp:
        if switch and char.isnumeric():
            second += char
        elif char.isnumeric():
            first += char
        elif first and char == ',':
            switch = True
    return int(first), int(second)


class Node:
    def __init__(self, code, price, left=None, right=None):
        self.code = code
        self.price = price
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, nodes):
        self.head = self.maketree(sorted(nodes, key=lambda x: x.code))

    def maketree(self, sorted_nodes):
        cur_node = sorted_nodes[len(sorted_nodes)//2]
        if len(sorted_nodes)//2 != 0:
            cur_node.left = self.maketree(sorted_nodes[:len(sorted_nodes)//2])
        if len(sorted_nodes)//2+1 < len(sorted_nodes):
            cur_node.right = self.maketree(sorted_nodes[len(sorted_nodes)//2+1:])
        return cur_node

    def calcprice(self):
        inp = input('Please, enter product id and count of items: ')
        p_id, p_count = clearize(inp)
        cur_node = self.head
        price = 0
        while True:
            if p_id < cur_node.code and cur_node.left:
                cur_node = cur_node.left
            elif p_id > cur_node.code and cur_node.right:
                cur_node = cur_node.right
            elif p_id == cur_node.code:
                price = cur_node.price
                break
            else:
                print('Wrong product code')
                break
        total_price = price * p_count
        ans = input('Do you want to add more products? (y/n): ')
        if ans == 'y':
            total_price += self.calcprice()
        return total_price

    def get_calc(self):
        out = self.calcprice()
        print(f'Total price is ${out}. Thanks for purchase!')


node5 = Node(5, 60)
node6 = Node(6, 50)
node7 = Node(7, 130)
node8 = Node(8, 1)
node1 = Node(1, 10)
node2 = Node(2, 15)
node3 = Node(3, 5)
node4 = Node(4, 100)


node_list = [node1, node2, node3, node4, node5, node6, node7, node8]

bt = BinaryTree(node_list)

bt.get_calc()