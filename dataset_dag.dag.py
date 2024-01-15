from pendulum import datetime
from airflow.datasets import Dataset
from airflow.decorators import dag, task
import os

from keras.models import Sequential
from keras.layers import Dense


FILE_PATH = os.path.join(os.path.expanduser('~/data'), 'data.txt')
FILE_PATH_2 = os.path.join(os.path.expanduser('~/data'), 'model.h5')
INSTRUCTIONS = Dataset(FILE_PATH)
INFO = Dataset(FILE_PATH_2)

@dag(
    dag_id="datasets_consumer_dag",
    start_date=datetime(2022, 10, 1),
    schedule=[INSTRUCTIONS],
    catchup=False,
    tags=['ml_test']
)

def datasets_producer_dag():
    @task(outlets=[INFO])
    def write_info_to_file(path1, path2):
    
        x_train = pd.read_csv(path1)
        y_train = x_train['labels']
        model = Sequential()
        
        model = keras.models.load_model(path2)
        
        model.fit(x_train, y_train,
                  batch_size=200,
                  epochs=50,
                  verbose=1)
        
        model.save('model.h5')

    write_info_to_file(FILE_PATH, FILE_PATH_2)
datasets_producer_dag()   