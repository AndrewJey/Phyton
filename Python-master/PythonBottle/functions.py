import pymysql

def check_login(username, password, conection):
        result = False
        cursor = conection.cursor()
        select = ("SELECT * FROM user WHERE username='"+username+"' AND password='"+password+"'")
        cursor.execute(select)
        if not cursor.rowcount:
                result = False
        else:
                result = True
        cursor.close()
        return result


def all_products(conection):
    cursor = conection.cursor(pymysql.cursors.DictCursor)
    select = (" SELECT id,name,price FROM products ")
    cursor.execute(select)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def create_product(name, price, conection):
    cursor = conection.cursor()
    select = ("INSERT INTO products (name,price) values (%s, %s)")
    product_data=(name, price)
    cursor.execute(select, product_data)
    cursor.close()
    conection.commit()


def get_product_edit(id, conection):
        cursor = conection.cursor()
        select = ("SELECT * FROM products WHERE id='"+str(id)+"'")
        cursor.execute(select)
        rows=cursor.fetchall()
        form='<form action="/products/edit" method="post">'
        form=form+'<br/>'
        form=form+'Id: <input type="text" name="id" id="id" readonly value="'+str(rows[0][0])+'"/><br/>'
        form=form+'Name: <input type="text" name="name" id="name" value="'+str(rows[0][1])+'"/><br/>'
        form=form+'Price: <input type="text" name="price" id="price" value="'+str(rows[0][2])+'"/><br/>'
        form=form+'<input value="Edit" type="submit" class="btn" />'
        return form


def edit_product(id,name,price,conection):
    cursor = conection.cursor()
    select = ("UPDATE products SET name=%s,price=%s WHERE id=%s")
    product_data=(name, price,id)
    cursor.execute(select, product_data)
    cursor.close()
    conection.commit()

def delete_product(id,conection):
    cursor = conection.cursor()
    select = ("DELETE FROM products where id=%s")
    product_data=(id)
    cursor.execute(select, product_data)
    cursor.close()
    conection.commit()