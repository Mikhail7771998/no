def make_negative(x):
    if x>0:
        return x*(-1)
    else:
        return x

print(make_negative(3))
print(make_negative(0))
print(make_negative(-2))



def between(a,b):
    return list(range(a,b+1)) 

print(between(1,4))
print(between(2,3))
print(between(0,5))



def repeat_str(i,h):
    return i*h

print(repeat_str(2, 'hello'))
print(repeat_str(5, 'любовь ручки и карндаша'))
print(repeat_str(3, 'нет'))



def find_average(r):
    return sum(r)/len(r)

print(find_average([1,2,3,5]))
# print(find_average([]))
print(find_average([7,7,7]))



def bool_to_word(k):
    if k == True:
        return "yes"
    elif k == False:
        return "no"
        
print(bool_to_word(True))
print(bool_to_word(False))
print(bool_to_word(True))



def update_light(l):
    if l == "green":
        return "yellow"
    elif l == "yellow":
        return "red"
    elif l == "red":
        return "green"

print(update_light("green"))
print(update_light("yellow"))
print(update_light("red"))



def century(f):
    if f % 100 == 0:
        return f//100
    else:
        return f//100+1


print(century(1705))
print(century(1900))
print(century(89))



def generate_shape(v):
    for i in range(v):
        print("+"*v)

print(generate_shape(2))
print(generate_shape(3))
print(generate_shape(0))
