import pymysql

db = pymysql.connect(host='192.168.56.101', user='thpark', password='xogus99', port=4567, db='LCK_db', charset='utf8')

cursor = db.cursor()

while 1:
    print("-----------[2018068040]----------------[Taehyunpark]----------")
    print("[LCK Viewer(E-Sports)]")
    print("1. Add Player")
    print("2. Delete Player")
    print("3. Search Player")
    print("4. Add Coaching Staff")
    print("5. Delete Coaching Staff")
    print("6. Search Player")
    print("7. Search Team")
    print("6. Print DB")
    print("Others. Exit(Input Any value (except 1,2,3,4)")
    print("--------------------------------------------------------------")
    command = int(input())
    if command == 1: #선수 입력
        sql = "INSERT INTO player (summoner_ID, firstname, lastname, line, birth, age, team, salary, expiration) VALUES(%s, %s, %s, %s)"
        print("Enter the information of [player] you want to insert in order(summoner_ID, firstname, lastname, line, birth, age, team, salary, expiration)")
        id = str(input())
        fname = str(input())
        lname = str(input())
        line = str(input())
        birth = str(input())
        age = str(input())
        team = str(input())
        salary = str(input())
        expiration = str(input())
        cursor.execute(sql, (id, fname, lname, line, birth, age, team, salary, expiration))

    elif command == 2: #선수 제거
        sql = "DELETE FROM player WHERE summoner_ID = %s"
        print("Input Summoner ID of player you want delete:  ")
        id = str(input())
        cursor.execute(sql, id)
        db.commit()

    elif command == 3: #선수 검색
        sql = "SELECT * FROM Book WHERE bookname = %s"
        print("Input Summoner ID of player you want search: ")
        searchPlayer = str(input())
        cursor.execute(sql, searchPlayer)
        result = cursor.fetchall()

    elif command == 4:

    elif command == 7: #팀 검색
        sql = "SELECT * FROM player"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row_data in result:
            print(row_data)
        sql2 = "SELECT * FROM coaching_staff"
        cursor.execute(sql2)
        result = cursor.fetchall()
        for row_data in result:
            print(row_data)

    else:
        break

