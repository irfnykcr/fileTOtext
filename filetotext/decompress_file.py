from zlib import decompress as z_decompress
def decompress(filepath: str) -> bytes:
	try:
		with open(fr"{filepath}", "rb") as f:
			try:
				return z_decompress(f.read())
			except Exception as e: return f"Error while decompressing.\n{e}"
	except Exception as e: return f"Error while reading file.\n{e}"