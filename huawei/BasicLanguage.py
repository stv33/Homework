sample_set ={'Prince','Techs'}
print ('Data' in sample_set)
sample_set.add('Data')
print('Data'in sample_set)
print (len(sample_set)) #打印集合大小
sample_set.remove('Data')
print (len(sample_set))
sample_set = {'Prince','Techs','Prince'}
print(sample_set)
#集合元素遍历
for idx, word in enumerate(sample_set):
    print('#%d: %s' %(idx+1,word))
#集合推导式
from math import sqrt
nums = {int(sqrt(x)) for x in range(100) }
print (len(nums))
print (nums) #Prints "set[0,1,2,3,4,5])"


