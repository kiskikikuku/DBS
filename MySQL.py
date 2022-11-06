import pymysql

db = pymysql.connect(host='192.168.56.101', user='thpark', password='xogus99', port=4567, db='madang', charset='utf8')

cursor = db.cursor()

while 1:
    print("-----------[2018068040]----------------[Taehyunpark]----------")
    print("[Bookstore Management System]")
    print("1. Insert Book")
    print("2. Delete Book")
    print("3. Search Book")
    print("4. Print Book DB")
    print("5. Exit(Input Any value (except 1,2,3,4)")
    print("--------------------------------------------------------------")
    menu = int(input())
    if menu == 1:
        sql = "INSERT INTO Book (bookid, bookname, publisher, price) VALUES(%s, %s, %s, %s)"
        print("삽입할 책의 정보를 순서대로 입력(bookid, bookname, publisher, price: )")
        bookid = int(input())
        bookname = str(input())
        publisher = str(input())
        price = int(input())
        cursor.execute(sql, (bookid, bookname, publisher, price))
    elif menu == 2:
        sql = "DELETE FROM Book WHERE bookname = %s"
        print("삭제할 책의 이름을 입력하세요: ")
        deleteBookname = str(input())
        cursor.execute(sql, deleteBookname)
        db.commit()

    elif menu == 3:
        sql = "SELECT * FROM Book WHERE bookname = %s"
        print("검색할 책의 이름을 입력하세요: ")
        searchBook = str(input())
        cursor.execute(sql, searchBook)
        result = cursor.fetchall()
        for data in result:
            print(data)
    elif menu == 4:
        sql = "SELECT * FROM Book"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row_data in result:
            print(row_data)

    else:
        break
    db.commit()



