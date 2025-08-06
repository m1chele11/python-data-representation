

#3
def frequencyCount(A):
    #make dict to store frequencies  which will be in (O| A| )
    freq = {}
    for i in A:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    #Convert the dictionary to a list of tuples (O(|A|))
    freq_list = list(freq.items())
    # sort the list of tuples by element value (O(|A| log2 |A|))
    freq_list.sort()

    return freq_list

A = [5, 3, 7, 5, 5, 1, 2, 10, 3, 3, 3, 2, 3, 4, 7, 1, 1]

result = frequencyCount(A)
print(result)

def tests():
    test_cases = [
        [],
        [1],
        [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [5, 3, 7, 5, 5, 1, 2, 10, 3, 3, 3, 2, 3, 4, 7, 1, 1]
    ]

    for i, test in enumerate(test_cases, 1):
        result = frequencyCount(test)
        print(f"Test case{i}: {result}" )

#tests()


#4 
def shuffle(l1, l2):
    #init the shuffled array
    shuffled = []
    #find the min length of the 2 lists
    min_length = min(len(l1), len(l2))
    for i in range(min_length):
        shuffled.append(l1[i])
        shuffled.append(l2[i])
    
    #add remeaning elements of shorter list to the longer list
    if len(l1) > len(l2):
        shuffled.extend(l1[min_length:])
    elif len(l2) > len(l1):
        shuffled.extend(l2[min_length:])

    return shuffled

l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c']
result = shuffle(l1, l2)
print(result)


#5
def mergeSort(A):
    # Helper function to merge two sorted lists
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # add left overs to end 
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # Treat each element as a sorted list and init a queue
    queue = [[x] for x in A]

    # merge lists in the queue
    while len(queue) > 1:
        merged_queue = []
        for i in range(0, len(queue), 2):
            if i + 1 < len(queue):
                merged_queue.append(merge(queue[i], queue[i + 1]))
            else:
                merged_queue.append(queue[i])
        queue = merged_queue

    #fully merged and sorted list
    return queue[0] if queue else []


A = [38, 27, 43, 3, 9, 82, 10]
sorted_A = mergeSort(A)
print(sorted_A)

def tests5():
    test_cases5 = [
        [],
        [1],
        [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [5, 3, 7, 5, 5, 1, 2, 10, 3, 3, 3, 2, 3, 4, 7, 1, 1]
    ]

    for i, test5 in enumerate(test_cases5, 1):
        result5 = mergeSort(test5)
        print(f"Test case{i}: {result5}" )
#tests5()

#6
def freqCountHash(A):
    #Inittialize table with 7 butckets
    hash_table = [[] for i in range(7)]

    #populate hash table
    for num in A:
        bucket_index = num % 7
        found = False
        for j, (key, count) in enumerate(hash_table[bucket_index]):
            if key == num:
                hash_table[bucket_index][j] = (key, count + 1)
                found = True
                break
        if not found:
            hash_table[bucket_index].append((num, 1))

    #Collect freq counts from the table
    result = []
    for bucket in hash_table:
        result.extend(bucket)

    return sorted(result)

A = [5, 3, 7, 5, 5, 1, 2, 10, 3, 3, 3, 2, 3, 4, 7, 1, 1]
frequency_counts = freqCountHash(A)
print(frequency_counts)

def tests6():
    test_cases6 = [
        [],
        [1],
        [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [5, 3, 7, 5, 5, 1, 2, 10, 3, 3, 3, 2, 3, 4, 7, 1, 1]
    ]

    for i, test6 in enumerate(test_cases6, 1):
        result6 = freqCountHash(test6)
        print(f"Test case{i}: {result6}" )

#tests6()

#7

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Part A: Descendants function
def Descendant(element, tree):
    def collect_descendants(node):
        if not node:
            return []
        descendants = [node.value]
        descendants += collect_descendants(node.left)
        descendants += collect_descendants(node.right)
        return descendants

    def find_node(node):
        if not node:
            return None
        if node.value == element:
            return node
        return find_node(node.left) or find_node(node.right)

    target_node = find_node(tree)
    if not target_node:
        return []  
    return collect_descendants(target_node)

# Part B: Ancestors function
def Ancestors(element, tree):
    def find_ancestors(node, path):
        if not node:
            return None
        if node.value == element:
            return path + [node.value]
        left_path = find_ancestors(node.left, path + [node.value])
        if left_path:
            return left_path
        return find_ancestors(node.right, path + [node.value])

    result = find_ancestors(tree, [])
    return result if result else []  


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Find descendants of 2
descendants = Descendant(2, root)
print("Descendants of 2:", descendants)

# Find ancestors of 5
ancestors = Ancestors(5, root)
print("Ancestors of 5:", ancestors)



#8
#reuse the TreeNode class


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node:
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(node, value):
            if not node:
                return False
            if value == node.value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)

    def inorder(self):
        def _inorder(node):
            if not node:
                return []
            return _inorder(node.left) + [node.value] + _inorder(node.right)

        return _inorder(self.root)

# Part A: Intersection
def Intersect(A, B):
    bst = BST()
    for a in A:
        bst.insert(a)

    intersection = []
    for b in B:
        if bst.search(b):
            intersection.append(b)

    return intersection

# Part B: Difference
def Difference(A, B):
    bst = BST()
    for b in B:
        bst.insert(b)

    difference = []
    for a in A:
        if not bst.search(a):
            difference.append(a)

    return difference

# Part C: Equal Set
def equalSet(A, B):
    bstA = BST()
    bstB = BST()

    for a in A:
        bstA.insert(a)
    for b in B:
        bstB.insert(b)

    return sorted(bstA.inorder()) == sorted(bstB.inorder())



A = [1, 5, 2, 7, 9]
B = [2, 5, 9, 1, 7]


print("Intersection:", Intersect(A, B))

print("Difference:", Difference(A, B))


print("Equal Set:", equalSet(A, B))



#9
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def isIn(self, element):
        index = self._hash(element)
        return element in self.table[index]

    def Insert(self, element):
        if not self.isIn(element):
            index = self._hash(element)
            self.table[index].append(element)

    def Delete(self, element):
        if self.isIn(element):
            index = self._hash(element)
            self.table[index].remove(element)

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# test cases based on specified parameters in the homework
def run_test():
    test_cases = {
        3: [  # For p = 3
            [],
            [1],
            [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            [5, 3, 7, 5, 5, 1, 2, 10, 3, 3, 2, 3, 4, 7, 1, 1],
            [7, 6, 6, 3, 9, 3, 2, 4, 8, 10, 7, 5, 1, 5, 1, 5, 3, 2, 3, 3, 3, 3, 1, 2],
        ],
        5: [  # For p = 5
            [],
            [1],
            [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            [5, 3, 7, 5, 5, 1, 2, 10, 3, 3, 2, 3, 4, 7, 1, 1],
            [7, 6, 6, 3, 9, 3, 2, 4, 8, 10, 7, 5, 1, 5, 1, 5, 3, 2, 3, 3, 3, 3, 1, 2],
        ],
    }

    for p, cases in test_cases.items():
        print(f"\nRunning tests for p = {p}:")
        for i, elements in enumerate(cases):
            print(f"\nTest Case {i + 1} with A = {elements}")
            hash_table = HashTable(p)

            # Insert elements
            for elem in elements:
                hash_table.Insert(elem)

            print("Hash Table after Insertions:")
            hash_table.display()

            # Check elements 1, 4, 8, 9, 10 using isIn
            for check in [1, 4, 8, 9, 10]:
                print(f"Is {check} in the table?", hash_table.isIn(check))

            # Delete elements at odd positions
            print("\nDeleting elements at odd positions:")
            for idx, elem in enumerate(elements):
                if idx % 2 == 0:  # Odd index (0-based)
                    hash_table.Delete(elem)

            print("Hash Table after Deletions:")
            hash_table.display()
run_test()






# Bonus (BST with Hash Table)
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, element):
        return element % self.size

    def isIn(self, element):
        index = self._hash(element)
        return element in self.table[index]

    def insert(self, element):
        index = self._hash(element)
        if element not in self.table[index]:
            self.table[index].append(element)

    def delete(self, element):
        index = self._hash(element)
        if element in self.table[index]:
            self.table[index].remove(element)




A = [1, 5, 2, 7, 9]
B = [2, 5, 9, 1, 7]


print("Intersection:", Intersect(A, B))


print("Difference:", Difference(A, B))


print("Equal Set:", equalSet(A, B))


hash_table = HashTable(7)
hash_table.insert(10)
hash_table.insert(20)
print("Is 10 in table:", hash_table.isIn(10))
hash_table.delete(10)
print("Is 10 in table after deletion:", hash_table.isIn(10))