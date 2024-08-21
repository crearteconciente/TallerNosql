import csv

# Cargar los datos desde los archivos CSV
with open('data/categorias.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    categorias = list(reader)

with open('data/productos.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    productos = list(reader)

categorias_dict={} # se construye  un diccionario
print("categorias") 
for categoria in categorias[:5]: #se recorre categorias
    print(categoria)
    categorias_dict[categoria['id']]={'nombre':categoria['modelo'],'productos':[]}
    
print(categorias_dict)

print('Productos')
productos_dict={}
for producto in  productos:
    productos_dict[producto['id']]= {producto['marca'],producto['precio'],producto['unidades_disponibles']}

union={[categorias_dict]:[productos_dict]}
print(union)