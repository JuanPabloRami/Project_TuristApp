# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, url_for
from werkzeug.utils import redirect

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


usuarios = {}

app = Flask(__name__)
#app.secret_key = "ajhsdg56dkgasdhbs"

#/ hace referencia a la url base: http://127.0.0.1:5000/


@app.route('/bienvenida')
def bienvenida():
    return render_template('bienvenida.html')


@app.route('/')
def inicio():
    return render_template('inicio.html')



@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/registrohecho', methods= ['POST'])
def registrohecho():
    correo = request.form.get("correo")
    contrasena = request.form.get("contrasena")
    username = request.form.get("username")
    primernombre= request.form.get("primernombre")
    segundonombre = request.form.get("segundonombre")
    usuarios[correo] = {}
    usuarios[correo]["contrasena"] = contrasena
    usuarios[correo]["username"] = username
    usuarios[correo]["primernombre"] = primernombre
    usuarios[correo]["segundonombre"] = segundonombre
    print("------------------------------------------------------------")
    print(correo,"se ha registrado")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("usuarios registrados: ", usuarios)
    print("--------------------------------------------------------------------------------------------------------------------")

    #credenciales
    proveedor_correo = 'smtp.live.com: 587'
    remitente = 'Adsi2339490_@outlook.com'
    password = '2339490adsi'
    #conexion a servidor
    servidor = smtplib.SMTP(proveedor_correo)
    servidor.starttls()
    servidor.ehlo()
    #autenticacion
    servidor.login(remitente, password)
    #mensaje 
    mensaje = """"<table>
    <h1>BIENVENIDO</h1>
    <p>BIENVENIDO A TURISTAPP, {{primernombre}} {{segundonombre}}</p>
    <p>nombre de usuario {{username}}</p>
    <p>correo {{correo}} a aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 30</p>


    </table>"""
    msg = MIMEMultipart()
    msg.attach(MIMEText(mensaje, 'html'))
    msg['From'] = remitente
    msg['To'] = 'juanpalabloramirezavs@gmail.com'
    msg['Subject'] = 'BIENVENIDO A TURISTAPP 2'
    servidor.sendmail(msg['From'] , msg['To'], msg.as_string())
    print('se ha enviado un correo a',usuarios[correo])
    print(mensaje)
    return render_template('registrohecho.html')
    


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logueado', methods= ['POST'])
def logueado():
    correo = request.form.get("correo")
    contrasena = request.form.get("contrasena")

    if usuarios.get(correo):
        if usuarios[correo]["contrasena"] == contrasena:
            print('----------------------------------')
            print(correo,"se ha logueado")
            print('----------------------------------')
            return render_template('logueohecho.html')
        return "Usuario o password incorrecto"
    return "Esta cuenta no existe, registrese."

app.run(debug = True, port=5000)
