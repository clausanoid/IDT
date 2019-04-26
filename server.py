from flask import Flask, render_template  # la libreria flask nos permite hacer un servidor web
from flask import Response
import json  # la libreria json nos permite convertir texto a json para consumir en cualquier lenguaje compatible
from time import sleep  # usamos la libreria sleep para darle tiempo a la tarjeta arduino de reiniciarse
import serial, time  # usamos la libreria serial para hacer la comunicacion a puerto serial

# configuramos nuestra aplicacion para que inicie en cuanto usemos el comando run
app = Flask(__name__)


# creamos una ruta , que tomara el nombre de la pagina html y la mostrara ejemplo: http://localhost/sensor.html
@app.route('/<string:page_name>/')
# le decimos a flask que usaremos los nombre de archivo de la carpeta templates
def render_static(page_name):
    return render_template('%s.html' % page_name)


# Creamos una ruta que nos regrese json con el status que muestra el sensor de nuestro arduino
@app.route('/sensor', methods=['GET'])
def api_sensor():
    # nos conectamos al puerto serial de nuestro equipo
    arduino = serial.Serial('COM3', baudrate=9600, timeout=1.0)
    # Nota: provocamos un reseteo manual de la placa para leer desde
    # el principio, ver http://stackoverflow.com/a/21082531/554319
    arduino.setDTR(False)
    time.sleep(1)
    arduino.flushInput()
    arduino.setDTR(True)
    # En Python 3 esta función devuelve un objeto bytes, ver
    # http://docs.python.org/3/library/stdtypes.html#typebytes
    line = arduino.readline()
    # Con errors='replace' se evitan problemas con bytes erróneos, ver
    # http://docs.python.org/3/library/stdtypes.html#bytes.decode
    # Con end='' se evita un doble salto de línea
    print(line.decode('ascii', errors='replace'), end='')
    # se muestra la informacion en json cada que hacemos una solicitud a nuestro endpoint
    data = {
        'mensaje': str(line.decode('ascii', errors='replace'), end='')

    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://localhost'

    return resp
