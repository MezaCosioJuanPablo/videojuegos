from flask import Blueprint, jsonify, render_template, request, redirect, url_for

# Crea un blueprint para organizar las rutas
main = Blueprint('main', __name__)

# Ruta para la página web principal
@main.route('/')
def home():
    return render_template('index.html')

# Ruta para la API de saludo
@main.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({"message": "Hello, welcome to my API!"})

# Ruta para la API de UNID
@main.route('/api/unid', methods=['GET'])
def unid():
    return jsonify(
        {
           "name": "Universidad Interamericana para el Desarrollo",
           "acronym": "UNID",
           "city": "Acapulco City",
           "country": "Mexico"
        }
    )

# Ruta para la página "Base"
@main.route('/base')
def base():
    return render_template('base.html')

# Ruta para la página de "Contacto"
@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Puedes realizar alguna acción con los datos, como almacenarlos o enviarlos por email
        print(f"Mensaje recibido de {name} ({email}): {message}")
        # Redirigir con un mensaje de confirmación
        return render_template('contact.html', confirmation=True)
    return render_template('contact.html', confirmation=False)

# Ruta para la página "Acerca de"
@main.route('/about')
def about():
    return render_template('about.html')
