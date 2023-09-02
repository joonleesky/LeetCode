## Python Basic

### String Manipulation

```
# l = [('a', 5, 'd'), ('b', 3, 'e'), ('b', 5, 'c')]
# sort a list based on the order of second then third elements. 
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
- Access: O(1): directly access by address
- Insert: O(n): requires moving all the elements in the memory
- Delete: O(n): requires moving all the elements in the memory
- Edit: O(1): access then change the value

#### Two-pointer technique

- O(n) time complexity to compute the sum of sub-arrays
- LeetCode: 0015-3sum, 0042-trapping-rain-water
```
left_idx = 0, right_idx = 1
while True:
  # do something
  right_idx += 1
```

### Linked-List

#### Time Complexity 
- Access: O(n): requires traverse
- Insert: O(1): just insert on the head node
- Delete: O(n): requires traverse
- Edit: O(n): requires traverse
```

```
```
