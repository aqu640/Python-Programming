"""
# leetcode
# 14. Longest Common Prefix

strs[0]  => flower
strs[1:] => ['flow', 'flight']

"""
def longestCommonPrefix(strs):

        for i in range( len(strs[0]) ): # 第一個單字的長度
            for string in strs[1:]:     # 第1個~end
                if i >= len(string) or string[i] != strs[0][i]:
                                        # 當i>比較字串長度 或 flower 比較到字母不同 回傳到當下字母
                    return strs[0][:i]
        return strs[0]                  # 檢查 strs=[""] 時 不回傳null 需回傳"" 也就是第一個[""]
    
strs = ["flower","flow","flight"]
#strs= [""]
longestCommonPrefix(strs)











#　有 print 版
# def longestCommonPrefix(strs):
#     for i in range( len(strs[0]) ): # 第一個單字的長度
#         print("i = ",i)

#         for string in strs[1:]:     # 第1個~end
#             if i >= len(string) or string[i] != strs[0][i]:
#                 print("strs[0][:i] = ",strs[0][:i])
#                 return strs[0][:i]
#     print("strs[0] = ",strs[0])

