import html


def check_login(username, password, conection):
    cursor = conection.cursor()
    try:
        cursor.execute(
            'SELECT 1 FROM user WHERE username = %s AND password = %s',
            (username, password),
        )
        return cursor.fetchone() is not None
    finally:
        cursor.close()


def all_products(conection):
    cursor = conection.cursor()
    try:
        cursor.execute('SELECT id, name, price FROM products ORDER BY id')
        rows = cursor.fetchall()
        if rows and isinstance(rows[0], dict):
            return rows
        return [{'id': r[0], 'name': r[1], 'price': r[2]} for r in rows]
    finally:
        cursor.close()


def create_product(name, price, conection):
    cursor = conection.cursor()
    try:
        cursor.execute('INSERT INTO products (name, price) VALUES (%s, %s)', (name, price))
        conection.commit()
    finally:
        cursor.close()


def get_product_edit(product_id, conection):
    cursor = conection.cursor()
    try:
        cursor.execute('SELECT id, name, price FROM products WHERE id = %s', (product_id,))
        row = cursor.fetchone()
    finally:
        cursor.close()
    if row is None:
        return '<p>Producto no encontrado.</p>'
    pid = html.escape(str(row[0] if not isinstance(row, dict) else row['id']), quote=True)
    name = html.escape(str(row[1] if not isinstance(row, dict) else row['name']), quote=True)
    price = html.escape(str(row[2] if not isinstance(row, dict) else row['price']), quote=True)
    return (
        '<form action="/products/edit" method="post">'
        f'<label>Id: <input type="text" name="id" id="id" readonly value="{pid}"/></label><br/>'
        f'<label>Name: <input type="text" name="name" id="name" required value="{name}"/></label><br/>'
        f'<label>Price: <input type="number" step="any" name="price" id="price" required value="{price}"/></label><br/>'
        '<input value="Edit" type="submit" class="btn" />'
        '</form>'
    )


def edit_product(product_id, name, price, conection):
    cursor = conection.cursor()
    try:
        cursor.execute('UPDATE products SET name = %s, price = %s WHERE id = %s', (name, price, product_id))
        conection.commit()
    finally:
        cursor.close()


def delete_product(product_id, conection):
    cursor = conection.cursor()
    try:
        cursor.execute('DELETE FROM products WHERE id = %s', (product_id,))
        conection.commit()
    finally:
        cursor.close()
