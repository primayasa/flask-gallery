from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
import random
import string
import os

app=Flask(__name__)
letters = string.ascii_lowercase
app.secret_key = ''.join(random.choice(letters) for i in range(15))
db_name = "gallery.db" 

@app.route("/")
@app.route("/index")
def index():
    con=sql.connect(db_name)
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from images")
    images=cur.fetchall()
    return render_template("index.html",images=images)

@app.route("/upload",methods=['POST','GET'])
def upload():
    if request.method=='POST':
        # Save uploaded image to the 'static' directory
        image_title = request.form['title']
        image_file = request.files['image']
        # image_name = image_file.filename
        file_name, file_extension = os.path.splitext(image_file.filename)
        image_name = ''.join(random.choices(string.ascii_lowercase +
                                string.digits, k=20))
        image_name = image_name + file_extension
        image_path = 'static/' + image_name
        image_file.save(image_path)

        # Insert image details into the database
        con=sql.connect(db_name)        
        con.execute('INSERT INTO images (image_name, image_path) VALUES (?, ?)',
                     (image_title, image_path))
        con.commit()
        flash('Image uploaded successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('upload.html')
    
@app.route('/delete/<int:image_id>', methods=['POST'])
def delete(image_id):
    # Delete image from the database and file system
    con=sql.connect(db_name)
    cursor = con.execute('SELECT image_path FROM images WHERE id = ?', (image_id,))
    image_path = cursor.fetchone()[0]
    con.execute('DELETE FROM images WHERE id = ?', (image_id,))
    con.commit()
    os.remove(image_path)
    flash('Image deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)