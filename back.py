import sqlite3

def connect():
    conn=sqlite3.connect("techfest.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs techfest (id INTEGER PRIMARY KEY , name TEXT , emailid TEXT , phone_number INTEGER, collegename TEXT , eventname TEXT , participationmode TEXT,amount INTEGER)")
    conn.commit()
    conn.close()
def insert(name,emailid,phone_number,collegename,eventname,participationode,amount):
    conn=sqlite3.connect("techfest.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO techfest VALUES (NULL, ?,?,?,?,?,?,?)",(name,emailid,phone_number,collegename,eventname,participationode,amount))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("techfest.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM techfest")
    row=cur.fetchall()
    conn.close()
    return row

def search(name="",emailid="",phone_number="",collegename="",eventname="",participationode="",amount=""):
    conn=sqlite3.connect("techfest.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM techfest WHERE name=? OR emailid=? OR phone_number=?  OR  collegename=?  OR  eventname=?  OR  participationmode=? OR amount=?",(name,emailid,phone_number,collegename,eventname,participationode,amount))
    row=cur.fetchall()
    conn.close()
    return row

def delete(id):
    conn=sqlite3.connect("techfest.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM techfest  where id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,emailid,phone_number,collegename,eventname,participationode,amount):
    conn=sqlite3.connect("techfest.db")
    cur=conn.cursor()
    cur.execute("UPDATE techfest SET name=? ,emailid=? , phone_number=? ,  collegename=? , eventname=? , participationmode=? , amount=? where id=?",(name,emailid,phone_number,collegename,eventname,participationode,amount,id))
    conn.commit()
    conn.close()



connect()
