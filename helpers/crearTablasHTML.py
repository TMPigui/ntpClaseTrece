def crearTabla(dataFrame, nombreTabla):
    archivoHTML = dataFrame.to_html() #dataframe version html
    archivo = open(f"./tablas/{nombreTabla}.html","w") #archivo html vacio
    archivo.write('''
        <!DOCTYPE html>
        <html>
        <head>
        <title>tablas</title>
        <meta charset="UTF-8">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        </head>
        <body>

    ''') 
    archivo.write(archivoHTML)
    archivo.write(''' 
        </body>
        </html> 
       ''')
    archivo.close() # siempre lo debemos cerrar