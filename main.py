path = os.path.join(pathlib.Path().resolve(),'tool\chromedriver.exe')
connection = Connection(path)
print(connection.load('https://google.com'))