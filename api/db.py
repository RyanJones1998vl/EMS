from datetime import datetime
import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def checkAccount(eml, psw):
    sql_select_query = """select employee_id, role from employee where email = ? and password = ? """
    cur = get_db().execute(sql_select_query, (eml,psw))
    rv = cur.fetchone()
    # cur.close()
    return (rv[0], rv[1]) if rv else None

def loadEmployee():
    sql_select_query = """select * from employee"""
    cur = get_db().execute(sql_select_query)
    rv = cur.fetchall()
    # cur.close()
    return [[e[0],e[1],e[2],e[4],e[5],e[6],e[7],e[8],e[9],e[10],e[11]] for e in rv]

def loadSalary():
    sql_select_query = """select * from salary"""
    cur = get_db().execute(sql_select_query)
    rv = cur.fetchall()
    # cur.close()
    if rv == None: return []
    return [[e[1],e[2],e[3],e[4],e[5],e[6],e[0]] for e in rv]

def loadLeaveFormsGivenId(id):
    sql_select_query = """select * from leave_application where employee_id = ?"""
    cur = get_db().execute(sql_select_query, id)
    rv = cur.fetchall()
    # cur.close()
    if rv == None: return []

    return [[e[2],e[3],e[4],e[5],e[6],e[0],e[1]] for e in rv]

def loadLeaveForms():
    sql_select_query = """select * from leave_application"""
    cur = get_db().execute(sql_select_query)
    rv = cur.fetchall()
    # cur.close()
    if rv == None: return []

    return [[e[2],e[3],e[4],e[5],e[6],e[0],e[1]] for e in rv]

def loadCEmotions():
    sql_select_query = """select * from expression"""
    cur = get_db().execute(sql_select_query)
    rv = cur.fetchall()
    # cur.close()
    if rv == None: return []
    print("hello")
    # print(type(rv[0][1]))
    # print(type(rv[0][2]))
    # print(type(rv[0][3]))
    print([[e[1],e[2],str(e[3]),str(e[4]),str(e[5]),str(e[6]),str(e[7]),str(e[8])] for e in rv])
    return [[e[1],e[2],str(e[3]),str(e[4]),str(e[5]),str(e[6]),str(e[7]),str(e[8])] for e in rv]


def getEmployee(id):
    print(id)
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    sql_select_query = """select * from employee where employee_id = ?"""
    cur = get_db().execute(sql_select_query, id)
    e = cur.fetchone()
    # cur.close()
    return [e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9],e[10],e[11]]

def getLeave(id):
    print(id)
    print("hello")
    
    sql_select_query = """select * from leave_application where id = ?"""
    cur = get_db().execute(sql_select_query, id)
    e = cur.fetchone()
    # cur.close()
    return [e[2],e[3],e[4],e[5],e[6],e[0],e[1]]

def getSalary(id):
    #print(id)
    #print("hello")
    sql_select_query = """select * from salary where id = ?"""
    cur = get_db().execute(sql_select_query, id)
    e = cur.fetchone()
    # cur.close()
    print([e[1],e[2],e[3],e[4],e[5],e[6],e[0]])
    return [e[1],e[2],e[3],e[4],e[5],e[6],e[0]]

def geRecentRspt():
    # #print(values)
    sql_select_query = """select rspt from rspt ORDER BY
                    id DESC"""

    cur = get_db().execute(sql_select_query)
    e = cur.fetchone()    
    return e[0]

def getEmployIds():
    sql_select_query = """select employee_id from employee"""
    cur = get_db().execute(sql_select_query)
    rv = cur.fetchall()
    # cur.close()
    #print([e[0] for e in rv])
    return [e[0] for e in rv]

def deleteEmployee(id):
    sql_select_query = """delete from employee where employee_id = ?"""
    get_db().execute(sql_select_query, id)
    get_db().commit()
    deleteELeaveForm(id)
    deleteESalary(id)
    # get_db().close()

def deleteSalary(id):
    sql_select_query = """delete from salary where id = ?"""
    get_db().execute(sql_select_query, id)
    get_db().commit()
    # get_db().close()
def deleteESalary(id):
    sql_select_query = """delete from salary where employee_id = ?"""
    get_db().execute(sql_select_query, id)
    get_db().commit()
    # get_db().close()

def deleteLeaveForm(id):
    sql_select_query = """delete from leave_application where id = ?"""
    get_db().execute(sql_select_query, id)
    get_db().commit()
    # get_db().close()
    

def deleteELeaveForm(id):
    sql_select_query = """delete from leave_application where employee_id = ?"""
    get_db().execute(sql_select_query, id)
    get_db().commit()
    # get_db().close()

def create_employee(values):
    # #print(values)
    sql_select_query = """insert into employee(employee_id,email,password, role, gender, full_name, id_card, address_1, address_2, dob, contact, start_day) 
                        values(?,?,?,?,?,?,?,?,?,?,?,?)"""
    cur = get_db().execute(sql_select_query, values)
    get_db().commit()
    # get_db().close()

def updateEmployee(values):
    # #print(values)
    sql_select_query = """update employee
                        set 
                            email=?,password=?, role=?, gender=?, full_name=?, id_card=?, address_1=?, 
                            address_2=?, dob=?, contact=?, start_day=? 
                        where 
                            employee_id=?"""
    cur = get_db().execute(sql_select_query, values)
    get_db().commit()
    # get_db().close()

def createSalary(values):
    # #print(values)
    sql_select_query = """insert into salary(employee_id,salary,bank, account, account_holder, tax_number) 
                        values(?,?,?,?,?,?)"""
    cur = get_db().execute(sql_select_query, values)
    get_db().commit()
    # get_db().close()
def addRspt(values):
    # #print(values)
    sql_select_query = """insert into rspt(rspt) 
                        values(?)"""
    cur = get_db().execute(sql_select_query, values)
    get_db().commit()
    # get_db().close()

def createLeaveForm(values):
    # #print(values)
    sql_select_query = """insert into leave_application(employee_id,leave_type,day_from, day_to, reason, status) 
                        values(?,?,?,?,?,?)"""
    cur = get_db().execute(sql_select_query, values)
    get_db().commit()
    # get_db().close()

def createExpression(values):
    # #print(values)
    print(values)
    sql_select_query = """insert into expression(employee_id,date, prob_emotion_1,prob_emotion_2, prob_emotion_3, prob_emotion_4, prob_emotion_5, prob_emotion_6) 
                        values(?,?,?,?,?,?,?,?)"""
    cur = get_db().execute(sql_select_query, values)
    # cur = get_db().execute(sql_select_query, ("htc1997", datetime.now().strftime('%m/%d/%Y'))+(0.2,0.3, 0.4,0.5,0.5, 0.5))
    get_db().commit()
    # get_db().close()

def updateSalary(values):
    # #print(values)
    sql_select_query = """update salary
                        set 
                            employee_id=?,salary=?, bank=?, account=?, account_holder=?, tax_number=?
                        where 
                            id=?"""
    cur = get_db().execute(sql_select_query, values)
    print(values)
    get_db().commit()
    # get_db().close()
def updateLeaveForm(values):
    # #print(values)
    sql_select_query = """update leave_application
                        set 
                            employee_id=?,leave_type=?, day_from=?, day_to=?, reason=?, status=?
                        where 
                            id=?"""
    cur = get_db().execute(sql_select_query, values)
    get_db().commit()
    # get_db().close()