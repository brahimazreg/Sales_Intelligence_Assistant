from app.schema import extract_schema
from app.generator import generate_sql
from app.validator import validate_sql,validate_column,validate_table
from app.connection import execute_query


def question_to_sql(question):
    schema = extract_schema()

    sql_generated = generate_sql(question, schema)

    validate_sql(sql_generated)
    validate_table(sql_generated, schema)
    validate_column(sql_generated, schema)


    result = execute_query(sql_generated)

    return result

# Juste pour tester
if __name__ == "__main__":
    question = "Quels sont les 5 produits les plus vendus ?"

    result = question_to_sql(question)

    print("Résultat :")
    for row in result:
        print(row)

