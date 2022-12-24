# import collections

class Node:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        # dir name -> Node
        self.children = {}
    
    def getOrAddChild(self, childNodeName, size):
        if childNodeName in self.children:
            return self.children[childNodeName]
        else:
            newChild =  Node(childNodeName, size, self)
            self.children[childNodeName] = newChild
        return self.children[childNodeName]
    
    def prettyPrint(self):
        print("Node "+self.name+", size:"+str(self.size)+", parent:")
        for child in self.children:
            print(self.children[child].name)
    
    def part1(self):
        if len(self.children) == 0:
            return self.size

        full_size = self.size
        for node_name in self.children:
            node_size = self.children[node_name].part1()
            full_size += node_size

        # if full_size <= 100000:
            # shortcut, just print it
            # print(full_size)
        return full_size

    def part2(self):
        if len(self.children) == 0:
            return self.size

        full_size = self.size
        for node_name in self.children:
            node_size = self.children[node_name].part2()
            full_size += node_size

        if full_size >= 3837783:
            print(self.name)
            print(full_size)
        return full_size


def read_input():
    lines = []
    with open('day7.txt', "r") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def execute_instruction(line, root_node, cur_node):
    no_dollar = line.replace('$ ', '')
    parts = no_dollar.split(' ')
    command = parts[0]

    if command != 'cd':
        # no-op for ls
        return cur_node
    
    new_cur = None
    dir_name = parts[1].strip()
    if dir_name == '/':
        new_cur = root_node
    elif dir_name == '..':
        new_cur = cur_node.parent
    else:
        new_cur = cur_node.getOrAddChild(dir_name, 0)

    return new_cur

def record_seen_artifact(line, cur_node):
    parts = line.split()
    if parts[0].strip() != 'dir':
        size = int(parts[0])
        file_name = parts[1]
        cur_node.getOrAddChild(file_name, size)
    # you don't have to do anything with the dir

def build_graph():
    lines = read_input()
    root_node = Node('/', 0, None)

    cur_node = root_node
    for line in lines:
        if line[0] == '$':
            cur_node = execute_instruction(line, root_node, cur_node)
        else:
            # it's a child dir or file of the cur_node
            record_seen_artifact(line, cur_node)
    return root_node


def main():
    root_node = build_graph()
    full_size = root_node.part1()
    part2 = root_node.part2()


if __name__ == "__main__":
    main()
