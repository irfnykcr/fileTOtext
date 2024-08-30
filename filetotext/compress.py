from deflate import zlib_compress
from os import listdir
def compress(dirpath: str, level: int = 6):
	for file in listdir(dirpath):
		with open(file, "rb") as f:
			data = f.read()
		r = zlib_compress(data, level)
		with open(file, "wb") as f:
			f.write(str(len(data)).encode("utf-8") + " " + r)
			return True