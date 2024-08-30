from json import load
from filetotext import make_chunks

def main(file):
    with open(r"./config/app.json", "r") as f: info = load(f)
    key = open(info['keyfile'], "rb").read()
    chunks = info['chunk_lenght']
    r = make_chunks.chunked(file, key, chunks)
    print(r)
if __name__ == "__main__":
    main("test/monkey.mp4")