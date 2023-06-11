import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
app.debug = True

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='postgres',
                            user='postgres',
                            password='RosinToast')
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM candidates;')
    candidates = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', candidates=candidates)


@app.route('/create/', methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
    LANDSDEL = request.form['LANDSDEL']
    STORKREDS = request.form['STORKREDS']
    PARTI = request.form['PARTI']
    STEMMESEDDELNAVN = request.form['STEMMESEDDELNAVN']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO candidates (LANDSDEL, STORKREDS, PARTI, STEMMESEDDELNAVN)'
                'VALUES (%s, %s, %s, %s)',
                (LANDSDEL, STORKREDS, PARTI, STEMMESEDDELNAVN))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))
  return render_template('create.html')


@app.route('/delete/', methods=('GET', 'POST'))
def delete():
    if request.method == 'POST':
        STEMMESEDDELNAVN = request.form['STEMMESEDDELNAVN']
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM candidates WHERE STEMMESEDDELNAVN = %s ;' , (STEMMESEDDELNAVN,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('delete.html')

@app.route('/update/', methods=('GET', 'POST'))
def update():
    if request.method == 'POST':
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM candidates;')
        LANDSDEL = request.form['LANDSDEL']
        STORKREDS = request.form['STORKREDS']
        PARTI = request.form['PARTI']
        STEMMESEDDELNAVN = request.form['STEMMESEDDELNAVN']
        
        LANDSDEL1 = request.form['LANDSDEL1']
        STORKREDS1 = request.form['STORKREDS1']
        PARTI1 = request.form['PARTI1']
        STEMMESEDDELNAVN1 = request.form['STEMMESEDDELNAVN1']

        print (LANDSDEL1, STORKREDS1, PARTI1, STEMMESEDDELNAVN1)
        print("\n")
        print(STEMMESEDDELNAVN, LANDSDEL, STORKREDS, PARTI)

        cur.execute('UPDATE candidates '
                    'SET LANDSDEL = %s, '
                    'STORKREDS = %s, '
                    'PARTI = %s, '
                    'STEMMESEDDELNAVN = %s '
                    'WHERE STEMMESEDDELNAVN = %s AND LANDSDEL = %s AND STORKREDS = %s AND PARTI = %s ;',
                    (LANDSDEL1, STORKREDS1, PARTI1, STEMMESEDDELNAVN1, STEMMESEDDELNAVN, LANDSDEL, STORKREDS, PARTI))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('update.html')



@app.route('/search/', methods=('GET', 'POST'))
def search():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM candidates;')
    candidates = cur.fetchall()
    
    if request.method == 'POST':
        STEMMESEDDELNAVN = request.form['STEMMESEDDELNAVN']
        PARTI = request.form['PARTI']
        LANDSDEL = request.form['LANDSDEL']
        STORKREDS = request.form['STORKREDS']
        conn = get_db_connection()
        cur = conn.cursor()
        
        stemmeseddelSQL = ''
        partiSQL = ''
        landsdelSQL = ''
        storkredsSQL = ''
        search_sql = ''

        if any(STEMMESEDDELNAVN in candidates for candidates in candidates):
            stemmeseddelSQL = 'STEMMESEDDELNAVN =' + '\''+ STEMMESEDDELNAVN + '\' ' + 'AND '
            search_sql = search_sql + stemmeseddelSQL
     
        if any(PARTI in candidates for candidates in candidates):
            partiSQL = 'PARTI =' + '\'' + PARTI + '\'' + 'AND '
            search_sql = search_sql + partiSQL

        if any(LANDSDEL in candidates for candidates in candidates):
            landsdelSQL = 'LANDSDEL =' + '\'' + LANDSDEL + '\'' + 'AND '
            search_sql = search_sql + landsdelSQL

        if any(STORKREDS in candidates for candidates in candidates):
            storkredsSQL = 'STORKREDS =' + '\'' + STORKREDS + '\'' + 'AND '
            search_sql = search_sql + storkredsSQL

        search_sql = search_sql + '1 = 1'

        cur.execute(f'SELECT * FROM candidates WHERE {search_sql};')

        conn.commit()
        candidates = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('search.html', candidates=candidates)

    
    cur.close()
    conn.close()
    return render_template('search.html', candidates=candidates)
