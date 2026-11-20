from pathlib import Path
import sqlite3
import sys
import unittest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'Python-master' / 'Practicas'))
sys.path.insert(0, str(ROOT / 'Python-master' / 'PythonBottle'))

from OperacionesBasicas import Operaciones  # noqa: E402
import functions as bottle_fn  # noqa: E402


class _SqliteAdapterCursor:
    def __init__(self, cur):
        self._cur = cur

    def execute(self, sql, params=()):
        return self._cur.execute(sql.replace('%s', '?'), params)

    def fetchone(self):
        return self._cur.fetchone()

    def fetchall(self):
        return self._cur.fetchall()

    def close(self):
        self._cur.close()


class _SqliteAdapterConn:
    def __init__(self, conn):
        self._conn = conn

    def cursor(self):
        return _SqliteAdapterCursor(self._conn.cursor())

    def commit(self):
        self._conn.commit()


class OperacionesAndBottleTest(unittest.TestCase):
    def test_operaciones_basicas(self):
        self.assertEqual(Operaciones.ContarDigitos(0), 1)
        self.assertEqual(Operaciones.ContarDigitos(-9087), 4)
        self.assertEqual(Operaciones.Apariciones_Numero_enNumero(2, 21225), 3)
        self.assertEqual(Operaciones.Apariciones_Numero_enNumero(0, 0), 1)
        self.assertEqual(Operaciones.cambiarNumero(2, 9, 21225), 91995)
        self.assertEqual(Operaciones.cambiarNumero(0, 7, 0), 7)
        self.assertEqual(Operaciones.invertir(12345), 54321)
        self.assertEqual(Operaciones.invertir(-120), -21)

    def test_bottle_parameterized_crud_and_xss_escape(self):
        raw = sqlite3.connect(':memory:')
        raw.execute('CREATE TABLE user (username TEXT, password TEXT)')
        raw.execute('INSERT INTO user VALUES (?, ?)', ('admin', 'secret'))
        raw.execute('CREATE TABLE products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL)')
        conn = _SqliteAdapterConn(raw)

        self.assertTrue(bottle_fn.check_login('admin', 'secret', conn))
        self.assertFalse(bottle_fn.check_login("admin' OR '1'='1", 'wrong', conn))

        bottle_fn.create_product('<script>x</script>', 12.5, conn)
        rows = bottle_fn.all_products(conn)
        self.assertEqual(len(rows), 1)
        form_html = bottle_fn.get_product_edit(rows[0]['id'], conn)
        self.assertNotIn('<script>', form_html)
        self.assertIn('&lt;script&gt;', form_html)

        bottle_fn.edit_product(rows[0]['id'], 'Teclado', 25.0, conn)
        self.assertEqual(bottle_fn.all_products(conn)[0]['name'], 'Teclado')
        bottle_fn.delete_product(rows[0]['id'], conn)
        self.assertEqual(bottle_fn.all_products(conn), [])
        raw.close()


if __name__ == '__main__':
    unittest.main()
