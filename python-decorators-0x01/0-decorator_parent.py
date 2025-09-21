def parent(num):
    def first_child():
        return ('This is Kate.')
    
    def second_child():
        return 'This is Chinedu.'
    
    # desired objects returned as value of parent function
    if num == 1:
        return first_child
    else:
        return second_child

#print(first_child)
first = parent(1)
second = parent(2)
print(first)
print(first())
print(second)
print(f'{second}()')