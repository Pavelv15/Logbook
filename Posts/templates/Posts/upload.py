import os, cgi

data = cgi.FieldStorage()

upload = data['filename']

filename = os.path.basename(upload.filename)

with open(filename,'wb') as f:
    f.write(upload.file.read())

print('<html>')
print('<head>')
print('<title>Загрузка выполена</title>')
print('</head>')
print('<body>')
print('<h1>Всё</h1>')
print('</body>')
print('</html>')
