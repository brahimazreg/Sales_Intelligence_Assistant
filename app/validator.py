import sqlglot
from sqlglot import exp
from app.schema import extract_schema

def validate_sql(sql):
    if not sql or not sql.strip():
        raise ValueError("SQL query is empty")

    sql_clean = sql.strip()

    # Une seule requête
    try:
        statements = sqlglot.parse(sql_clean, read="mysql")
    except sqlglot.errors.ParseError as e:
        raise ValueError(f"Invalid SQL syntax: {e}") from e

    if len(statements) != 1:
        raise ValueError("Multiple SQL statements are not allowed")

    statement = statements[0]

    # SELECT ou WITH ... SELECT uniquement
    if not isinstance(statement, exp.Select):
        raise ValueError(
            "Only SELECT or WITH ... SELECT queries are allowed"
        )

    return sql_clean

def validate_table(sql, schema):
    statement = sqlglot.parse_one(sql, read="mysql")

    valid_tables = {table.lower() for table in schema}

    # Récupérer les noms des CTE
    cte_names = {
        cte.alias_or_name.lower()
        for cte in statement.find_all(exp.CTE)
    }

    for table in statement.find_all(exp.Table):
        table_name = table.name.lower()

        # Un CTE n'est pas une table physique du schéma
        if table_name in cte_names:
            continue

        if table_name not in valid_tables:
            raise ValueError(
                f"La table '{table_name}' n'existe pas dans le schéma"
            )

    return "Tables validées"

def validate_column(sql, schema):
    statement = sqlglot.parse_one(sql, read="mysql")

    # ---------------------------------------------------------
    # 1. Récupérer les CTE et leurs colonnes exposées
    # ---------------------------------------------------------
    cte_columns = {}

    for cte in statement.find_all(exp.CTE):
        cte_name = cte.alias_or_name.lower()

        cte_query = cte.this

        columns = set()

        for column in cte_query.find_all(exp.Column):
            # On récupère les colonnes utilisées dans le SELECT,
            # mais pas les colonnes des conditions JOIN/WHERE.
            pass

        select = cte_query.find(exp.Select)

        if select:
            for projection in select.expressions:
                if isinstance(projection, exp.Alias):
                    columns.add(projection.alias.lower())
                elif isinstance(projection, exp.Column):
                    columns.add(projection.name.lower())

        cte_columns[cte_name] = columns

    # ---------------------------------------------------------
    # 2. Construire alias -> table/CTE
    # ---------------------------------------------------------
    table_aliases = {}

    for table in statement.find_all(exp.Table):
        table_name = table.name
        table_alias = table.alias

        if table_alias:
            table_aliases[table_alias.lower()] = table_name
        else:
            table_aliases[table_name.lower()] = table_name

    # ---------------------------------------------------------
    # 3. Valider les colonnes
    # ---------------------------------------------------------
    for column in statement.find_all(exp.Column):
        column_name = column.name.lower()
        table_alias = column.table

        if not table_alias:
            continue

        resolved_name = table_aliases.get(table_alias.lower())

        if not resolved_name:
            raise ValueError(
                f"L'alias '{table_alias}' ne correspond à aucune table"
            )

        # CTE
        if resolved_name.lower() in cte_columns:
            if column_name not in cte_columns[resolved_name.lower()]:
                raise ValueError(
                    f"La colonne '{column.name}' n'existe pas "
                    f"dans la CTE '{resolved_name}'"
                )
            continue

        # Table physique
        table_schema = schema.get(resolved_name)

        if not table_schema:
            raise ValueError(
                f"La table '{resolved_name}' n'existe pas dans le schéma"
            )

        schema_columns = {
            col["name"].lower()
            for col in table_schema["columns"]
        }

        if column_name not in schema_columns:
            raise ValueError(
                f"La colonne '{column.name}' n'existe pas "
                f"dans la table '{resolved_name}'"
            )