import os
DATA_DIR = 'C:\Users\TheatroIT\Documents\Scripts2\grammar_converter\sample_grammars'

def print_available_grams(data_dir=DATA_DIR):
    for filename in os.listdir(DATA_DIR):
        print filename