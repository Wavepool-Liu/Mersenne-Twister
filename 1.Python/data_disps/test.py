import numpy as np


filename = "E:\\Mersenne-Twister\\1.Python\\data_disps\\tdata.txt"
pos = []
with open(filename, 'r') as file_to_read:
	while True:
		lines = file_to_read.readline() 
		lines = lines.strip('\n')
		if not lines:
			break
		pos.append(lines) 
print(pos)