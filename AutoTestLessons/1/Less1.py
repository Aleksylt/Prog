import math

if __name__ == '__main__':

    fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
    print(fun(5))
