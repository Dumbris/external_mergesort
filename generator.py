import os
import numpy as np
from tqdm import tqdm


def write_to_file(name, arr):
    with open(name, 'ab') as file:
        np.savetxt(file, arr, delimiter=" ", fmt='%d')

def write_to_file2(name, arr):
    with open(name, 'w+') as file:
        file.writelines(arr)

def rows_to_str(arr):
    return [" ".join(map(str,line)) for line in arr]

def generate(size=(1,5)):
    return np.random.randint(np.iinfo(np.int32).min,high=np.iinfo(np.int32).max, size=size, dtype=np.int32)

#@profile
def gen(name, size):
    total_col, total_rows = size
    chunk_size = 5000
    n = total_col // chunk_size
    with open(name, 'a') as file:
        for _ in tqdm(range(0,n)):
            arr = generate((chunk_size, total_rows))
            np.savetxt(file, arr, delimiter=" ", fmt='%d')

if __name__ == '__main__':
    name = os.environ.get('FILENAME')
    if not name:
        print("Please, set FILENAME environment variable.")
        exit(1)
    gen(name, (50000,50000))
