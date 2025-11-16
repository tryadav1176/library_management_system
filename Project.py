from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Root@123'
app.config['MYSQL_DB'] = 'library_management'

# Upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        cursor.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s)", (title, author, year))
        mysql.connection.commit()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall() 
    cursor.close()
    return render_template('index.html', books=books)

@app.route('/delete/<int:id>')
def delete_book(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        cursor.execute("UPDATE books SET title=%s, author=%s, year=%s WHERE id=%s", (title, author, year, id))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('index'))
    else:
        cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
        book = cursor.fetchone()
        cursor.close()
        return render_template('edit.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)
