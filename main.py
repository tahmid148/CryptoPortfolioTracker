import databaseHelper
from classes.order import Order

def main():
    print("main")
    df = databaseHelper.get_all_rows()
    print(df)

    databaseHelper.close_connection()



if __name__ == "__main__":
    main()
