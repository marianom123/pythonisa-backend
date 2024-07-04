from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexión a la DB:
mysql = MySQL()

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sistema'

mysql.init_app(app)

@app.route('/')
def index():
  sql_insert = "INSERT INTO `productos` \
              (`id`, `titulo`, `descripcion`, `precio`, `foto`) \
              VALUES( \
                    NULL, \
                    'Pncho de Lluvia Kite', \
                    'Diseñado para acompañar cualquier exploración, el poncho de lluvia Kite, es un poncho repelente al agua y resistente al viento para una protección ligera contra los elementos.', \
                    '0.00', \
                    'https://picsum.photos/200' \
                    )"
  conn = mysql.connection
  cursor = conn.cursor()
  cursor.execute(sql_insert)
  conn.commit()
  
  return render_template('productos/index_test.html')

if __name__ == '__main__':
  app.run(debug = True)
