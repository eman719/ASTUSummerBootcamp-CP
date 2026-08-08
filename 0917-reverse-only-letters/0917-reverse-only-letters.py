class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s_list=list(s)
        l=0
        right=len(s)-1
        for i in range(len(s_list)):
            while l<right:
                if s_list[l] not in char:
                    l+=1
                elif s[right] not in char:
                    right-=1
                else: 
                    s_list[l], s_list[right] = s_list[right], s_list[l]
                    l+=1
                    right-=1
        return "".join(s_list)


        