# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, url_for,redirect


"""import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText"""


usuarios = {}

negocios_usuarios = {"panaderia": {}, "moda": {} }

app = Flask(__name__)
app.secret_key = "ajhsdg56dkgasdhbs"

#/ hace referencia a la url base: http://127.0.0.1:5000/


@app.route('/bienvenida')
def bienvenida():
    return render_template('bienvenida.html')


@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/tiponegocio')
def formulariotiponegocio():
    
    return render_template('tiponegocio.html')

@app.route('/detallesnegocio')
def formulariodetallesnegocio():
    return render_template('creacionnegocionegocio.html')



@app.route('/negociocreado/<negocio>')
def creacionnegocio(negocio):
    #aca verificamos si la cookie es valida y extraemos el correo
    #del usuario
    if 'user' in session:
        #aca extraemos el email del usuario
        correo = session['user']
        #HACEMOS LA INSCRIPCION AL CURSO MEDIANTE SU correo
        if negocio == "panaderia" or negocio == "moda":
            negocios_usuarios[negocio]["correo"] = correo

        else:
            return "error, usted solo puede crear un negocio valido", 401
        print("negocios creados:  ", negocios_usuarios)
        nombreusuario = usuarios[correo]["primernombre"]
        return "Señor {} Usted ha creado su nuevo negocio ".format(nombreusuario), 201 
    return redirect('/login' , 'error , debe iniciar !!funciona!!sesion')



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

    """
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
    mensaje = """
    """
    msg = MIMEMultipart()
    msg.attach(MIMEText(mensaje, 'html'))
    msg['From'] = remitente
    msg['To'] = 'juanpalabloramirezavs@gmail.com'
    msg['Subject'] = 'BIENVENIDO A TURISTAPP 2'
    servidor.sendmail(msg['From'] , msg['To'], msg.as_string())
    """
    print('se ha enviado un correo a',usuarios[correo])
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
            #para saludar al usuario extraemos el nombre
            nombre = usuarios[correo]["username"]
            #generamos cookie de sesion igual al correo de usuario
            #tabien, podriamos hacerlo con el id de base de datos etc
            #tambein, podriamos agregar mas valores a la cookie
            session['user'] = correo
            return render_template('perfil.html', nombre_usuario=nombre)
        return "Usuario o password incorrecto"
    return "Esta cuenta no existe, registrese.", 401






app.run(debug = True, port=5000)
