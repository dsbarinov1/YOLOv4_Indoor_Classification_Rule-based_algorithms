import os

ext = "jpg"
dir = '.'


with open('path_list.txt','w') as file:
    for i in os.listdir(dir):
        if i.endswith(ext): 
            file.write("/mydrive/images/hotel_rooms/bathroom/" + i+'\n')