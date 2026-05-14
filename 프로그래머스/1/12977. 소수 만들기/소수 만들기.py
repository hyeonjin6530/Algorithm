def solution(nums):
    answer = 0
    
    n = len(nums)

    def isPrime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if isPrime(nums[i] + nums[j] + nums[k]):
                    answer += 1
                
    return answer