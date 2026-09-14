
from app.schema import extract_schema
from app.integration.generator_with_rag import generate_sql_with_rag
from app.validator import validate_sql ,validate_table ,validate_column

question = "Quel est le chiffre d'affaires total ?"

context = """
Génère uniquement une requête SQL.
Ne fournis aucune explication.
Ne fournis aucun Markdown.

## Chiffre d'affaires
Le chiffre d'affaires d'une ligne de commande est calculé avec :
order_items.quantity * order_items.unit_price

Le chiffre d'affaires total est :
SUM(order_items.quantity * order_items.unit_price)

Les commandes annulées doivent être exclues.
"""

schema = extract_schema()

sql = generate_sql_with_rag(
    question=question,
    schema=schema,
    context=context
)

validate_sql(sql)
validate_table(sql, schema)
validate_column(sql, schema)

print("SQL RAG validé !")
print("\nSQL généré :")
print(sql)