from create import insert
from read import read
from update import update
from delete import delete

obj = insert()
objread = read()
objupdate = update()
objdelete = delete()


print("_____bank management system___")
print("for inserting data press 1")
print("for reading data press 2")
print("for updating data press 3")
print("for deleting data press 4")

opr=int(input("please enter your operation"))

def myopr():

    print("____for personal information press 1____")
    print("______for bank details press 2____")
    print("____for transcation details press 3_____")
    print("___for account details press 4___")

    vr=int(input ("please select your table:"))
    if vr==1:
       return 'personal_details'
    elif vr==2:
        return 'bank_details'
    elif vr==3:
        return 'transaction_details'
    elif vr==4:
        return 'account_details'

if opr==1:
    m=myopr()
    if m=='personal_details':
     cid = int(input("please enter customer id:"))
     fname = input("please enter customer first name:")
     lname = input("please enter customer last name:")
     addr = input("please eneter customer address:")
     pn = int(input("please enter customer phone number:"))
     an = input("please enter customer aadhar number:")
     pan = input("please enter customer pan number:")
     obj.personal_details(cid,fname,lname,addr,pn,an,pan)
    elif m=="bank_details":
        acc=int(input("please enter accountnumber:"))
        cid=int(input("please enter customer id:"))
        ifsc=(input("please enter isfc code:"))
        actype=(input("please enter account type:"))
        obj.bank_details(acc,cid,ifsc,actype)
    elif m=="transaction_details":
        tid=int(input("please enter transcation id:"))
        sacc=int(input("please enter sender account:"))
        recacc=int(input("please enter reciever account:"))
        amou=int(input("please enter amount:"))
        meth=input("please enter method:")
        obj.transaction_details(tid,sacc,recacc,amou,meth)
        
    elif m=="account_details":
        acn=int(input("please enter account number:"))
        tid=int(input("please enter transcation id:"))
        amount=int(input("please enter amount:"))
        cb=int(input("please enter closing balance:"))
        tt=input("please enter transaction type:")
        obj.account_details(acn,tid,amount,cb,tt)

        
if opr==2: # user wanted to read the data
    j = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    objread.specific_info(cusid,j)

if opr ==3:
    j = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    colname = input("please enter column name:")
    newval = input("please enter new values:") # 500 str # 'jhon'
    objupdate.myupdate(j,colname,newval,cusid)

if opr ==4:
    k = myopr()
    cusid = int(input("please enter customer id to delete the data: "))
    objdelete.specific_del(k,cusid)

