

import mysql.connector

conn = mysql.connector.connect(
    user='root', password='Dennis860404_', database='website'
)

cursor = conn.cursor()
query = ("SELECT id, name, username, password FROM member")
cursor.execute(query)
accpass_list = cursor.fetchall()
print(accpass_list)


Account_typein = "test"
Password_typein = "123"

#這個檢查方法會有可能帳號是A用戶 阿密碼是Ｂ用戶 阿也可以登入成功
check_acc_list_1 = [tup for tup in accpass_list if tup[2] == Account_typein]
check_pass_list_1 = [tup for tup in accpass_list if tup[3] == Password_typein]
print(check_acc_list_1)
print(check_pass_list_1)



check_acc_list = [tup for tup in accpass_list if tup[2] == Account_typein]
password_check = check_acc_list[0][3]


print(check_acc_list)
print (password_check)

