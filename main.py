from json import load
from filetotext import compress_dir, dechunk_dir, make_chunks_file
from sys import argv

def chunk(filepath: str, fname:str="output") -> str:
    try:
        with open(r"./config/app.json", "r") as f: info = load(f)
        key = open(info['keyfile'], "rb").read()
        chunks = int(info['chunk_lenght'])
        willcompress = bool(info['compress'])
        level = int(info['compression_level'])
    except Exception as e:
        return f"Error while loading configuration.\n{e}"
    try:
        r = make_chunks_file.chunked(fname=fname, filepath=filepath, key=key, chunks=chunks, willcompress=willcompress)
    except Exception as e:
        return f"Error while chunking file.\n{e}"
    try:
        if willcompress: return compress_dir.compress(r=r, level=level,fname=fname)
        else: return f"File chunked and saved in './output/{r}-{fname}'"
    except Exception as e:
        return f"Error while compressing.\n{e}"

def dechunk(filepath: str) -> str:
    try:
        with open(r"./config/app.json", "r") as f: info = load(f)
        key = open(info['keyfile'], "rb").read()
        willcompress = bool(info['compress'])
    except Exception as e:
        return f"Error while loading configuration.\n{e}"
    try:
        r = dechunk_dir.dechunked(dirpath=filepath, key=key, willcompress=willcompress)
        return r
    except Exception as e:
        return f"Error while dechunking file.\n{e}"

def _help(i: int = 0):
    if i == 1: return "Usage: main.py <chunk> <file> [filename]"
    elif i == 2: return "Usage: main.py <dechunk> <file_dir>"
    else: return "Usage: main.py <chunk> <file> [filename]\nUsage: main.py <dechunk> <file_dir>"

if __name__ == "__main__":
    if len(argv) < 2: print(_help()); exit()
    elif argv[1] == "chunk":
        if len(argv) == 3: r = chunk(argv[2])
        elif len(argv) == 4: r = chunk(argv[2], argv[3])
        else: print(_help(1)); exit()
    elif argv[1] == "dechunk":
        if len(argv) == 3: r = dechunk(argv[2])
        else: print(_help(2)); exit()
    else:
        print(_help());exit()
    print(r)