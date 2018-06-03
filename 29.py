class Solution:
    def divide(self, dividend, divisor):
        if dividend < -2**31 or dividend > 2**31-1 or divisor < -2**31 or divisor > 2**31-1:
            return 2**31-1
        if dividend == 0:
            return 0 
        else:
            flag = dividend * divisor
            flag = 1 if flag > 0 else -1
            dividend = abs(dividend)
            divisor = abs(divisor)
            result = 0
            c = 1
            con = divisor
            while dividend - divisor > 0:
                result += c
                c *= 2
                dividend = dividend - divisor
                divisor *= 2
            while dividend >= con:
                divisor /= 2
                c /= 2
                if dividend - divisor > 0 or dividend - divisor == 0:
                    result += c
                    dividend -= divisor


            """
            while dividend - divisor < 0:
                divisor /= 2
                c /= 2
            while dividend - divisor > 0 or dividend - divisor == 0:
                result += c
                c /= 2
                dividend = dividend - divisor
                if dividend < con:
                    break
                divisor /= 2 
                while dividend - divisor < 0:
                    divisor /= 2
                    c /= 2
            """
            if int(flag*result) < -2**31 or int(flag*result) > 2**31-1:
                return 2**31-1
            else:
                return int(flag*result)               
dividend = int(input())
divisor = int(input())
print(Solution().divide(dividend, divisor))