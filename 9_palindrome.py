class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        b=len(str(x))-1      #注意-1
        range=b**10
        r=x
        
        while range>=1:      
            k=r%10                      #提取出整数的最后一位
            r=(r-k)/10     
            l=(x//range)%10             #提取出整数的第一位   %10是为了每次循环提取对应digit的数字而不是前几位数字
            if l!=k:
                return False
            range/=10
        return True
