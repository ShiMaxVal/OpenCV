fil = open('settings_HSV.txt','r')  # открыть файл из рабочей директории в режиме чтения
str1 = fil.readline().split()
h1, s1, v1, h2, s2, v2 = [int(i) for i in str1]
print (v2)
fil.close()