class Solution(object):
    def romanToInt(self, s):
        

        romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}

        pre_val=running_val=0
        for i in range(len(s)-1,-1,-1):          #注意这种写法
            int_val=romans[s[i]]         #注意用romans[s[i]]而不是s[i]
            if int_val<pre_val:
                running_val-=int_val
            else:
                running_val+=int_val
            pre_value=int_val                  #pre_val保持在int_val后面一个
        return running_val
        
