from json import load
from filetotext import make_chunks
from filetotext import compress
from sys import argv
def main(filepath: str):
    with open(r"./config/app.json", "r") as f: info = load(f)
    key = open(info['keyfile'], "rb").read()
    chunks = int(info['chunk_lenght'])
    willcompress = bool(info['compress'])
    level = int(info['compression_level'])

    r = make_chunks.chunked(filepath=filepath, key=key, chunks=chunks, willcompress=willcompress)
    if willcompress:
        print(compress.compress(dirpath=fr"output/temp_{r}", level=level))
if __name__ == "__main__":
    print("Usage: main.py <file>") if len(argv) != 2 else main(argv[1])
    