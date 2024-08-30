from deflate import zlib_compress

def compress(filepath: str, level: int = 6):

    return zlib_compress(filepath, level)