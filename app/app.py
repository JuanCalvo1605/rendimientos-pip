from flask import Flask, jsonify,request
from flask_cors import CORS
import pymssql
from waitress import serve
app = Flask(__name__)
CORS(app)

# Ruta para obtener datos desde la base de datos
#@app.route('/obtener_datos', methods=['GET'])
def obtener_datos(parametro1,parametro2):
    try:
        print("Intentando conectar a la base de datos...")
        conn = pymssql.connect(
            server = '172.20.10.2',
            user= 'consulta',
            password= 'Consulta_2017',
            database = 'MONVER',
            as_dict= True
            )
        print("Conexión establecida.")
        cursor = conn.cursor()
        print(f"Ejecutando consulta con parametros: {parametro1}, {parametro2}")
        # Obtener parámetros de la solicitud
        #parametro1 = request.args.get('parametro1')
        #parametro2 = request.args.get('parametro2')
        # Utilizar parámetros nombrados con SQL Server
        #sql = 
        cursor.execute("SELECT ltrim(rtrim(NOMBRE)) as NOMBRE, REND_HR FROM dbo.fp_inf_rendimiento_clav2(%s, %s)", (parametro1, parametro2))
        resultados = cursor.fetchall()
        print("Consulta ejecutada exitosamente.")
        print("Resultados obtenidos:", resultados)
        #resultados_json = []
        #for x in resultados:
            
            #resultados_json.append(dict(zip([column[0] for column in cursor.description], x)))
        # Cerrar la conexión
        conn.close() 
        print("Conexión cerrada.")
        # Devolver resultados en formato JSON
        #return resultados
        return jsonify(resultados)
        
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    #serve(app,host = '172.19.10.8',port="8084", threads=2)
    obtener_datos('20240729','20240729')