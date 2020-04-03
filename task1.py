# методами строк очистить текст от знаков препинания
a=open("text.txt","r",encoding = "utf-8")
f=a.read()
print(f)
b=",",".", "?","!", ":"
f = f.replace("..", " ")
f = f.replace(",", " ")
f = f.replace(".", " ")
f = f.replace("?", " ")
f = f.replace("!", " ")
f = f.replace( ":", " ")
f = f.replace( ";", " ")
f = f.replace( "—", " ")
print(f)


# сформировать list со словами (split);

list_f = f.rsplit()
print(list_f)

# привести все слова к нижнему регистру (map);
list_f = list(map(str.lower, list_f))
print(list_f)

#получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
text_dict = {}
for b in list_f:
    text_dict[b] = list_f.count(b)
print(text_dict)

#вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).

list_f1 = list(text_dict.items())
list_f1.sort(key=lambda i: i[1])
print(list_f1)
list_f1.reverse()
print(list_f1[:5])

text_set=set(list_f1)
print(len(text_set))
