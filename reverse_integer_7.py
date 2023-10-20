class Solution:
    def reverse(self, x: int) -> int:
            s = 0
            negative = False
    
            if x < 0:
                negative = True
                x = -x
            
            while x:
                r = x % 10
                s = s * 10 + r
                x = x // 10
            
            if negative:
                s = -s
            
            if s > -2**31 and s < 2**31 - 1:
                return s
            return 0

       
