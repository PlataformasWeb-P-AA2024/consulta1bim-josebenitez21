import pandas as pd
from pymongo import MongoClient


df = pd.read_csv('atp_tennis.csv')

# Conectar a MongoDB
client = MongoClient('localhost', 27017)
db = client['tennis_db']
collection = db['matches']


data = df.to_dict(orient='records')
collection.insert_many(data)

print("Datos insertados exitosamente en MongoDB")

#Consulta para mostrar los 5 primeros partidos.

for match in collection.find().limit(5):  
    print(match)

#En la consola de mongo tambien podemos hacer la consulta usando lo siguiente:
#use tennis_db
#db.matches.find().limit(5).pretty()
#Se adjuntaron capturas de pantalla en la carpeta del codigo.
