import pymysql

db = pymysql.connect(host='192.168.56.101', user='thpark', password='xogus99', port=4567, db='LCK_db', charset='utf8')

cursor = db.cursor()

sql = ["USE LCK_db;",
       "CREATE TABLE player(summoner_ID VARCHAR(20) NOT NULL, firstname VARCHAR(10),lastname VARCHAR(10), line VARCHAR(3), birth INT(8), age INT(2), team VARCHAR(30), salary INT(20),expiration INT(8));",
       "SHOW TABLES;"]

for s in sql:
    cursor.execute(s)
    result = cursor.fetchall()
    for r in result:
        print(r)

sql2 = ["CREATE TABLE club(teamname VARCHAR(30) NOT NULL, initial VARCHAR(3), num_player INT(2), num_coach INT(1));",
       "SHOW TABLES;"]

sql3 = ["CREATE TABLE coaching_staff(summoner_ID VARCHAR(20) NOT NULL, firstname VARCHAR(10),lastname VARCHAR(10), role VARCHAR(10), birth INT(8), age INT(2), team VARCHAR(30), expiration INT(8));",
       "SHOW TABLES;"]

for s in sql3:
    cursor.execute(s)
    result = cursor.fetchall()
    for r in result:
        print(r)

sql = "INSERT INTO club (teamname, initial, num_player, num_coach) VALUES(%s, %s, %s, %s)" # LCK 프랜차이즈 10개팀 입력
teamlist = [["Hanhwa Life Esports", "HLE", 0, 0],
            ["DWG KIA", "DK", 0, 0],
            ["KT Rolster", "KT", 0, 0],
            ["Fredit BRION", "FBR", 0, 0],
            ["T1", "T1", 0, 0],
            ["Gen. G", "GEN", 0, 0],
            ["KWANGDONG FREECS", "KDF", 0, 0],
            ["DRX", "DRX", 0, 0],
            ["NONGSHIM REDFORCE", "NS", 0, 0],
            ["Liiv SANDBOX", "LSB", 0, 0]
            ]
for team in teamlist:
    teamname = team[0]
    initial = team[1]
    np = team[2]
    nc = team[3]
    cursor.execute(sql, (teamname, initial, np, nc))

