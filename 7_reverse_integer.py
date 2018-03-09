class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=(x>0)-(x<0)      #找出x为正还是为负
        r=int(str(x*s)[:,:,-1])    #为什么要int str
        return r*s if r<(2**32) else 0    
