#!/usr/bin/python3

import subprocess

def ececutecommand(path_to_image):
	command = 'strings'

	temporary = subprocess.Popen([command, path_to_image], stdout = subprocess.PIPE)

	result = str(temporary.communicate())
	return result

path_to_image = input("give us .svg file path :")
content = ececutecommand(path_to_image)

content_list = content.split(" ")

# for i in content_list:
# 	print(i,"    ->", content_list.index(i))

id_1 = content_list[461][-1]
id_2 = content_list[507][-1]
id_3 = content_list[553][-1]
id_4 = content_list[599][-1]
id_5 = content_list[645][-1]
id_6 = content_list[691][-1]
id_7 = content_list[737][-1]
id_8 = content_list[738:744]
id_9 = content_list[789][-1]
id_10 = content_list[790:801]

string1 = ''.join([id_1, id_2, id_3, id_4, id_5, id_6, id_7])
string2 = ''.join(id_8)
string3 = ''.join(id_10)

print(string1 + string2 + id_9 + string3 + "}")