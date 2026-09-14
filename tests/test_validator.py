import sqlglot
from sqlglot import exp
from app.validator import validate_sql, validate_table,validate_column
from app.schema import extract_schema

def test_valid_select():
    sql = "SELECT * FROM customers"
    result = validate_sql(sql)

    print("SELECT valide :")
    print(result)


def test_valid_with():
    sql = """
    WITH customer_count AS (
        SELECT COUNT(*) AS total
        FROM customers
    )
    SELECT total
    FROM customer_count
    """

    result = validate_sql(sql)

    print("\nWITH valide :")
    print(result)


def test_forbidden_drop():
    try:
        validate_sql("DROP TABLE customers")
        print("\nERREUR : DROP aurait dû être refusé")
    except ValueError as e:
        print("\nDROP correctement refusé :", e)


def test_forbidden_delete():
    try:
        validate_sql("DELETE FROM customers WHERE customer_id=1")
        print("\nERREUR : DELETE aurait dû être refusé")
    except ValueError as e:
        print("\nDELETE correctement refusé :", e)


def test_multiple_statements():
    try:
        validate_sql("SELECT * FROM customers; DROP TABLE customers")
        print("\nERREUR : plusieurs requêtes auraient dû être refusées")
    except ValueError as e:
        print("\nPlusieurs requêtes correctement refusées :", e)


def test_forbidden_update():
    try:
        validate_sql(
            "UPDATE customers SET email='xxx@xy.com' WHERE customer_id=1"
        )
        print("\nERREUR : UPDATE aurait dû être refusé")
    except ValueError as e:
        print("\nUPDATE correctement refusé :", e)


def test_forbidden_insert():
    try:
        validate_sql(
            "INSERT INTO customers (company_name) VALUES ('Test')"
        )
        print("\nERREUR : INSERT aurait dû être refusé")
    except ValueError as e:
        print("\nINSERT correctement refusé :", e)


def test_word_inside_string():
    sql = "SELECT product_name FROM products WHERE product_name = 'DROP'"

    try:
        result = validate_sql(sql)
        print("\nMot interdit dans une chaîne correctement accepté :")
        print(result)
    except ValueError as e:
        print("\nERREUR :", e)


# --------------------------------------------------
# Tests validate_table()
# --------------------------------------------------

def test_existing_table():
    schema = [
        "customers",
        "sales_reps",
        "categories",
        "suppliers",
        "products",
        "orders",
        "order_items"
    ]

    sql = "SELECT * FROM products"

    result = validate_table(sql, schema)

    print("\nTable existante correctement validée :")
    print(result)


def test_multiple_existing_tables():
    schema = [
        "customers",
        "sales_reps",
        "categories",
        "suppliers",
        "products",
        "orders",
        "order_items"
    ]

    sql = """
    SELECT *
    FROM products p
    JOIN categories c
        ON p.category_id = c.category_id
    """

    result = validate_table(sql, schema)

    print("\nPlusieurs tables existantes correctement validées :")
    print(result)


def test_unknown_table():
    schema = [
        "customers",
        "sales_reps",
        "categories",
        "suppliers",
        "products",
        "orders",
        "order_items"
    ]

    sql = "SELECT * FROM unknown_table"

    try:
        validate_table(sql, schema)

        print("\nERREUR : unknown_table aurait dû être refusée")

    except ValueError as e:
        print("\nTable inconnue correctement refusée :", e)


def test_mixed_existing_and_unknown_tables():
    schema = [
        "customers",
        "sales_reps",
        "categories",
        "suppliers",
        "products",
        "orders",
        "order_items"
    ]

    sql = """
    SELECT *
    FROM products p
    JOIN unknown_table u
        ON p.product_id = u.product_id
    """

    try:
        validate_table(sql, schema)

        print("\nERREUR : unknown_table aurait dû être refusée")

    except ValueError as e:
        print("\nTable inconnue correctement refusée :", e)


def test_table_case_insensitive():
    schema = [
        "customers",
        "products"
    ]

    sql = "SELECT * FROM PRODUCTS"

    result = validate_table(sql, schema)

    print("\nNom de table insensible à la casse :")
    print(result)
def test_column():
    schema = [ "products"  ]
    sql = """
    SELECT p.product_name
    FROM products p
    """
    result = validate_column(sql, schema)
    statement = sqlglot.parse_one(
        """
        SELECT p.product_name
        FROM products p
        JOIN categories c
            ON p.category_id = c.category_id
        """,
        read="mysql"
    )

    for table in statement.find_all(exp.Table):
        print("table.name :", table.name)
        print("table.alias:", table.alias)
        print("---")

def test_existing_column_with_alias():
    schema = extract_schema()

    sql = """
    SELECT p.product_name
    FROM products p
    """

    result = validate_column(sql, schema)

    print("\nColonne existante correctement validée :")
    print(result)


def test_unknown_column_with_alias():
    schema = extract_schema()

    sql = """
    SELECT p.unknown_column
    FROM products p
    """

    try:
        validate_column(sql, schema)

        print("\nERREUR : unknown_column aurait dû être refusée")

    except ValueError as e:
        print("\nColonne inconnue correctement refusée :", e)

def test_column():
    schema = extract_schema()

    sql = """
    SELECT p.product_name
    FROM products p
    """

    result = validate_column(sql, schema)

    print("\nColonne existante correctement validée :")
    print(result)

def test_unknown_column():
    schema = extract_schema()

    sql = """
    SELECT p.unknown_column
    FROM products p
    """

    try:
        validate_column(sql, schema)

        print("\nERREUR : unknown_column aurait dû être refusée")

    except ValueError as e:
        print("\nColonne inconnue correctement refusée :", e)

def main():
    test_valid_select()
    test_valid_with()
    test_forbidden_drop()
    test_forbidden_delete()
    test_multiple_statements()
    test_forbidden_update()
    test_forbidden_insert()
    test_word_inside_string()

    test_existing_table()
    test_multiple_existing_tables()
    test_unknown_table()
    test_mixed_existing_and_unknown_tables()
    test_table_case_insensitive()
    test_column()
    test_existing_column_with_alias()
    test_unknown_column_with_alias()
    test_unknown_column()
    test_column()

if __name__ == "__main__":
    main()