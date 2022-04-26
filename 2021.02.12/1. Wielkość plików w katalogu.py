>>> total=0
>>> for filename in os.listdir('C:\\Users\\Soldi\\Documents\\Python - skrypty\\2020.07.24'):
	total+=os.path.getsize(os.path.join('C:\\Users\\Soldi\\Documents\\Python - skrypty\\2020.07.24',filename))
>>> print(total)
