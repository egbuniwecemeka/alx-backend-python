"""  wrapper() has a reference to the original say_whee() as func, and it calls that function between the two calls to print() """

def decorator(func):
    def wrapper():
        print('Print before function runs')
        func()
        print('Print after function runs')
    return wrapper

def sample_text():
    print('Random text')

print('Original sample_text', sample_text) # -> Points to sample_text

# Applying decorators
sample_text = decorator(sample_text)

print('Decorated sample_text', sample_text) # -> Points to  wrapper
