"""
Functions
def function_name(parameter1, parameter2, parameter3 ...):
    code
    return ans_1, ans_2 [optional]
"""


def hello():
    print('hello world')
    print('i am inside function')


# parameters
def full_name(first_name, last_name, middle_name=None):
    if middle_name is None:
        return first_name + ' ' + last_name
    # print('in middle name case')
    return first_name + ' ' + middle_name + ' ' + last_name
    # unreachable code
    # print('hello')


# argument
print(full_name('anish', 'sachdeva'))
print(full_name('ada', 'lovelace', 'countess of'))
print(full_name('alan', 'turing'))
print(full_name('john', 'doe'))

print(full_name(last_name='mozart', first_name='wolfgang', middle_name='amadeus'))
print(full_name('wolfgang', middle_name='amadeus', last_name='mozart'))

print('hello world', end=' ** ')
