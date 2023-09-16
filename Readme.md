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
- Obviously, this technique cannot be used in a singly linked list.
- LeetCode: 0015-3sum, 0042-trapping-rain-water.
```
left_idx = 0, right_idx = len(arr)-1
while True:
  # do something
  left_idx += 1
  right_idx -= 1
```

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

### Search

#### BFS
- Starts at the root node and explores all nodes at the present depth then moves on to the next depth.
- Commonly implemented with queue.

#### DFS
- Starts at the root node and explores all nodes at the present depth then moves on to the next depth.
- Commonly implemented with stack.

#### Dijkstra
- Algorithm for finding the shortest path with positive distance between each node.
- Dijkstra can be interpreted as BFS + jump-in-queue.
- For each node, Dijkstra explores all nodes at the present depth and then selects the node with the smallest total distance.
- Commonly implemented with a priority queue (to select the node with the smallest distance).
```
import heapq
heapq.heappush(item)
heapq.heappop()

```
