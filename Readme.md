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

#### Multiple Assignment

- Multiple assignment allows to link nodes without generating temp.

```
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

rev, rev.next, node = node, rev, node.next
```
#### Tips

- Given the head, it is good to generate a root node at the beginning
```
root = ListNode()
root.next = head
```

### Stack & Queue & Deque

#### When to use Stack

- Parentheses or bracket matching.
- Backtracking.
- Evaluating postfix/prefix expressions.
- DFS.

#### When to use Queue

- Problems related to order or sequence.
- Level order traversal in trees.
- BFS.

#### When to use Deque

- Sliding window problems (when you want to add/remove elements from both ends).
- Palindrome checking.
- Default (when the problem is ambiguous to select either stack or queue, just use deque).
