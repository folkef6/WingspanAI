import os

PATH = "C:\\WingspanAI\\WingspanAI\\media\\Birds"
dir = os.fsencode(PATH)

for file in os.listdir(dir):
    old_filename = os.fsdecode(file)
    new_filename = old_filename.replace("_","’")
    os.rename(PATH + old_filename, PATH + new_filename)