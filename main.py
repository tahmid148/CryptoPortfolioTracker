from typing import List
import databaseHelper
from classes.order import Order

def main():
    print("main")
    rows = databaseHelper.get_all_rows()
    print(rows[0].pair)

    databaseHelper.close_connection()



if __name__ == "__main__":
    main()
