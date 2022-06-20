#Bibliografía
1. ```https://www.digitalocean.com/community/tutorials/como-preparar-aplicaciones-de-flask-con-gunicorn-y-nginx-en-ubuntu-18-04-es```
2. ```https://www.youtube.com/watch?v=Esdj9wlBOaI&t=157s```


#Tutorial
1. Instalar python
2. Instalar pip
3. Crear un entorno virtual de Python
3.1 ```sudo apt install python3-venv```
3.2 Crear entorno virtual para este proyecto
```python3 -m venv ToDo_env```
Con esto se instalará una copia local de Python y pip en un directorio llamado ToDo_env dentro del directorio de su proyecto.
3.3 Activar entorno virtual
```source ToDo_env/bin/activate```
4. Instalar flask
```pip install flask```
4.1 Ejemplo sencillo de flask
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port:4000)
```

4.2 Ejecutar nuestro servidor
```python3 app.py```
