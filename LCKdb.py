# import pymysql
#
# db = pymysql.connect(host='192.168.56.101', user='thpark', password='xogus99', port=4567, db='LCK_db', charset='utf8')
#
# cursor = db.cursor()

while 1:
    print("-----------[2018068040]----------------[Taehyunpark]----------")
    print("[LCK Viewer(E-Sports)]")
    print("1. Insert Data")
    print("2. Delete Data")
    print("3. Search Data")
    print("4. Print DB")
    print("Others. Exit(Input Any value (except 1,2,3,4)")
    print("--------------------------------------------------------------")
    command = int(input())
    if command == 1:
        sql = "INSERT INTO Book (bookid, bookname, publisher, price) VALUES(%s, %s, %s, %s)"
        print("삽입할 책의 정보를 순서대로 입력(bookid, bookname, publisher, price: )")
        bookid = int(input())
        bookname = str(input())
        publisher = str(input())
        price = int(input())
        # cursor.execute(sql, (bookid, bookname, publisher, price))
    elif command == 2:
        sql = "DELETE FROM Book WHERE bookname = %s"
        print("Input Summoner ID you want delete:  ")
        deleteBookname = str(input())
        # cursor.execute(sql, deleteBookname)
        # db.commit()

    elif command == 3:
        sql = "SELECT * FROM Book WHERE bookname = %s"
        print("검색할 책의 이름을 입력하세요: ")
        searchBook = str(input())
        # cursor.execute(sql, searchBook)
        # result = cursor.fetchall()

    elif command == 4:
        sql = "SELECT * FROM Book"
        # cursor.execute(sql)
        # result = cursor.fetchall()
        # for row_data in result:
        #     print(row_data)
    else:
        break

