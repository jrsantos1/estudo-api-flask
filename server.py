from flask import jsonify
import pyodbc 
import pandas as pd
import json
 
cnxn = pyodbc.connect("Driver={SQL Server};Server=DESKTOP-EN90SVC;Database=Fundos")
cursor = cnxn.cursor()
# fundos = cursor.execute("Select * from Fundos").fetchall()
def consulta(query): 
    dados = pd.read_sql(query, cnxn)
    jso = json.loads(dados.to_json(orient='records'))
    return jso



#with (cnxn.cursor() as conexao):
    
    