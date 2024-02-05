a = input()
g = len(a)
print(g)
if g==0:
    print ('вы нечего не ввели,попробуйте снова')

elif g<4 and g>0:
    print('слишком короткое название')

elif g<7 and g>=4:
    print ('идеальное название')

else:
    print ('слишком длиное название')