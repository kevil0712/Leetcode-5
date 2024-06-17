class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Trim leading and trailing spaces
        s = s.strip()
        
        # Step 2: Split the string into words using spaces as delimiters
        words = s.split()
        
        # Step 3: Reverse the list of words
        words.reverse()
        
        # Step 4: Join the reversed list of words with a single space
        reversed_string = ' '.join(words)
        
        return reversed_string
