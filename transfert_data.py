from sqlalchemy import create_engine, Column, Integer, Select, text
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


Session = sessionmaker(bind=engine)
session = Session()


data = list(session.execute(text("""SELECT * FROM creditcard;""")))

session.close()
#creating an engine
url2 = URL.create(
    drivername= "mysql+pymysql",
    username= "root",
    host= "localhost",
    database= "creditcard_data"
)
engine2 = create_engine(url2)

connection2 = engine2.connect()

Base2 = declarative_base()
class Creditcard(Base2):
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
Base2.metadata.create_all(engine2)

Session2 = sessionmaker(bind=engine2)
session2 = Session2()
rows_list = []
for row in data:
    info = Creditcard(
        time= row[1],
        v1= row[2],
        v2=row[3],
        v3=row[4],
    )
    rows_list.append(info)

for idx in range(0,len(rows_list), 5000):
     session2.add_all(rows_list[idx:idx+5000])
     session2.commit()

