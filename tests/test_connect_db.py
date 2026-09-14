from app.connection import connect_database,execute_query


def main():
    response=execute_query("SELECT * FROM orders")       
    for row in response:
                print(row)    
if __name__ == "__main__":
    main()