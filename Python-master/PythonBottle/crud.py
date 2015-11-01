from bottle import route, run,redirect,get, post, request,template,response
from functions import check_login,all_products,create_product,get_product_edit,edit_product,delete_product
from conection import conectar
from json import dumps

conection=conectar()

@route('/')

@get('/login')
def login():
    return template('Templates/index.tpl')

@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password, conection):
        redirect("/products")
    else:
        return "<p>Login failed.</p>"


@get('/products')
def products():
    return template('Templates/products.tpl')

@get('/products.json')
def products():
    table=all_products(conection)
    response.content_type = 'application/json'
    return dumps(table)

@get('/products/create')
def products_create():
    return template('Templates/create.html')

@post('/products/create')
def do_products_create():
    name = request.forms.get('name')
    price = request.forms.get('price')
    create_product(name, price, conection)
    redirect("/products")

@get('/products/edit/<ID>')
def products_edit(ID):
    form= get_product_edit(ID,conection)
    return template('Templates/edit_product.tpl',form=form)

@post('/products/edit')
def do_products_edit():
    id = request.forms.get('id')
    name = request.forms.get('name')
    price = request.forms.get('price')
    edit_product(id,name,price,conection)
    redirect("/products")

@get('/products/delete/<ID>')
def products_delete(ID):
    return template('Templates/delete_product.tpl', id=ID)

@post('/products/delete')
def do_products_delete():
    id = request.forms.get('id')
    delete_product(id,conection)
    redirect("/products")


run(host='localhost', port=8080, debug=True)


