import os
#逐个打开文件
path = 'D:/pythonProject\STUDY/bishe/P'

path_list = os.listdir(path)

# path_list.remove('.DS_Store')

path_list.sort(key=lambda x: int(x.split('.')[0]))

print(path_list)

for filename in path_list:
    f = open(os.path.join(path, filename), 'rb')

