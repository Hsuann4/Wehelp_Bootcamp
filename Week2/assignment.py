
'''Requirement 1'''

def calculate(min, max, step):
    sum = 0
    while max >= min:
        sum += min
        min += step
    print(sum)
    return sum
    

calculate(1, 3, 1) 
calculate(4, 8, 2) 
calculate(-1, 2, 2) 



'''Requirement 2'''


def avg (data):
    times = 0
    sum = 0
    for i in range(len(data["employees"])):
        if (data["employees"][i]["manager"]) == False:
            sum = sum + data["employees"][i]["salary"]
            times += 1
    result = sum / times
    print(result)   
    return result
    


avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":False
},
{
"name":"Bob",
"salary":60000,
"manager":True
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
})

  




'''Requirement 3'''

def func(a):
    def func_b(b,c):
        
        
        result = a + b * c
        print(result)
        return result
    return func_b




func(2)(3, 4) 
func(5)(1, -5) 
func(-3)(2, 9) 


def add(n1, n2):
    result= n1 + n2
    print(result)


   
'''Requirement 4'''

def maxProduct(nums):
    max = 0
    if len(nums) == 2:
        max = nums[0] * nums[1]
        return max
    for i in range(0, len(nums)-1):
        for j in range (i+1, len(nums)):
            product = nums[i] * nums[j]
            if product > max:
                max = product
    return max 


print(maxProduct([5, 20, 2, 6]) )
print(maxProduct([10, -20, 0, 3]))
print(maxProduct([10, -20, 0, -3]))
print(maxProduct([-1, 2]))
print(maxProduct([-1, 0, 2]))
print(maxProduct([5,-1, -2, 0]))
print(maxProduct([-5, -2]))



'''Requirement 5'''


from re import I


def twoSum(nums, target):

    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            product = nums[i] + nums[j]
            if product == target:
                result = []
                result.append(i)
                result.append(j)
    print (result)
    return result
                



twoSum([2, 11, 7, 15], 9)



    

