from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

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

mysql.init_app(app)

@app.route('/')
def index():
  return render_template('productos/index_test.html')


@app.route('/admin')
def admin():
  sql = "SELECT * FROM productos"
  conn = mysql.connection
  cursor = conn.cursor()
  cursor.execute(sql)
  productos = cursor.fetchall()
  conn.commit()
  
  return render_template('productos/admin.html', productos=productos)

if __name__ == '__main__':
  app.run(debug = True)



