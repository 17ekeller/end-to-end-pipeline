from IPython.display import display
import pandas as pd
from sqlalchemy import create_engine

password = "Rockon2017#"
database = "demo1"
#create a the dataframe and display the data
data = {'name': ['Eric', 'Kenyon', 'TrevDog'],
        'address': ['1435 E. Katie Ln', '123 Wauconda Way', 'NULL']}
df=pd.DataFrame(data)
display(df)

#create SQLAlchemy engine to connect the database
engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/{database}")

df.to_sql('customers', con=engine, if_exists='replace', index=False)
print("data upload complete")