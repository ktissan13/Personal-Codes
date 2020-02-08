# Rename Batch Files
# Tissan Kugathas
# Feb 8th 2020

import os

src = "D:\ANIME\Black Clover (TV) (Dub)"
i = 79

while i < 100:
    string = "Black Clover (Dub) - 0"+str(i)+".mp4"
    for filename in os.listdir(src):
        if filename.upper() == string.upper():
            new_name = "Black Clover (Dub) - "+str(i)+".mp4"
            print(filename)
            os.rename(src+'\\'+filename,src+'\\'+new_name)
            i += 1
