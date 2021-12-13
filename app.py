# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, url_for,redirect


"""import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText"""


usuarios = {}

negocios_usuarios = {}

app = Flask(__name__)
app.secret_key = "ajhsdg56dkgasdhbs"

#/ hace referencia a la url base: http://127.0.0.1:5000/


@app.route('/bienvenida')
def bienvenida():
    return render_template('bienvenida.html')

@app.route('/cerrarsesion')
def cerrar_sesion():
    if 'user' in session:
        session.pop('user')
        return render_template ("inicio.html", despedida =  True)
    return render_template ("login.html", errorsesion = True)

@app.route('/')
def inicio():
    if 'user' in session:
        correo = session['user']
        nombreusuario = usuarios[correo]["username"]
        foto_perfil = usuarios[correo]["fotoperfil"]
        descrip_cion = usuarios[correo]["descripcion"]
        arreglo_misnegocios = []
        for nombrenegocio in negocios_usuarios:
            for correo_usuario in negocios_usuarios[nombrenegocio]:
                if correo_usuario != "":
                    negocio_creado = []
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["tiponegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["nombrenegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["descripcionnegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["imagennegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["portadanegocio"])
                    arreglo_misnegocios.append(negocio_creado)
        print('arreglo_misnegocios :', arreglo_misnegocios)
        return render_template ("inicio.html",  nav_logueado = True, nombre_usuario = nombreusuario, fotoperfil = foto_perfil, arreglo_misnegocios = arreglo_misnegocios, descripcion = descrip_cion)
    return render_template('inicio.html',nav_logueado=False)

@app.route('/crearnegocios')
def formulariocrearnegocio():
    if 'user' in session:
        correo = session['user']
        nombreusuario = usuarios[correo]["username"]
        
        print('funciona?',nombreusuario)
        return render_template('creacionnegocio.html',nombre_usuario = nombreusuario, nav_logueado = True)
    return render_template ("login.html", errorsesion = True, nav_logueado = False)

@app.route('/perfil/')
def mi_perfil():
    if 'user' in session:
        correo = session['user']
        no_mbres = usuarios[correo]["nombres"]
        ape_llidos = usuarios[correo]["apellidos"]
        nombreusuario = usuarios[correo]["username"]
        foto_perfil = usuarios[correo]["fotoperfil"]
        descrip_cion = usuarios[correo]["descripcion"]
        foto_perfil = usuarios[correo]["fotoperfil"]
        fo_toportada = usuarios[correo]["fotoportada"]
        arreglo_misnegocios = []
        for nombrenegocio in negocios_usuarios:
            for correo_usuario in negocios_usuarios[nombrenegocio]:
                if correo_usuario == correo:
                    negocio_creado = []
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["tiponegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["nombrenegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["descripcionnegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["imagennegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["portadanegocio"])
                    arreglo_misnegocios.append(negocio_creado)
        print('arreglo_misnegocios :', arreglo_misnegocios)
        return render_template('perfil.html', nombre_usuario= nombreusuario , nav_logueado=True, fotoperfil = foto_perfil, arreglo_misnegocios = arreglo_misnegocios, descripcion = descrip_cion, fotoportada = fo_toportada, nombres = no_mbres, apellidos = ape_llidos )
    return render_template ("login.html", errorsesion = True , nav_logueado = False)


"""@app.route('/perfil/<correo>')
def perfiles(correo):
    correo = usuarios[correo]
    nombreusuario = usuarios[correo]["username"]
    return render_template('perfil.html',nombre_usuario = nombreusuario)"""


@app.route('/negociocreado', methods= ['POST'])
def creacionnegocio():
    #aca verificamos si la cookie es valida y extraemos el correo
    #del usuario
    if 'user' in session:
        #aca extraemos el email del usuario
        correo = session['user']
        #HACEMOS LA INSCRIPCION AL CURSO MEDIANTE SU correo
        negocio = request.form.get("tiponegocio")
        if negocio == "panaderia" or negocio == "moda" or negocio == "otro":
            nombrenegocio = request.form.get("nombrenegocio")
            imagennegocio = request.form.get("imagennegocio")
            descripcionnegocio = request.form.get("descripcionnegocio")
            portadanegocio = request.form.get("portadanegocio")
            print('se ha creado un nuevo negocio:  ',nombrenegocio)
            negocios_usuarios[nombrenegocio] = {}
            negocios_usuarios[nombrenegocio][correo] = {}
            negocios_usuarios[nombrenegocio][correo]["tiponegocio"] = negocio
            negocios_usuarios[nombrenegocio][correo]["nombrenegocio"] = nombrenegocio
            negocios_usuarios[nombrenegocio][correo]["imagennegocio"] = imagennegocio
            negocios_usuarios[nombrenegocio][correo]["portadanegocio"] = portadanegocio
            negocios_usuarios[nombrenegocio][correo]["descripcionnegocio"] = descripcionnegocio

        print("negocios creados:  ", negocios_usuarios)
        nombreusuario = usuarios[correo]["username"]
        foto_perfil = usuarios[correo]["fotoperfil"]
        descrip_cion = usuarios[correo]["descripcion"]


        arreglo_misnegocios = []
        for nombrenegocio in negocios_usuarios:
            for correo_usuario in negocios_usuarios[nombrenegocio]:
                if correo_usuario != "":
                    negocio_creado = []
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["tiponegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["nombrenegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["descripcionnegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["imagennegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["portadanegocio"])
                    arreglo_misnegocios.append(negocio_creado)
        
        print('arreglo_misnegocios :', arreglo_misnegocios)

        return render_template ("inicio.html", creadonegocio = True, nav_logueado = True, nombre_usuario = nombreusuario, fotoperfil = foto_perfil, arreglo_misnegocios = arreglo_misnegocios, descripcion = descrip_cion)
    return render_template('login.html' , errorsesion = True , nav_logueado = False)

@app.route('/minegocio')
def mi_negocio():
    if 'user' in session:
        correo = session['user']
        #HACEMOS LA INSCRIPCION AL CURSO MEDIANTE SU correo
        nombreusuario = usuarios[correo]["username"]
        foto_perfil = usuarios[correo]["fotoperfil"]
        arreglo_misnegocios = []
        for nombrenegocio in negocios_usuarios:
            for correo_usuario in negocios_usuarios[nombrenegocio]:
                if correo_usuario == correo:
                    negocio_creado = []
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["tiponegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["nombrenegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["descripcionnegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["imagennegocio"])
                    negocio_creado.append(negocios_usuarios[nombrenegocio][correo]["portadanegocio"])
                    arreglo_misnegocios.append(negocio_creado)
        
        print('arreglo_misnegocios :', arreglo_misnegocios)
        return render_template ("minegocio.html", nav_logueado = True, nombre_usuario = nombreusuario, fotoperfil = foto_perfil, arreglo_misnegocios = arreglo_misnegocios)
    return render_template ('login.html', errorsesion = True , nav_logueado = False)

@app.route('/registro')
def registro():
    return render_template('registro.html', nav_logueado = False)

@app.route('/registrohecho', methods= ['POST'])
def registrohecho():
    correo = request.form.get("correo")
    contrasena = request.form.get("contrasena")
    username = request.form.get("username")
    nombres = request.form.get("nombres")
    apellidos = request.form.get("apellidos")
    fotoperfil = request.form.get("fotoperfil")
    fotoportada = request.form.get("fotoportada")
    descripcion = request.form.get("descripcion")
    usuarios[correo] = {}
    usuarios[correo]["contrasena"] = contrasena
    usuarios[correo]["username"] = username
    usuarios[correo]["nombres"] = nombres
    usuarios[correo]["apellidos"] = apellidos
    usuarios[correo]["fotoperfil"] = fotoperfil
    usuarios[correo]["fotoportada"] = fotoportada
    usuarios[correo]["descripcion"] = descripcion
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
    
    print('se ha enviado un correo a',usuarios[correo])"""
    return render_template('login.html', loginok = True, nav_logueado = False)
    


@app.route('/login')
def login():
    return render_template('login.html', nav_logueado = False)


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
            nombreusuario = usuarios[correo]["username"]
            #generamos cookie de sesion igual al correo de usuario
            #tabien, podriamos hacerlo con el id de base de datos etc
            #tambein, podriamos agregar mas valores a la cookie
            session['user'] = correo
            if 'user' in session:
                no_mbres = usuarios[correo]["nombres"]
                ape_llidos = usuarios[correo]["apellidos"]
                foto_perfil = usuarios[correo]["fotoperfil"]
                descrip_cion = usuarios[correo]["descripcion"]
                fo_toportada = usuarios[correo]["fotoportada"]
                arreglo_misnegocios = []
                for negocio in negocios_usuarios:
                    for correo_usuario in negocios_usuarios[negocio]:
                        if correo_usuario == correo:
                            negocio_creado = []
                            negocio_creado.append(negocio)
                            negocio_creado.append(negocios_usuarios[negocio][correo]["nombrenegocio"])
                            negocio_creado.append(negocios_usuarios[negocio][correo]["descripcionnegocio"])
                            negocio_creado.append(negocios_usuarios[negocio][correo]["imagennegocio"])
                            negocio_creado.append(negocios_usuarios[negocio][correo]["portadanegocio"])
                            arreglo_misnegocios.append(negocio_creado)
                print('arreglo_misnegocios :', arreglo_misnegocios)
                return render_template('perfil.html', nombre_usuario=nombreusuario , nav_logueado=True, fotoperfil = foto_perfil, arreglo_misnegocios = arreglo_misnegocios, descripcion = descrip_cion, fotoportada = fo_toportada, nombres = no_mbres, apellidos = ape_llidos )
        return render_template ("login.html", credencialincorrecta = True, nav_logueado = False) 
    return render_template ("login.html", cuentanoexiste = True, nav_logueado = False)

"""_________________________PARTE FOOTER_________________________"""

@app.route('/Sobre_nosotros')
def Sobre_nosotros():
    if 'user' in session:
        correo = session['user']
        nombreusuario = usuarios[correo]["username"]
        return render_template('Sobre_nosotros.html', nav_logueado = True, nombre_usuario=nombreusuario)
    return render_template('Sobre_nosotros.html', nav_logueado = False)

@app.route('/contactanos')
def conctatanos():
    if 'user' in session:
        correo = session['user']
        nombreusuario = usuarios[correo]["username"]
        return render_template('contactanos.html', nav_logueado = True, nombre_usuario=nombreusuario)
    return render_template('contactanos.html', nav_logueado = False)

@app.route('/terminos_condiciones')
def terminos_condiciones():
    if 'user' in session:
        correo = session['user']
        nombreusuario = usuarios[correo]["username"]
        return render_template('terminos_condiciones.html', nav_logueado = True, nombre_usuario=nombreusuario)
    return render_template('terminos_condiciones.html', nav_logueado = False)

@app.route('/politica_privacidad')
def politica_provacidad():
    if 'user' in session:
        correo = session['user']
        nombreusuario = usuarios[correo]["username"]
        return render_template('politica_privacidad.html', nav_logueado = True, nombre_usuario=nombreusuario)
    return render_template('politica_privacidad.html', nav_logueado = False)

@app.route('/Quienes_Somos')
def quienes_somos():
    if 'user' in session:
        correo = session['user']
        nombreusuario = usuarios[correo]["username"]
        return render_template('Quienes_Somos.html', nav_logueado = True, nombre_usuario=nombreusuario)
    return render_template('Quienes_Somos.html', nav_logueado = False)

@app.route('/Desarrolladores')
def Desarrolladores():
    if 'user' in session:
        correo = session['user']
        nombreusuario = usuarios[correo]["username"]
        return render_template('Desarroladores.html', nav_logueado = True, nombre_usuario=nombreusuario)
    return render_template('Desarroladores.html', nav_logueado = False)
"""________________________FIN PARTE FOOTER_________________________"""







app.run(debug = True, port=5000)
