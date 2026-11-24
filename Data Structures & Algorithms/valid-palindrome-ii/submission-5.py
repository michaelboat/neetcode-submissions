class Solution:
    def validPalindrome(self, s: str) -> bool:

        i, j = 0, len(s)-1
        skipped = False

        def checksub(word) -> bool:
            
            i, j = 0, len(word)-1

            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        while i < j:
            if s[i] != s[j] and not skipped:
                print(s[i+1:j+1])
                print(s[i:j])
                return checksub(s[i+1:j+1]) or\
                checksub(s[i:j])
            i += 1
            j -= 1

        return True


        