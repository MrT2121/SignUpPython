def btn_go_create():
    #CREATES A USER AND ITS IT TO THE DATABASE
    if textEmail.value == "" or textFname.value == "" : 
         info("ERROR","All details must be entered")
    elif textEmail.value.find("@") == -1:
           info("ERROR","Email must contain an @")
    elif len(textPW.value) <8:
           info("ERROR","Pasword must be atleast 8 characters long")
    else:
        # insert user as all credential correct
           conn = sqlite3.connect('UserBookings.db')
           info("INSERT USER","Account Created")
           insert = f"insert into UserTable (Username, UserPW, UserForname, UserSurname, UserEmail, AccountType) values ('{textUName.value}', '{textPW.value}', '{textFname.value}', '{textSName.value}','{textEmail.value}','{AccountType.value}');"
           print(insert)
           cursor = conn.cursor ()
           result = cursor.execute(insert)
           conn.commit()
           print(insert)
           close_windowS()