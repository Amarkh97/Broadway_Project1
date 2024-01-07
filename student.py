from tables import connect
from all_functions import lend_status
from all_functions import available_books_info, book_query

def operations(conn):
    while True:
        print("\n0.Exit.. ")
        print("1. Search Book by name")
        print("2. Your Lend Status")
        try:

            choice= int(input("\nenter your choice"))

            if choice== 0:
                break
            elif choice== 1:
                name=input("\nenter book name:")
                book_query(conn,name)
                print("all available books...\n")
                available_books_info(conn)
            elif choice==2:
                sid=int(input("\nenter your sid: "))
                lend_status(conn,sid)
            else:
                print("invalid choice")
        
        except:
            print("illegal input..!!")


def main():
    """
    main function

    """
    conn= connect()
    try:
        operations(conn)
    except:
        print("db error")
#####################
    
if __name__ == "__main__":
    main()