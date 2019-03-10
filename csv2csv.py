import pandas as pd
import sys

path = sys.argv[1]
print('loading from', path)
file = pd.read_csv(path, encoding='cp1250', delimiter=';', low_memory=False)
file_name = path[5:]
new_path = 'data_new/' + file_name
print('saving to', new_path)
file.to_csv(new_path, sep=',', encoding='utf-8', index=False)
