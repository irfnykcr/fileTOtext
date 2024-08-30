from json import load
from filetotext import make_chunks
from filetotext import compress
from sys import argv
def main(filepath: str, fname:str="output") -> None:
    try:
        with open(r"./config/app.json", "r") as f: info = load(f)
        key = open(info['keyfile'], "rb").read()
        chunks = int(info['chunk_lenght'])
        willcompress = bool(info['compress'])
        level = int(info['compression_level'])
    except Exception as e:
        return f"Error while loading configuration.\n{e}"
    try:
        r = make_chunks.chunked(fname=fname, filepath=filepath, key=key, chunks=chunks, willcompress=willcompress)
    except Exception as e:
        return f"Error while chunking file.\n{e}"
    try:
        if willcompress: return compress.compress(r=r, level=level,fname=fname)
        else: return f"File chunked and saved in './output/{r}-{fname}'"
    except Exception as e:
        return f"Error while compressing.\n{e}"
if __name__ == "__main__":
    if len(argv) == 2: r = main(argv[1])
    elif len(argv) == 3: r = main(argv[1], argv[2])
    else: print("Usage: main.py <file> [filename]"); exit()
    print(r)
    