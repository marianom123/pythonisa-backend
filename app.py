from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from datetime import datetime
import os

app = Flask(__name__)

# Conexión a la DB:
#------------------------------------------------
# Link: https://www.phpmyadmin.co/
# Server: sql10.freemysqlhosting.net
# DB Name: sql10717628
# Username: sql10717628
# Password: 6rqZbmvWgl
# Port number: 3306
#------------------------------------------------
mysql = MySQL()

app.config['MYSQL_HOST'] = 'sql10.freemysqlhosting.net'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'sql10717628'
app.config['MYSQL_PASSWORD'] = '6rqZbmvWgl'
app.config['MYSQL_DB'] = 'sql10717628'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql.init_app(app)

UPLOADS = os.path.join('uploads')
app.config['UPLOADS'] = UPLOADS

@app.route('/')
def index():
  return render_template('productos/index_test.html')

# Vista de administración de produtcos. 
@app.route('/admin')
def admin():
  sql = "SELECT * FROM productos ORDER BY id DESC"
  conn = mysql.connection
  cursor = conn.cursor()
  cursor.execute(sql)
  productos = cursor.fetchall()
  conn.commit()
  
  return render_template('productos/admin.html', productos=productos)

# Vista de Agregar Nuevo prodcuto.
@app.route('/store', methods=['POST'])
def create():
  _titulo = request.form['titulo']
  _descripcion = request.form['descripcion']
  _precio = request.form['precio']
  _foto = request.files['foto']
  
  now = datetime.now()
  time = now.strftime("%Y%m%d_%H%M%S")
  
  if _foto.filename != '':
    fotoname = time + '_' + _foto.filename
    _foto.save("uploads/"+fotoname)
    
  sql = "INSERT INTO `productos` \
                (`titulo`, `descripcion`, `precio`, `foto`) \
                VALUES (%s, %s, %s, %s);"
  datos = (_titulo, _descripcion, _precio, fotoname)
  
  conn = mysql.connection
  cursor = conn.cursor()
  cursor.execute(sql, datos)
  conn.commit()
  
  return redirect('admin')

# Eliminar un producto
@app.route('/delete/<int:id>')
def delete(id):
  sql = "DELETE FROM productos WHERE id=%s;"
  conn = mysql.connection
  cursor = conn.cursor()
  cursor.execute(sql, (id,))
  conn.commit()
  
  return redirect('/admin')

@app.route('/editar/<int:id>')
def editar(id):
  sql = "SELECT * FROM productos WHERE id=%s;"
  conn = mysql.connection
  cursor = conn.cursor()
  cursor.execute(sql, (id,))
  productos = cursor.fetchall()
  conn.commit()
  
  return render_template('/productos/editar.html', productos = productos)

@app.route('/update', methods = ['POST'])
def update():
  _id = request.form['id']
  _titulo = request.form['titulo']
  _descripcion = request.form['descripcion']
  _precio = request.form['precio']
  _foto = request.files['foto']
  
  sql = "UPDATE productos SET titulo=%s, descripcion=%s, precio=%s WHERE id=%s;"
  datos = (_titulo, _descripcion, _precio, _id)
  
  conn = mysql.connection
  cursor = conn.cursor()
  cursor.execute(sql, datos)
  productos = cursor.fetchall()
  conn.commit()
  
  now = datetime.now()
  time = now.strftime("%Y%m%d_%H%M%S")
  
  if _foto.filename != '':
    fotoname = time + '_' + _foto.filename
    _foto.save("uploads/"+fotoname)
    cursor.execute("SELECT foto FROM productos WHERE id=%s", (_id,))
    fila = cursor.fetchone()
    if fila and fila[0] is not None:
      nombreAnterior = fila[0]
      rutaAnterior = os.path.join(app.config['UPLOADS'], nombreAnterior)
      if os.path.exists(rutaAnterior):
        os.remove(rutaAnterior)
    cursor.execute("UPDATE productos SET foto=%s WHERE id=%s;", (fotoname, _id,))
    conn.commit()
    cursor.close()

  
  return redirect('admin')

if __name__ == '__main__':
  app.run(debug = True)



