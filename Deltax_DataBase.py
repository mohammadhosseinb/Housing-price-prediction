from Deltax_web import info_of_home
import mysql.connector
import datetime
def SaveToDataBase(zone, floor_area, year_built, rooms, price, price_per_meter, home_option, date_creat, link):
    connection = mysql.connector.connect(
        host= "127.0.0.1",
        user="deltax",
        password= "kecheq210",
        database= "Deltax_Home"
    )
    cursor = connection.cursor()
    command = f"select 1 from homes_links where link = '{link}'"
    cursor.execute(command)
    result = cursor.fetchone()
    if result:
        print("exists")
        return False
    try:
        command = f"insert into home_info(zone, floor_area, year_built, rooms, price, price_per_meter, home_option, date_creat)VALUES ('{zone}', {floor_area}, {year_built}, {rooms}, {price}, {price_per_meter}, '{home_option}', '{date_creat}');"
        cursor.execute(command)
        last_id = cursor.lastrowid
        command = f"insert into homes_links(home_id, is_valid, link)VALUES ({last_id}, True, '{link}');"
        cursor.execute(command)
    except:
        return False
    connection.commit()

    cursor.close()
    connection.close()
    return True

def SaveAllToDataBase():
    infolist = info_of_home()
    today = datetime.date.today()
    count_ok = 0
    for info in infolist:
        ok = SaveToDataBase(
            info["zone"],
            info["floor_area"],
            info["year_built"],
            info["rooms"],
            info["price"],
            info["price_per_meter"],
            info["home_option"],
            today,
            info["link"]
            )
        print(ok)
        if ok:
            count_ok+=1
    print(f"has {count_ok} link added to database")
        
def ListData():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="deltax",
        password= "kecheq210",
        database= "Deltax_Home"
    )
    cursur = connection.cursor()
    command = "SELECT * from home_info;"
    cursur.execute(command)
    data = cursur.fetchall()
    return data

#SaveAllToDataBase()


