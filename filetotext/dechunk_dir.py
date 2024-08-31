from os import listdir
from time import perf_counter_ns
from cryptography.fernet import Fernet
from filetotext import decompress_file
def dechunked(dirpath: str, key: bytes, willcompress: bool) -> str:
	try:
		fer = Fernet(key)
	except Exception as e:
		return f"Invalid key\n{e}"
	unix_1 = perf_counter_ns()
	try:
		fname = (dirpath.split("\\")[-1]).split("-")[-1]
	except Exception as e:
		try:
			fname = (dirpath.split("/")[-1]).split("-")[-1]
		except:
			return "Invalid directory path"
	for file in listdir(dirpath):
		if willcompress:
			try:
				data = decompress_file.decompress(filepath=fr"{dirpath}/{file}")
				if type(data) == str: return data
			except Exception as e:
				return f"Error while decompressing.\n{e}"
		else:
			try:
				with open(fr"{dirpath}/{file}", "rb") as f: data = f.read()
			except Exception as e:
				return f"Error while reading file.\n{e}"
		try:
			r = fer.decrypt(data)
		except Exception as e:
			return f"Error while dechunking.\n{e}"
		try:
			with open(fr"./output/{unix_1}-{fname}", "ab") as f:
				f.write(r)
		except Exception as e:
			return f"Error while writing file.\n{e}"
	if willcompress: return f"File dechunked, decompressed and saved in './output/{unix_1}-{fname}'"
	else: return f"File dechunked and saved in './output/{unix_1}-{fname}'"