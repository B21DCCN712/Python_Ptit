def is_valid(s, target):
    try:
        result = eval(s)
        return result == target
    except:
        return False

def Try(nums, target):
    n = len(nums)
    expressions = []

    def backtrack(index, s):
        if index == n:
            if is_valid(s, target):
                expressions.append(s)
            return

        for operator in ["+", "-", "*"]:
            if nums[index]<0:next = s + operator + '('+ str(nums[index]) +')'
            else: next = s + operator + str(nums[index])
            backtrack(index + 1, next)
    if(nums[0] >=0): x=str(nums[0])
    else: x= '('+str(nums[0])+')'
    backtrack (1, x)
    return expressions

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

expressions = Try(numbers, m)

if expressions:
    for exp in expressions:
        print(exp + f"={m}")
else:
    print("IMPOSSIBLE")
