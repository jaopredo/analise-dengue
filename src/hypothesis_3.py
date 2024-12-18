import pandas as pd
import concurrent.futures
import os
import sys
sys.path.append(os.getcwd())
from src.hypothesis.hypothesis_3 import hypothesis3
from src.config import *
from src.utils.timing import measure_function_execution


@measure_function_execution
def main():
    # Vou ler o dataset por chunks
    chunks = pd.read_csv(os.path.join(DATASET_LOCAL(), f'sinan_dengue_sample_total.csv'), low_memory=False, chunksize=CHUNKS_SIZE)

    hypothesis3(chunks)


if __name__ == "__main__":
    main()
