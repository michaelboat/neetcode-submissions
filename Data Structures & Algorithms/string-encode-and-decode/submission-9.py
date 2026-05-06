class Solution:

    def encode(self, strs: List[str]) -> str:
        # length word before delimiter and then the delimeter
        # 4#neet4#code4#love3#you
        # 2#we3#say1#:3#yes
        coded = ""
        for word in strs:
            coded += word + "#" + str(len(word)) + "#"
        return coded

    def decode(self, s: str) -> List[str]:
        print(s)
        # encoded str: 4#neet4#code4#love3#you
        # neet#4#code#4#love#4#you#3#
        toReturn = []
        last = len(s) - 1

        while(last > 0):
            curr = last - 1
            while (s[curr] != '#'):
                curr -= 1
            print(s[curr+1: last])
            str_len = int(s[curr + 1: last])
            word_to_add = s[curr-str_len : curr]
            toReturn.append(word_to_add)
            last = curr-str_len-1
        # my list is reversed
        reversed_list = []
        for i in range(len(toReturn)-1, -1, -1):
            reversed_list.append(toReturn[i])
        # return list
        return reversed_list
        
            
