import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker


#creating an engine
url = URL.create(
    drivername="postgresql",
    username="postgres",
    host="localhost",
    database="creditcard_data"
)
engine = create_engine(url)
connection = engine.connect()

Base = declarative_base()

class Creditcard(Base):
    __tablename__ = 'creditcard'

    id = Column(Integer(), primary_key=True)
    time = Column(Integer())
    v1 = Column(Integer())
    v2 = Column(Integer())
    v3 = Column(Integer())
    # v4 = Column(Integer())
    # v5 = Column(Integer())
    # v6 = Column(Integer())
    # v7 = Column(Integer())
    # v8 = Column(Integer())
    # v9 = Column(Integer())
    # v10 = Column(Integer())
    # v11 = Column(Integer())
    # v12 = Column(Integer())
    # v13 = Column(Integer())
    # v14 = Column(Integer())
    # v16 = Column(Integer())
    # v17 = Column(Integer())
    # v18 = Column(Integer())
    # v19 = Column(Integer())
    # v20 = Column(Integer())
    # v21 = Column(Integer())
    # v22 = Column(Integer())
    # v23 = Column(Integer())
    # v24 = Column(Integer())
    # v25 = Column(Integer())
    # v26 = Column(Integer())
    # v27 = Column(Integer())
    # v28 = Column(Integer())
    # amount = Column(Integer())



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
#loading data as dataframe in pandas
data = pd.read_csv('creditcard.csv', lineterminator='\n')
rows_list = []

for idx,row in data.iterrows():
    info = Creditcard(
        time= row['Time'],
        v1= row['V1'],
        v2=row['V2'],
        v3=row['V3'],
    )
    rows_list.append(info)
print(len(rows_list))

for idx in range(0,len(rows_list),5000):
    session.add_all(rows_list[idx:idx+5000])
    session.commit()




