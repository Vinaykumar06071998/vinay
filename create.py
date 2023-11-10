## installed library mysql-connector-python
import mysql.connector


class insert:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "root",
                database = "bank"
                )
        
    def personal_details(self,cid,fname,lname,add,ph,aadh,pan):
        cur = self.conn.cursor() # creating cursor
        cur.execute(f"INSERT INTO PERSONAL_DETAILS VALUES({cid},'{fname}','{lname}','{add}',{ph},'{aadh}','{pan}')")
        self.conn.commit()
        print("data has been saved succesfully")

    def bank_details(self,acc,cid,ifsc,actype):
        cur=self.conn.cursor()
        cur.execute(f"insert into bank_details values('{acc}',{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print("data has been saved succesfully")

    def transaction_details(self,tid,sacc,recacc,amou,meth):
        cur=self.conn.cursor()
        cur.execute(f"insert into transaction_details values({tid},{sacc},{recacc},{amou},'{meth}')")
        self.conn.commit()
        print("data has been saved succesfully")

    def account_details(self,acn,tid,amount,cb,tt):
        cur=self.conn.cursor()
        cur.execute(f"insert into account_details values({acn},{tid},{amount},{cb},'{tt}')")
        self.conn.commit()
        print("data has been saved succesfully")