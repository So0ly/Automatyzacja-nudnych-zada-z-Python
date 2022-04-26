import traceback,os
os.chdir('C:\\Users\\Soldi\\Documents\\Python - skrypty\\2021.02.18\\10')
try:
	raise Exception('To jest komunikat bledu.')
except:
	errorFile=open('errorInfo.txt','w')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('Info o bledach w pliku errorInfo.txt')
