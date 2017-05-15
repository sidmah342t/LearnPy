
def division(p,q):
    return p/q
try:
    print('Enter dividend')
    p=int(input())
    print('Enter divisor')
    q=int(input())
    print('quotient of dividing'+ str(p) + 'by' + str(q))
    print(division(p, q))

except ZeroDivisionError:
    print('cannot divide by zero')

except ValueError:
    print('Cannot pass Letter or special characters')