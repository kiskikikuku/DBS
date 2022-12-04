import pymysql

db = pymysql.connect(host='192.168.56.101', user='thpark', password='xogus99', port=4567, db='LCK_db', charset='utf8')

cursor = db.cursor()

while 1:
    print("-----------[2018068040]----------------[Taehyunpark]----------")
    print("[LCK Team Contract Viewer]")
    print("1. Add Player")
    print("2. Delete Player")
    print("3. Search Player")
    print("4. Add Coaching Staff")
    print("5. Delete Coaching Staff")
    print("6. Search Player")
    print("7. Search Team")
    print("Exit: Input Any other keys")
    print("--------------------------------------------------------------")
    command = int(input())
    if command == 1: #선수 입력
        sql = "INSERT INTO player (summoner_ID, firstname, lastname, line, birth, age, team, salary, expiration) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
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

    elif command == 3: #선수 검색
        sql = "SELECT * FROM player WHERE summoner_ID = %s"
        print("Input Summoner ID of player you want search: ")
        searchPlayer = str(input())
        cursor.execute(sql, searchPlayer)
        result = cursor.fetchall()
        for data in result:
            print(data)

    elif command == 4: #코칭스태프 추가
        sql = "INSERT INTO coaching_staff (summoner_ID, firstname, lastname, role, birth, age, team, expiration) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        print(
            "Enter the information of [coachingstaff] you want to insert in order(summoner_ID, firstname, lastname, role, birth, age, team, expiration)")
        id = str(input())
        fname = str(input())
        lname = str(input())
        role = str(input())
        birth = str(input())
        age = str(input())
        team = str(input())
        expiration = str(input())
        cursor.execute(sql, (id, fname, lname, role, birth, age, team, expiration))

    elif command == 5: #코칭스태프 제거
        sql = "DELETE FROM coaching_staff WHERE summoner_ID = %s"
        print("Input Summoner ID of [coaching_staff] you want delete:  ")
        deleteCoach = str(input())
        cursor.execute(sql, deleteCoach)

    elif command == 6: #코칭스태프 검색
        sql = "SELECT * FROM coaching_staff WHERE summoner_ID = %s"
        print("Input Summoner ID of [coaching_staff] you want search:  ")
        searchCoach = str(input())
        cursor.execute(sql, searchCoach)
        result = cursor.fetchall()
        for data in result:
            print(data)

    elif command == 7: #팀 검색
        sql = "SELECT * FROM player WHERE team = %s"
        searchteam = str(input())
        cursor.execute(sql, searchteam)
        result = cursor.fetchall()
        for row_data in result:
            print(row_data)
        sql2 = "SELECT * FROM coaching_staff WHERE team = %s"
        cursor.execute(sql2, searchteam)
        result = cursor.fetchall()
        for row_data in result:
            print(row_data)

    else:
        break
    db.commit()

