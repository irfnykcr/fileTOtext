from os import mkdir
from cryptography.fernet import Fernet
from time import perf_counter_ns
def chunked(fname: str,filepath: str, key: bytes, chunks: int=3000000, willcompress: bool=True) -> int:
	"""
	chunks, encrypts and saves the file in the 'output/id' folder.
	function returns the id.
	"""
	try:
		fer = Fernet(key)
	except Exception as e:
		return f"Invalid key\n{e}"
	unix_1 = perf_counter_ns()
	if willcompress:outdir = f"output/temp_{unix_1}"
	else: outdir = f"output/{unix_1}-{fname}"
	try:
		mkdir(outdir)
	except:
		try:
			from shutil import rmtree
			rmtree(outdir)
			mkdir(outdir)
		except Exception as e:
			return f"Cannot create directory.\n{e}"
	try:
		with open(filepath, "rb") as f:
			while chunk := f.read(chunks):
				unix_2 = perf_counter_ns()
				with open(fr"{outdir}/{unix_2}", "ab") as fw:
					fw.write(fer.encrypt(chunk))
	except Exception as e:
		return f"Something went wrong! File not found.\n{e}"
	return unix_1