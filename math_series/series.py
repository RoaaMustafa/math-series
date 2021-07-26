def fibonacci_series(number):
     """
    is a numeric series starting with the integers 0 and 1. In this series, 
    the next integer is determined by summing the previous two. This gives us:
    """
   
     if type(number) != int:
        return 'Invalid Input'
     # return 0 and 1 for first and second terms
     if number == 0:
        return 0

     elif number == 1:
        return 1
     else:
        # return the sum of two numbers
         return fibonacci_series(number - 1) + fibonacci_series(number - 2)

print(fibonacci_series(7))   
   
"""
start with the values 2 and 1 rather than 0 and 1
"""
def lucas_series(number):
      if number==0:
        return 2

      if number ==1:
        return 1

      if number>1:
        return  lucas_series(number-1)+lucas_series(number-2)


print(lucas_series(7)) 


"""
  The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced
"""
def sum_series(n,optional1=0,optional2=1):
    if optional1==0 and optional2==1:
        return fibonacci_series(n)
    elif optional1==2 and optional2==1:
        return lucas_series(n)
    else:
        return anotherSeries(n,optional1,optional2)



def anotherSeries(a,b,c):
    if a==0 : 
        return b
    if a== 1 : 
        return c
    else:
        return anotherSeries(a-1,b,c)+ anotherSeries(a-2,b,c)


print(sum_series(5,1,5)) #40
print(sum_series(5,0,1)) #5  same fibonacci
print(sum_series(5,2,1)) #11 same lucas