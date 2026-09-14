from app.generator import generate_sql
from app.schema import extract_schema


def main():

    schema = extract_schema()

    question = "Quels sont les 5 produits les plus vendus ?"

    print("Question :", question)
    print("Génération du SQL...")

    sql = generate_sql(question,schema)

    print("\nSQL généré :")
    print(sql)

 
    print("\nPrésence de LIMIT 5 :")
    print("LIMIT 5" in sql.upper())


if __name__ == "__main__":
    main()
