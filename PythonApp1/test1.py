string = "str"   # type = str
string1 = 'str1'   # type = str
doc = """ documentation """   # type = str
doc = ''' documentation '''   # type = str

print(type(doc))  

s = "s\np\ta\nbbb"   # \n - следующая строка, \t - сдвиг вправо

print(s)

r = r"C:\SDA2''\ASD\SD"   # это сырая строка - он выводит всё как есть в строке

print(r)   # C:\SDA2''\ASD\SD

byte = b"wow"   # преобразование в байт код 

print(type(byte))   # bytes

combine = string + string1   # обьединяет строки в единую строку
mult = string * 3   # повторяет текст строки несколько раз в единую строке

print(combine)   # strstr1
print(mult)   # strstrstr
print(string[0])   # получение элемента из строки по индексу - s
print(string[0:2:1])   # это срез. Он включает в себя несколько параметров [start, end, step] - st
print(len(string))   # определяет количество элементов в строке - 3
print(doc.find("t"))  # 8 ищет необходимый элемент
print(doc.find("t", 9))  # 10 ищет необходимый элемент
print(doc.rfind("t"))  # 10 ищет необходимый элемент начиная поиск с конца
print(doc.index("t"))  # 8 ищет необходимый элемент
print(doc.rindex("t"))  # 10 ищет необходимый элемент начиная поиск с конца
print(doc.replace("ment", "pip8")) # docupip8ation - замена элемента в строке
print(string.split("st"))  # разделяет строку
print("2ф".isdigit())  # False - проверяет является ли строка - числом
print(string.isalpha())  # True - проверка на наличие алфавита
print("2fsdsd".isalnum()) # True - состоит ли строка из чисел и букв
print(string.islower())  # состоит ли буквы в нижнем регистре  - True
print("STR".isupper())  # состоит ли буквы вверхнем регистре - True
print("\n".isspace())  # состоит ли специальные симловы \n в строке - True
print(string.upper())  # сделать строку в вверхнем регистре - STR
print(string.lower())  # сделать строку в нижнем регистре - str
print(string)
