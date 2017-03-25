import web

#db_host = 'localhost';
#db_name = 'store';
#db_user = 'root';
#db_pw = '';

db = web.database(
			dbn='mysql',
			host='if0ck476y7axojpg.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
			db='vzvh9nyml6fld1d9',
			user='twoz5kghnry9241t',
			pw='ifxg7id1n56pvvc2'
			)

def get_posts():
	try:
		return db.select('productos')
	except:
		return None

def get_post(id):
	try: 
		return db.select('productos', where ='id_producto=$id', vars=locals())[0]
	except IndexError:
		return None

def new_post(producto, descripcion, existencias, precio_compra, precio_venta,imagen_producto):
		db.insert('productos', producto=producto, descripcion=descripcion, existencias=existencias, 
		precio_compra=precio_compra, precio_venta=precio_venta, imagen_producto=imagen_producto)

def delete_post(id):
	db.delete('productos', where ='id_producto=$id', vars=locals())

def update_post(id, producto, descripcion, existencias, precio_compra, precio_venta, imagen_producto): #modificar
		db.update('productos', where="id_producto=$id", vars=locals(), producto=producto, descripcion=descripcion, 
		existencias=existencias, precio_compra=precio_compra, precio_venta=precio_venta, imagen_producto=imagen_producto)

#productos = get_productos()
	#for item in productos:
	#	print item.id_producto
	#	print item.producto
	#	print item.descripcion
	#	print item.existencias
	#	print item.precio_compra
	#	print item.precio_venta
