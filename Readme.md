## Python Basic

### String Manipulation

```
# l = [('a', 5, 'd'), ('b', 3, 'e'), ('b', 5, 'c')]
# Sort a list based on the order of second and then third elements. 
sorted(l, key=lambda x:(x[1], x[2])) 
```

```
# is alphabetical or numeric
word.isalnum()
```

```
# remain alphabets
str = re.sub(r'[^a-z^A-Z]', ' ', str)
```

```
# check the existence of the anagram (i.e., permutation)
anagram = {}
_word = ''.join(sorted(word))
_word in anagram
```

## Linear Data Structure

### Array

#### Time Complexity 
- Access: O(1): directly access by address.
- Insert: O(n): requires moving all the elements in the memory.
- Delete: O(n): requires moving all the elements in the memory.
- Edit: O(1): access then change the value.

#### Two-pointer technique

- O(n) time complexity to compute the sum of sub-arrays.
- Commonly used in an ordered array.
- Obviously, this technique cannot be used in a singly linked list.
- LeetCode: 0015-3sum, 0042-trapping-rain-water.
```
left_idx = 0, right_idx = len(arr)-1
while True:
  # do something
  left_idx += 1
  right_idx -= 1
```

#### Sliding-window technique

- O(n) time complexity to compute the sum of sub-arrays.
- Commonly used in an un-ordered array.

### Linked-List

#### Time Complexity 
- Access: O(n): requires traverse.
- Insert: O(1): just insert on the head node.
- Delete: O(n): requires traverse.
- Edit: O(n): requires traverse.

#### Tips

- Given the head, it is good to generate a root node at the beginning
```
root = ListNode()
root.next = head
```

### Stack

#### When to use

- Parentheses or bracket matching.
- Backtracking.
- Evaluating postfix/prefix expressions.
- DFS.

#### Time Complexity

- Insertion at the beginning: not typically supported (If implemented, array: O(n), linked list: O(1)).
- Insertion at the end: O(1).
- Deletion at the beginning: not typically supported (If implemented, array: O(1)).
- Deletion at the end: O(1).
- 
### Queue

#### When to use

- Problems related to order or sequence.
- Level order traversal in trees.
- BFS.

#### Time Complexity

- Insertion at the beginning: not typically supported (If implemented, array: O(n), linked list: O(1)).
- Insertion at the end: O(1).
- Deletion at the beginning: O(1).
- Deletion at the end: Not typically supported (If implemented, array: O(n), linked list: O(1) if a tail pointer is maintained).

### Deque

#### When to use Deque

- Sliding window problems (when you want to add/remove elements from both ends).
- Palindrome checking.
- Default (when the problem is ambiguous to select either stack or queue, just use deque).

#### Time Complexity

- Insertion at the beginning: O(1) on average, O(n) in the worst case for array, O(1) for linked list.
- Insertion at the end: O(1) on average, O(n) in the worst case for array, O(1) for linked list.
- Deletion at the beginning: O(1).
- Deletion at the end: O(1).

#### Tips 

- Use collections.deque()

### Hash Map

hash_map = dict()
hash_map = collections.defaultdict()

#### Time Complexity

- Write it later.

## Non-Linear Data Structure

### Graph
- Graph consists of Vertices (i.e., Nodes) and Edges, G=(V, E).
- Vertices are commonly represented with a list.
- Edges are commonly represented with a dictionary.

### Tree
- A tree is an acyclic undirected graph (i.e., no cycle structure).

#### Binary Search Tree
- A tree with every right node's value is greater than the left node's value.
- Insertion (avg): O(logN).
- Insertion (worst): O(logN).
- Find any: O(logN).
- Find max: O(1).
  - Common misconception is O(logN).
  - We can simply modify the BST algorithm to track the largest.
- Deletion: O(logN).

#### Heap
- A tree with every parent node's value is greater than the child node's value.
- Heap is a complete binary tree.
- Insertion (avg): O(1).
  - Generally, most of the nodes will be located in the bottom.
  - Although not widely recognized, this is the major benefit of Heap!
- Insertion (worst): O(logN).
- Find any: O(N).
- Find max: O(1).
- Deletion: O(logN).

```
import heapq
heapq.heappush(item)
heapq.heappop()
```

#### Trie
- A tree structure for comparing strings.
- 

### Search

#### BFS
- Starts at the root node and explores all nodes at the present depth then moves on to the next depth.
- Commonly implemented with queue.

#### DFS 
- Starts at the root node and explores all nodes at the present depth then moves on to the next depth.
- Commonly implemented with stack.
- Pre-order-traverse: center->left->right.
- In-order-traverse: left->center->right (ascending order in BST).
- Post-order-traverse: left->right->center.

#### In-order Traverse
- left -> center -> right

#### Post-order Traverse
- left -> right -> center

#### Dijkstra
- Algorithm for finding the shortest path with positive distance between each node.
- Dijkstra can be interpreted as BFS + jump-in-queue.
- For each node, Dijkstra explores all nodes at the present depth and then selects the node with the smallest total distance.
- Commonly implemented with a priority queue (to select the node with the smallest distance).

## Algorithms

### Sorting

#### Bubble-Sort
```
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

#### Quick Sort
- average time complexity: O(nlogn).
- worst time complexity: O(n^2).
  - The smallest or the largest pivot is selected.
- space complexity: None (just in-place operation).

```
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

#### Merge Sort
- average time complexity: O(nlogn).
- worst time complexity: O(nlogn).
- space complexity: O(n) (merged array should be kept).

```
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged
```

## Math

### Finding GCD (Euclidean algorithm)

- GCD of x & y only exists within max(x,y) - min(x,y).

