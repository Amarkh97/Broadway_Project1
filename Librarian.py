
from tables import create_table, connect
from all_functions import add_student, delete_a_student, retrieve_students, update_a_student,retrieve_a_student
from all_functions import book_query, add_a_book, delete_books, update_books,available_books_info
from all_functions import lend_book, lend_status, lend_record,return_book

############################################################################################################################
def main():
    """
    main function

    """
    conn= connect()
    create_table(conn)
    operations(conn)
############################################################################################################################   
def operations(conn):
    while True:
        """
        operations to be executed by the librarian according to the mode required
        choices are given for how to operate as

        parameters: 
        conn: connection with db
        

        """
        print("====================================================")
        print("\n0. Exit")
        print ("1. FOR STUDENT MANAGEMENT ROLE")
        print ("2. FOR BOOKS MANAGEMENT ROLE")
        print ("3. FOR LEND_RECORD MANAGEMENT ROLE")
        print("====================================================")
        try:

            mode= int(input("\nSELECT YOUR CURRENT OPERATING ROLE: "))
            if mode==0:
                break
            elif mode ==1:
                print("0.Exit ")
                print("1. to add a new student")
                print("2. to delete a student record")
                print("3. to retrieve all student records")
                print("4. to update student info")
                print("5. to retreive single student info")
                print("====================================================")

                

                

                try:
                    choice= int(input("enter your choice: "))

                    if choice==0:
                        break
                    elif choice==1:
                        name=input("new student name: ")
                        add_student(conn,name)
                    elif choice==2:
                        id=int(input("enter student id to delete record: "))
                        delete_a_student(conn,id)
                    elif choice==3:
                        data = retrieve_students(conn)
                        for i in data:
                            print(i)
                    elif choice==4:
                        id= int(input("enter student id you want to update: "))
                        name= input("new name to rename: ")
                        update_a_student(conn, id , name)
                    elif choice==5:
                        id=int(input("enter student id to view info: "))
                        retrieve_a_student(conn,id)
                    else:
                        print("Invalid Choice..!!")

                except:
                    print("illegal input!!")
            
            elif mode==2:
                print("\n0. Exit")
                print("1. Add Book")
                print("2. Retrieve Books")
                print("3. Delete Books")
                print("4. Update Books")
                print("5. Book query by name/ Book Search")


                try:
                    choice = int(input("Enter your choice: "))
                    if choice == 0:
                        break
                    
                    
                    elif choice == 1:
                        name = input("Enter book name: ")
                        
                        quantity = int(input("Enter quantity: "))
                        add_a_book(conn, name, quantity)
                    
                    elif choice == 3:
                        book_id=[]
                        while True:
                            try:
                                st = input("Enter id to delete: ")
                                if st == "Q":
                                    break
                                else:
                                    book_id.append(int(st))
                            except:
                                print('Invalid Id')
                        delete_books(conn, book_id)
                    
                    elif choice== 2:
                        data =available_books_info(conn)
                        for i in data:
                            print(i)

                    elif choice == 4:
                        book_id = int(input("Enter book ID to update: "))
                        new_name = input("Enter new name: ")
                        quantity = int(input("Enter new quantity: "))
                        update_books(conn,new_name, book_id,quantity)
                    elif choice==5:
                        name= input("\nenter name of book you want to check info of: ")
                        book_query(conn,name)
                    else:
                        print("invalid choice")
                except:
                    print("illegal input..!!")
            
            
            elif mode== 3:
                print("\n0. Exit")
                print("1. Lend book")
                print("2. Lend Status by Student ID")
                print("3. View Overall Lend record")
                print("4. Return book")
                print("====================================================")
                try:
                    choice=int(input("\nenter your choice: "))
                    if choice==0:
                        break
                    elif choice==1:
                        # try:
                            sid=int(input("\nEnter Student Id: "))
                            book_id=int(input("Enter book Id: "))
                            lend_book(conn, book_id, sid)
                            
                        # except:
                        #     print("illegal input..!!")
                    elif choice==2:
                        sid=int(input("\nenter your student id: "))
                        lend_status(conn,sid)
            
            
                    elif choice==3:
                        lend_record(conn)
                    


                    elif choice==4:
                        sid=int(input("enter your student id: "))
                        bid=int(input("enter your book id: "))

                        return_book(conn,sid,bid)
                

                    else:
                        print("invalid choice..!!")

                except:
                    print("\nillegal input..!!")

            else:
                print("invalid mode..!!")
        
        
        except:
             print("illegal Input..!!")





#####################################################################################
if __name__ == "__main__":
    main()