from zlib import compress as z_compress
from os import listdir, mkdir
from shutil import rmtree

def compress(fname:str, r: int, level: int = 6):
	oldout = fr"output/temp_{r}"
	newout = fr"output/{r}-{fname}"
	try:
		mkdir(newout)
	except:
		try:
			rmtree(newout)
			mkdir(newout)
		except Exception as e:
			return f"Cannot create directory.\n{e}"
	try:
		for file in listdir(oldout):
			with open(fr"{oldout}/{file}", "rb") as f:
				try:
					r = z_compress(f.read(), level)
				except Exception as e:
					return f"Error while compressing.\n{e}"
				with open(fr"{newout}/{file}", "ab") as f2:
					f2.write(r)
	except Exception as e:
		return f"File not found.\n{e}"
	try:
		rmtree(oldout)
	except Exception as e:
		return f"Cannot remove directory {oldout}.\n{e}"
	return f"File chunked, compressed and saved in './{newout}'"