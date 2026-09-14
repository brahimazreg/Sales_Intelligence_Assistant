from app.schema import extract_schema


def main():

    schema = extract_schema()

    for table, info in schema.items():

        print(f"\nTABLE: {table}")

        print("  Columns:")

        for column in info["columns"]:
            print(
                f"    - {column['name']} "
                f"({column['type']})"
            )

        print(
            f"  Primary key: "
            f"{info['primary_key']}"
        )

        print("  Foreign keys:")

        for fk in info["foreign_keys"]:
            print(
                f"    - {fk['column']} "
                f"→ {fk['references_table']}."
                f"{fk['references_column']}"
            )


if __name__ == "__main__":
    main()