class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        dict = {'(' : ')', '[' : ']', '{' : '}'}
        s = []
        for i in s:
            if i in dict.keys():
                s.append(i)
            else:
                if s == []:
                    return False
                a = s.pop()
                if i!= dict[a]:
                    return False
        if(s==[]):
            return True
        else:
            return False 
    
o=Solution()
print(o.isValid("{(])}"))
    
    
    
    
    
    
     # curl=square=flo=0
        # for i in range(len(s)):
        #     if(s[i]=="(" or s[i]==")"):
        #         curl+=1
        #     elif(s[i]=="{" or s[i]=="}"):
        #         flo+=1
        #     elif(s[i]=="[" or s[i]=="]"):
        #         square+=1
        #     else:
        #         print("Not valid")
        # if(curl%2==0 and flo%2==0 and square%2==0):
        #     return True
        # else:
        #     return False
            
        