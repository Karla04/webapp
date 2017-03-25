import web
import model
        
urls = (
    '/', 'Index',
    '/ver/(\d+)','Ver',
    '/delete/(\d+)', 'Delete',
    '/modificar/(\d+)','Modificar',
    '/borrar/(\d+)','Borrar',
    '/insertar','Insertar'
    )

t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates', base='master', globals=t_globals)

class Index:
    def GET(self):
        posts = model.get_posts()
        return render.index(posts)

class Ver:
    def GET(self, id):
        post = model.get_post(int(id))
        return render.ver(post)

class Borrar:
    def GET(self, id):
        post = model.get_post(int(id))
        return render.borrar(post)
    
    def POST(self, id):
        model.delete_post(int(id))
        raise web.seeother('/')

class Delete:
    def POST(self, id):
        model.delete_post(int(id))
        raise web.seeother('/')

class Insertar:
    form = web.form.Form(
        web.form.Textbox('producto', web.form.notnull, size=30, description="Producto:"),
        web.form.Textarea('descripcion', web.form.notnull, rows=4, cols=32, description="Descripcion:"),
        web.form.Textbox('existencias', web.form.notnull, size=30, description="Existencias:"),
        web.form.Textbox('precio_compra', web.form.notnull, size=30, description="Precio Compra:"),
        web.form.Textbox('precio_venta', web.form.notnull, size=30, description="Precio Venta:"),
        web.form.File('imagen_producto', web.form.notnull, size=30, description="Imagen del Producto:"),
        web.form.Button('Guardar Producto'),
    )

    def GET(self):
        form = self.form()
        return render.insertar(form)

    def POST(self):
        form = self.form()
        imagen = web.input(imagen_producto={})
        filedir = 'static/files'
        filepath = imagen.imagen_producto.filename.replace('\\','/')
        filename = filepath.split('/')[-1]
        #copiar archivo al servidor
        fout= open(filedir+'/'+filename,'w')
        fout.write(imagen.imagen_producto.file.read())
        fout.close()
        imagen_producto = filename
        if not form.validates():
            return render.insertar(form)
        model.new_post(form.d.producto, form.d.descripcion,form.d.existencias, form.d.precio_compra, form.d.precio_venta, imagen_producto)
        raise web.seeother('/')

class Modificar:
    def GET(self, id):
        post = model.get_post(int(id))
        form = Insertar.form()
        form.fill(post)
        return render.modificar(post, form)

    def POST(self, id):
        form = Insertar.form()
        imagen = web.input(imagen_producto={})
        filedir = 'static/files'
        filepath = imagen.imagen_producto.filename.replace('\\','/')
        filename=  filepath.split('/')[-1]
        #copiar archivo al servidor
        fout = open(filedir+'/'+filename,'w')
        fout.write(imagen.imagen_producto.file.read())
        fout.close()
        imagen_producto = filename
        post = model.get_post(int(id))
        if not form.validates():
            return render.modificar(post, form)
        model.update_post(int(id), form.d.producto, form.d.descripcion,form.d.existencias, form.d.precio_compra, form.d.precio_venta, imagen_producto)
        raise web.seeother('/')

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
