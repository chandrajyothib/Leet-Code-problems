class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs is None:
            return ""

        pre=strs[0]
        for i in strs[1:]:
            while i.find(pre)!=0:
                pre=pre[:-1]
                if pre is None:
                    return ""
        return pre
                
o=Solution()
print(o.longestCommonPrefix(["float","flower","flow"]))