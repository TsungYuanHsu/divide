# Make decorator to add condition judge without changing divide function

def judge(func):
    def inner(n, d):
        if d == 0:
            return 0
        else:
            return func(n, d)
    return inner

@judge
def divide(n, d):
    return n / d

print('We are calculating n / d')
n = int(input('Please input n: '))
d = int(input('Please input d: '))
# divide = judge(divide)
print('n / d is', divide(n, d))