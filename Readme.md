### Python Basic

#### String Manipulation

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

### Linear Data Structure

#### Array

```
# l = [('a', 5, 'd'), ('b', 3, 'e'), ('b', 5, 'c')]
# sort a list based on the order of second then third elements. 
sorted(l, key=lambda x:(x[1], x[2])) 
```
