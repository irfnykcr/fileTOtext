from os import mkdir
from cryptography.fernet import Fernet
from time import perf_counter_ns

def chunked(file, key, chunks=3000000):
	try:
		fer = Fernet(key)
	except Exception as e:
		return f"Invalid key\n{e}"

	unix_1 = perf_counter_ns()
	outdir = f"output/{unix_1}"

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
		with open(file, "rb") as f:
			while chunk := f.read(chunks):
				unix_2 = perf_counter_ns()
				with open(fr"{outdir}/{unix_2}", "ab") as fw:
					fw.write(fer.encrypt(chunk))
	except Exception as e:
		return f"Something went wrong! File not found.\n{e}"

	return unix_1