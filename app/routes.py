from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from app import db
from app.models import Kevin

# Crea un blueprint para organizar las rutas
main = Blueprint('main', __name__)

# Página web principal
@main.route('/')
def home():
    kevin_list = Kevin.query.all()
    return render_template('index.html', kevin_list=kevin_list)

@main.route('/formulario')
def formulario():
    kevin_list = Kevin.query.all()
    return render_template('formulario.html', kevin_list=kevin_list)

# API básica de saludo
@main.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({"message": "Hello, welcome to my API!"})

# API con información de la UNID
@main.route("/api/unid", methods=["GET"])
def unid():
    return jsonify({
        "name": "Universidad Interamericana para el Desarrollo",
        "acronym": "UNID",
        "city": "Acapulco City",
        "country": "Mexico"
    })

# 🟢 API para listar registros de la tabla `kevin`
@main.route("/api/kevin", methods=["GET"])
def get_kevin():
    kevin_list = Kevin.query.all()
    return jsonify([{
        "id": k.id,
        "nombre": k.nombre,
        "apellidos": k.apellidos,
        "telefono": k.telefono
    } for k in kevin_list])

# 🔵 API para agregar un nuevo registro
@main.route("/api/kevin/add", methods=["POST"])
def add_kevin():
    nombre = request.form.get('nombre')
    apellidos = request.form.get('apellidos')
    telefono = request.form.get('telefono')

    if not nombre or not apellidos or not telefono:
        return "Error: Todos los campos son obligatorios", 400

    new_entry = Kevin(nombre=nombre, apellidos=apellidos, telefono=telefono)
    db.session.add(new_entry)
    db.session.commit()

    return redirect(url_for('main.home'))

# 🔴 API para eliminar un registro
@main.route("/api/kevin/delete/<string:id>", methods=["POST"])
def delete_kevin(id):
    entry = Kevin.query.get(id)
    if entry:
        db.session.delete(entry)
        db.session.commit()
        return redirect(url_for('main.home'))

    return jsonify({"error": "Usuario no encontrado"}), 404