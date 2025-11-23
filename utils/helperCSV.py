import csv
import json
from utils.helpers import get_file_path

def get_login_csv(csv_file="data_login.csv"):
    cfile=get_file_path(csv_file,"data")

    casos=[]

    with open(cfile,newline="") as h:
        read=csv.DictReader(h)
        for row in read:
            username=row["username"]
            password=row["password"]
            expected_result=row["login_result"].lower()=="true"
            casos.append((username,password,expected_result))
    
    return casos    

def get_login_json(json_file="data_login.json"):
    jfile=get_file_path(json_file,"data")

    datos=[]

    with open(jfile) as h:
        data=json.load(h)
        for row in data:
            username=row["username"]
            password=row["password"]
            expected_result=row["login_result"]
            datos.append((username,password,expected_result))

    return datos        