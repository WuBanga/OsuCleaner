import os
import re

path = os.path.abspath("D:\\osu!\\Songs")
libs = os.listdir(path)

for lib in libs:
	for file in os.listdir(path + "\\" + lib):
		if file.endswith(".osu"):
			f = open(path + "\\" + lib + "\\" + file, encoding='utf-8')
			text = f.read()
			if int(re.search(r'Mode:\s([0-9])', text).group(1)) != 0:
				f.close()
				os.remove(path + "\\" + lib + "\\" + file)