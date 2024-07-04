# pythonisa-backend
[CaC 2024] Grupo 7 "Pythonisa" BACK END
  
  
  sql = "INSERT INTO `productos` \
              (`titulo`, `descripcion`, `precio`, `foto`) \
              VALUES( \
                      'Pncho de Lluvia Kite', \
                      'Diseñado para acompañar cualquier exploración, el poncho de lluvia Kite, es un poncho repelente al agua y resistente al viento para una protección ligera contra los elementos.', \
                      '0.00', \
                      'https://picsum.photos/200' \
                    )"
  conn = mysql.connection
  cursor = conn.cursor()
  cursor.execute(sql)
  conn.commit()