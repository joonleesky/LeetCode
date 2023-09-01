# Lesson
# For sorting with keys, use python sorted() function with lambda
# l = [('a',5), ('b',3)]
# sorted(l, key=lambda x:x[1]) -> sorted based on numeric order

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        # letter logs require re-ordering
        letter_logs =[]

        # digit logs do not require ordering
        digit_logs = []
        
        for log in logs:
            _log = log.split(' ')
            identifier = _log[0]
            contents = _log[1:]
            
            if contents[0].isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
                
        # sort by lexicographical order
        letter_logs = sorted(letter_logs, key=lambda x:(x.split()[1:], x.split()[0]))
        
        # digit logs followed by letter logs
        logs = letter_logs + digit_logs
        
        return logs
            
            
            
            
            