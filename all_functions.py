from tables import connect, create_table



#functions to be carried out by a librarian for student

def add_student(conn, name):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO student (name) VALUES (?)', (name,))
    conn.commit()
    cursor.execute('SELECT LAST_INSERT_ROWID()')
    sid = cursor.fetchone()[0]
    print("sid: ",sid)

def retrieve_students(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student')
    return cursor.fetchall()

def retrieve_a_student(conn, id):
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM student WHERE sid = ?', (id,))
    print( cursor.fetchone())
    

def delete_a_student(conn, id):
    cursor= conn.cursor()
    cursor.execute('select name from student where sid=? ',(id,))
    name= cursor.fetchone()[0]
    cursor.execute('DELETE FROM student WHERE sid = ?', (id,))
    conn.commit()
    print(id,name,"deleted !!")

def update_a_student(conn, id,new_name):
    cursor= conn.cursor()
    cursor.execute('UPDATE student SET name = ? WHERE sid = ?', (new_name, id))
    conn.commit()
    print(id,"'s name changed to: ", new_name)


#functions to operate on books by librarian

def add_a_book(conn,name,quantity):
    cursor= conn.cursor()
    cursor.execute('INSERT INTO books (book_name, available_quantity) VALUES (?,?)',(name, quantity))
    conn.commit()

def available_books_info(conn):
    #this function is available at mode==2; choice==100
    cursor= conn.cursor()
    cursor.execute('select * from books')
    data=cursor.fetchall()
    for i in data:
        print(i)
    print("========================================================================================")
def delete_books(conn, ids):
    """
    Delete books from the system based on a list of book IDs.

    Parameters:
    - conn (sqlite3.Connection): The SQLite database connection.
    - ids (list): A list of book IDs to be deleted.

    Returns:
    None
    """
    try:
        cursor = conn.cursor()

        for book_id in ids:
            cursor.execute('DELETE FROM books WHERE id=?', (book_id,))
            conn.commit()
            print(f"Book with ID {book_id} deleted")

        print("Books deleted successfully!")

    except Exception as e:
        print(f"Error deleting books: {e}")

# def delete_books(conn, ids):
    
#     # try:

#         for id in ids:
#             cursor= conn.cursor()
#             cursor.execute('DELETE FROM books WHERE id=?',(id,))
#             conn.commit()
#             print("1 book deleted")
#         print("BOOKS DELETED..!!")
    # except:
        print("ERror..!!")

def update_books(conn,new_name,id,quantity):
    cursor=conn.cursor()
    cursor.execute('UPDATE books SET book_name=?, available_quantity=?  WHERE id=?',(new_name,quantity,id))
    conn.commit()
    print("updated..!!")
def book_query(conn,name):
    try:
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM books WHERE book_name=?',(name,))
        book=cursor.fetchall()
        if book:
            for i in book:
                print("\nBOOK FOUND")
                print("BOOK id:",i[0])
                
                print("BOOK available quantity",i[2])
                print("=============================================================================")

        else:
            print("Book N/A")
    except:
        print("Error searching books")


#functions to operate by librarian for lend_record
    
def lend_book(conn,book_id,student_id):
    cursor=conn.cursor()
    cursor.execute('INSERT INTO lend_record (book_id, student_id) VALUES (?,?)',(book_id,student_id))
    conn.commit()
    cursor.execute('update books set available_quantity=available_quantity-1 where id=?',(book_id,))
    conn.commit()
def lend_status(conn,student_id):
    cursor= conn.cursor()
    cursor.execute(
"""
select lend_record.id as lend_id,
       books.book_name,
       student.name,
       lend_record.return_status

from lend_record 
inner join books on lend_record.book_id = books.id
inner join student on lend_record.student_id =student.sid     
       
where lend_record.student_id = ?

""", (student_id,)
    )
    data= cursor.fetchall()
    if data:   
        for i in data:
            print(i)
    else:
        print("no data found..!!")
def lend_record(conn):
    cursor=conn.cursor()
    cursor.execute(
"""
select lend_record.id as lend_id,
       books.book_name,
       student.name,
       lend_record.return_status

from lend_record 
inner join books on lend_record.book_id = books.id
inner join student on lend_record.student_id =student.sid     
       

"""
    )
    
    data = cursor.fetchall()
    
    for i in data:
            print(i)
    
def return_book(conn,sid,bid):
    cursor= conn.cursor()
    cursor.execute('update lend_record set return_status=1 where student_id=? and book_id=?', (sid,bid))
    cursor.execute('update books set available_quantity=available_quantity+1 where id=?',(bid,))
    
    conn.commit()




