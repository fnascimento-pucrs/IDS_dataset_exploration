import pandas as pd

# Read CSVs without optimization
# data_userN=pd.read_csv("UserN_BEHAVE.csv", encoding='latin-1')

# Read CSVs with memory optimization
# If the CSV files are readed without any optimization, columns are taken as float64, 
# so the CSV occupies a lot of memory.
# In order to reduce memory, this procedure changes dtype parameter and optmices it
# For that purpose, a chunk is read and then types are optimiced


def extract_dataframe(filename: str):
    data_user = pd.read_csv(filename, encoding='latin-1', chunksize=1000)

    a = next(data_user)
    dtypes_col = a.dtypes.index
    dtypes_type = [i.name for i in a.dtypes.values]
    column_types = dict(zip(dtypes_col, dtypes_type))

    for k, v in column_types.items():
        if k == 'timestamp':
            column_types[k] = 'float64'
        elif 'average' in k:
            column_types[k] = 'float32'
        elif 'stddev' in k:
            column_types[k] = 'float32'
        elif v == 'float64':
            column_types[k] = 'float32'
        elif v == 'int64':
            if k.startswith('press') or ('counter' in k) or ('usage' in k):
                column_types[k] = 'int8'
            else:
                column_types[k] = 'int32'

    data_user = pd.read_csv(filename, encoding='latin-1', dtype=column_types)
    return data_user
