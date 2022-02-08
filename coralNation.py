import numpy as np
import plotly.express as px
import csv

def getDataSource (data_path):
    sizeTv=[]
    timeSpit=[]
    with open(data_path)as f:
        df=csv.DictReader(f)
        for row in df:
            sizeTv.append(float(row["Size of TV"]))
            timeSpit.append(float(row["Average time spent watching TV in a week"]))
        #graf=px.scatter(df, x="Size of TV", y="Average time spent watching TV in a week")
        #graf.show()
    return{"x":sizeTv,"y":timeSpit}
    

def findCorellation (data_source):
    corall=np.corrcoef(data_source["x"],data_source["y"])
    print(corall[0,1])

def setup ():
    data_path="TvData.csv"
    data_source=getDataSource(data_path)
    findCorellation(data_source)

setup()
