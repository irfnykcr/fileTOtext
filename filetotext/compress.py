from deflate import zlib_compress
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
				data = f.read()
			try:
				r = zlib_compress(data, level)
			except Exception as e:
				return f"Error while compressing.\n{e}"
			with open(fr"{newout}/{file}", "ab") as f:
				f.write(str(len(data)).encode("utf-8") + b" " + r)
	except Exception as e:
		return f"File not found.\n{e}"
	try:
		rmtree(oldout)
	except Exception as e:
		return f"Cannot remove directory {oldout}.\n{e}"
	return f"File chunked, compressed and saved in './{newout}'"