import sys
import sqlite3
db = sqlite3.connect("FLIGHT.db")
conn = db.cursor()

conn.execute("""CREATE TABLE FLIGHT(
                REG_NO INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                FATHER_NAME TEXT NOT NULL,
                MOBILE_NO INT NOT NULL,
                STATUS TEXT NOT NULL)""")

conn.execute("""CREATE TABLE FLIGHT1(
                REG_NO INT PRIMARY KEY NOT NULL,
                FLIGHT_NO INT  NOT NULL,
                SOURCE TEXT NOT NULL,
                DESTINATION TEXT NOT NULL,
                FOREIGN KEY (REG_NO) REFERENCES FLIGHT(REG_NO))""")


def input_data():
    t_reg_no=int(input("ENTER THE REGISTRATION NO :"))
    t_name=input("ENTER THE NAME :")
    t_f_name=input("ENTER THE FATHER NAME :")
    a=input("ENTER THE MOBILE NO :")
    ok=False
    while not ok:
        if len(a)==10:
            t_mobile_no=a
            ok=True
        else:
            print("renter")
            a = input("ENTER THE MOBILE NO :")

    t_flight_no=int(input("ENTER THE FLIGHT NO :"))
    t_source=input("ENTER THE SOURCE :")
    t_destination=input("ENTER THE DESTINATION :")
    t_status=input("ENTER THE STATUS  :")
    conn.execute("insert into flight (reg_no,name,father_name,mobile_no,status) values (?,?,?,?,?)", (t_reg_no, t_name,t_f_name ,t_mobile_no, t_status))
    conn.execute("insert into flight1 (reg_no,FLIGHT_no,source,destination) values (?,?,?,?)", (t_reg_no,  t_flight_no, t_source, t_destination))
    print("data entered succrssfully")
    db.commit()

def  update_data():
    up_data = int(input("enter the reg_no which you want to update :"))
    print("press 1 to update name :")
    print("press 2 to update father name :")
    print("press 3 to update mobile_no :")
    print("press 4 to update flight_no :")
    print("press 5 to update source :")
    print("press 6 to update destination :")
    print("press 7 to update status :")
    data = int(input("enter your choice :"))
    if (data == 1):
        up_name = input("enter the new name :")
        sql2 = "UPDATE FLIGHT SET name=? where REG_NO=?"
        conn.execute(sql2, (up_name, up_data,))
        print("update successfuly")
    elif(data==2):
        up_f_name = input("enter the new father name :")
        sql2 = "UPDATE FLIGHT SET father_name=? where REG_NO=?"
        conn.execute(sql2, (up_f_name, up_data,))
        print("update successfuly")
    elif (data == 3):
        a = input("enter the new mobile_no :")
        ok = False
        while not ok:
            if len(a) == 10:
                up_mb = a
                ok = True
            else:
                print("renter")
                a = input("ENTER THE MOBILE NO :")
        sql2 = "UPDATE FLIGHT SET mobile_no=? where REG_NO=?"
        conn.execute(sql2, (up_mb, up_data,))
        print("update successfuly")
    elif (data == 4):
        up_trno = input("enter the new flight_no :")
        sql2 = "UPDATE FLIGHT1 SET flight_no=? where REG_NO=?"
        conn.execute(sql2, (up_trno, up_data,))
        print("update successfuly")
    elif (data == 5):
        up_source = input("enter the new source :")
        sql2 = "UPDATE FLIGHT1 SET source=? where REG_NO=?"
        conn.execute(sql2, (up_source, up_data,))
        print("update successfuly")
    elif (data == 6):
        up_ds = input("enter the new destination :")
        sql2 = "UPDATE FLIGHT1 SET destination=? where REG_NO=?"
        conn.execute(sql2, (up_ds, up_data,))
        print("update successfuly")
    elif (data == 7):
        up_status = input("enter the new status :")
        sql2 = "UPDATE FLIGHT SET status=? where REG_NO=?"
        conn.execute(sql2, (up_status, up_data,))
        print("update successfuly")
    else:
        print("please enter valid choice")
    db.commit()
    
def delete_data():
    del_id = int(input("enter the reg_no which you want to delete :"))
    sql3="select * from FLIGHT"
    conn.execute(sql3,())
    check=conn.fetchall()
    print(check)
    sql = "delete from FLIGHT where REG_NO=?"
    conn.execute(sql, (del_id,))
    sql1 = "delete from FLIGHT1 where REG_NO=?"
    conn.execute(sql1, (del_id,))
    print("delete successfully")
    print("data doesnot exist")
    db.commit()

def show_data():
    text=input("\t\t\t\tENTER THE REGISTRATION NO :")
    sql3 = "SELECT * FROM FLIGHT where REG_NO=?"
    conn.execute(sql3, (text,))
    a=conn.fetchall()
    for row in a:
        print("reg no is :",row[0])
        print("Name is :", row[1])
        print("Father name is :", row[2])
        print("Phone number  is :", row[3])
        print("status is:",row[4])
    sql6 = "SELECT * FROM FLIGHT1 where REG_NO=?"
    conn.execute(sql6, (text,))
    b = conn.fetchall()
    for row1 in b:
        print("flight no is :", row1[1])
        print("source is :", row1[2])
        print("destination is is :", row1[3])
    db.commit()

def login():
    a=input("ENTER THE USERNAME :")
    if(a=="ACET"):
        print()
        b=input("ENTER THE PASSWORD :")
        if(b=="RDBMS"):
            print("LOGIN SUCCESSFUL")
            admin()
        else:
            print("ENTER THE VALID PASSWORD")
    else:
        print("ENTER THE VALID USERNAME")

def admin():
    ch='y'
    while(ch=='y'):

        print("\t\t\t\tPRESS 1 TO INPUT NEW DATA")
        print("\t\t\t\tPRESS 2 TO UPDATE DATA")
        print("\t\t\t\tPRESS 3 TO DELETE DATA")
        print("\t\t\t\tPRESS 4 FOR MAIN MENU")
        print("\t\t\t\tPRESS 5 TO EXIT")
        choice = int(input("\t\t\t\tENTER YOUR CHOICE :"))
        if (choice == 1):
            input_data()
        elif (choice == 2):
            update_data()
        elif (choice == 3):
            delete_data()
        elif(choice==4):
            main_program()
        elif(choice==5):
            sys.exit("thank you")
        else:
            print("\t\t\t\tPLEASE ENTER THE VALID CHOICE")
    ch=input("if want to continue press (y/n)")



def user():
    show_data()


def main_program():
    ch='y'
    while(ch=='y'):
        print("\t\t\t\tPRESS 1 FOR ADMIN MODE")
        print("\t\t\t\tPRESS 2 FOR USER MODE")
        print("\t\t\t\tPRESS 3 FOR EXIT")
        ind=int(input("\t\t\t\tENTER YOUR CHOICE :"))
        if(ind == 1):
            login()
        elif(ind == 2):
            user()
        elif(ind == 3):
            sys.exit("thank you")
    ch=input("if you want to continue PRESS (y/n)")


main_program()

