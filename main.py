from json import load
from filetotext import make_chunks
from sys import argv
def main(filepath: str):
    with open(r"./config/app.json", "r") as f: info = load(f)
    key = open(info['keyfile'], "rb").read()
    chunks = info['chunk_lenght']
    r = make_chunks.chunked(filepath, key, chunks)
    print(r)
if __name__ == "__main__":
    if len(argv) != 2: print("Usage: main.py <file>"); exit()
    main(argv[1])