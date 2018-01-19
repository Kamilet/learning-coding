'''
判断两个函数输出是否相同。
如果相同，返回(第一个函数的值,same)
如果不同，返回(第一个函数的值,different)
如果第一个返回错误，返回(第二个函数的值,第一个函数名_error)
第二个错误同上
两个都错误，返回(NONE, both_error)
'''

def checkio(f,g):

    def h(*args,**kwargs):
        try:
            return_f = f(*args,**kwargs)
            if return_f == None:
                return_f = '_error'
        except:
            return_f = '_error'
        try:
            return_g = g(*args,**kwargs)
            if return_g == None:
                return_g = '_error'
        except:
            return_g = '_error'
        if return_g == '_error' and return_f == '_error':
            return (None, 'both_error')
        elif return_g == '_error' and return_f != '_error':
            return (return_f, 'g_error')
        elif return_g != '_error' and return_f == '_error':
            return (return_g, 'f_error')
        else:
            if return_g == return_f:
                return (return_f, 'same')
            else:
                return (return_f, 'different')

    return h

if __name__ == '__main__':
       
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    # (x+y)(x-y)/(x-y)
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,3)==(4,'same'), "Function: x+y, first"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,2)==(3,'same'), "Function: x+y, second"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1.01)==(2.01,'different'), "x+y, third"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1)==(2,'g_error'), "x+y, fourth"

    # Remove odds from list               
    f = lambda nums:[x for x in nums if ~x%2]
    def g(nums):
      for i in range(len(nums)):
        if nums[i]%2==1:
          nums.pop(i)
      return nums 
    assert checkio(f,g)([2,4,6,8]) == ([2,4,6,8],'same'), "evens, first"
    assert checkio(f,g)([2,3,4,6,8]) == ([2,4,6,8],'g_error'), "evens, second"         
    
    # Fizz Buzz    
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (6)==('Fizz','same'), "fizz buzz, first"      
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (30)==('Fizz Buzz','same'), "fizz buzz, second"
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (7)==('7','different'), "fizz buzz, third"
