import sqlite3 as sql
import hashlib

from flask import Flask, request, Response, render_template, jsonify
from datetime import datetime

app = Flask(__name__)
DATABASE = 'wallets.db'

def start_db():
    try:
        db= sql.connect(DATABASE)
        db.execute('CREATE TABLE IF NOT EXISTS wallets(id TEXT PRIMARY KEY NOT NULL, balance INT NOT NULL, coin_symbol TEXT NOT NULL)')
        print("****Initializing database****")


        db.execute("CREATE TABLE IF NOT EXISTS txns (from_wallet TEXT NOT NULL, to_wallet TEXT NOT NULL, amount INT NOT NULL, time_stamp TEXT NOT NULL , txn_hash TEXT NOT NULL, status TEXT DEFAULT 'pending')")

        db.execute("INSERT INTO wallets (id, balance, coin_symbol) VALUES(?,?,?)",('1', 10, 'FOO_COIN'))
        db.execute("INSERT INTO wallets (id, balance, coin_symbol) VALUES(?,?,?)",('2', 20, 'FOO_COIN'))

        db.commit()
        msg = "Database initialization finished"
    except:
        db.rollback()
        msg = "Already created"

    finally:
        db.close()
        return msg


@app.route('/')
def index():
    con = sql.connect(DATABASE)
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM wallets")
    rows = cur.fetchall()

    cur.execute("SELECT * FROM txns")
    txs = cur.fetchall()

    con.close()
    return render_template('index.html', rows = rows, txs = txs)

#curl -i -X POST http://127.0.0.1:5000/wallets -d "id=3" -d "balance=5" -d "coin_symbol=FOO_COIN"
@app.route('/wallets', methods = ['POST'])
def regist():
    if request.method == 'POST':
        try:
            _id = request.form["id"]
            _balance = int(request.form["balance"])
            _coin_symbol = request.form["coin_symbol"]

            with sql.connect(DATABASE) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO wallets (id, balance, coin_symbol) VALUES (?,?,?)",(_id, _balance, _coin_symbol))
                con.commit()
                #con.close()
                msg = {'id':_id, 'balance': _balance, 'coin_symbol':_coin_symbol}
        except:
            con.rollback()
            msg = {'error' : 'failed to create new wallet'}
        finally:
            con.close()
            return jsonify(msg)

@app.route('/wallets/<id>', methods = ['GET'])
def show(id):
    if request.method == 'GET':
        sql_query = "SELECT * FROM wallets WHERE id = " + id

        try:
            with sql.connect(DATABASE) as con:
                cur = con.cursor()
                '''
                for i in cur.execute(sql_query):
                    print i
                '''

                cur.execute(sql_query)
                target = cur.fetchall()
                #con.commit()
                msg = {'id': target[0][0], 'balance': target[0][1], 'coin_symbol': target[0][2]}
        except:
            con.rollback()
            msg = {'error' : 'no such wallet'}
        finally:
            con.close()
            return jsonify(msg)

@app.route('/wallets/<id>', methods=['DELETE'])
def delete_row(id):
    if request.method == 'DELETE':
        sql_query = "DELETE FROM wallets where id = " + id
        try:
            with sql.connect(DATABASE) as con:
                cur = con.cursor()
                cur.execute(sql_query)

                con.commit()
                msg = 'id : {}, deleted'.format(id)
        except:
            con.rollback()
            msg = "failed"
        finally:
            con.close()
            return msg


#curl -i -X POST http://127.0.0.1:5000/txns -d "from=1" -d "to=2" -d "amount=3"
#curl -i -X POST http://127.0.0.1:5000/txns -d "from=3" -d "to=2" -d "amount=100"
@app.route('/txns', methods=['POST'])
def txn():
    if request.method == 'POST':
        try:
            _from = request.form["from"]
            _to = request.form["to"]
            _amount = int(request.form["amount"])
            _time = datetime.now().isoformat(' ')

            b = _from + _to + str(_amount) + _time

            _txn_hash = hashlib.sha1(b.encode('utf-8')).hexdigest()

            from_query = "UPDATE wallets SET balance = balance - " + str(_amount) +" WHERE id = " + _from
            to_query = "UPDATE wallets SET balance = balance + " + str(_amount) +" WHERE id = " + _to

            with sql.connect(DATABASE) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO txns (from_wallet, to_wallet, amount, time_stamp, txn_hash) VALUES(?,?,?,?,?)",(_from, _to, _amount, _time, _txn_hash))
                print("1")
                cur.execute("SELECT * FROM wallets WHERE id = " + _from)
                rows = cur.fetchall()

                if (int(rows[0][1]) < _amount):
                    cur.execute("UPDATE txns SET status = 'failed' WHERE txn_hash =" +  "'"+_txn_hash+"'")
                    # for string value, remember to add "'" before and after
                    # otherwise will raise error
                    con.commit()

                    raise Exception('Not enough balance')

                cur.execute(from_query)
                cur.execute(to_query)

                cur.execute("UPDATE txns SET status = 'finished' WHERE txn_hash =" + "'"+_txn_hash+"'")

                con.commit()
                msg = {'from_wallet':_from, 'to_wallet': _to, 'amount': _amount, 'time_stamp': _time, 'txn_hash':_txn_hash}
        except Exception as error:
            msg = {'error' : 'Not enough balance'}
        except:
            con.rollback()
            msg = {'error' : 'operation error, check sql query'}
        finally:
            con.close()
            return jsonify(msg)

@app.route('/txns/<txn_hash>', methods=['GET'])
def getTxn(txn_hash):
    if request.method =='GET':
        try:
            with sql.connect(DATABASE) as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM txns WHERE txn_hash=" + "'" +txn_hash+"'")
                rows = cur.fetchall() # notice do not close con after this step, will cause error !!!
                msg = {'from_wallet': rows[0][0], 'to_wallet': rows[0][1], 'amount': rows[0][2], 'time_stamp': rows[0][3], 'txn_hash': rows[0][4], 'status':rows[0][5]}
        except:
            msg = {'error' : "not exist"}
        finally:
            con.close()
            return jsonify(msg)


if __name__ == "__main__":
    msg = start_db()
    print(msg)
    app.run(debug=True)