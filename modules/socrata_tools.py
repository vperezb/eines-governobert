from sodapy import Socrata
import pandas as pd

def __get_socrata_client(app_token):
    return Socrata('analisi.transparenciacatalunya.cat',
                 app_token= app_token)

def get_pandas_from_dataset_id(dataset_id, client, chunk_size = 2000):
    all_data = []
    data_left = True
    next_start = 0
    while data_left:
        all_data +=  client.get(dataset_id, 
                               limit = chunk_size, 
                               offset = next_start)
        next_start = len(all_data)
        data_left = not bool(next_start % chunk_size)
    return pd.DataFrame.from_records(all_data)