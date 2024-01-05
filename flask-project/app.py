from flask import Flask, render_template ,redirect, url_for, flash,request
from flask_mysqldb import MySQL
app = Flask(__name__)



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Arshad444@'
app.config['MYSQL_DB'] = 'myStore'

mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['pswd']

        con = mysql.connection.cursor()
        query = "SELECT * FROM users WHERE emailid = %s AND password = %s"
        con.execute(query, (email, pwd))  
        user = con.fetchone()
        con.close()

        if user:
            
            return redirect(url_for('admin'))
        else:
            
            return render_template('auth/Login.html', error='Invalid credentials')

    return render_template('auth/Login.html')
    


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname=request.form['uname']
        email = request.form['email']
        pwd=request.form['pword']
        con=mysql.connection.cursor()
        query="insert  into users values(%s,%s,%s)"
        con.execute(query,(uname,email,pwd))
        con.connection.commit()
        return redirect(url_for('loginPage'))

    return render_template('auth/Register.html')
        

@app.route("/admin")
def admin():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM products")
    data = con.fetchall()
    con.close()

    total_products = len(data)
    products_in_shop = sum(1 for row in data if row[6].lower() == 'shop') 
    products_in_shop2 = sum(1 for row in data if row[6].lower() == 'shop2')
    products_in_warehouse = sum(1 for row in data if row[6].lower() == 'warehouse') 

    return render_template('admin/admin.html', data=data, total_products=total_products,
                           products_in_shop=products_in_shop, products_in_warehouse=products_in_warehouse, products_in_shop2=products_in_shop2)

    

    


@app.route("/product", methods=['GET', 'POST'])
def product():
    data = []

    if request.method == 'POST':
        brand_name = request.form['brand']
        product_name = request.form['productName']
        category = request.form['category']
        quantity = request.form['quantity']
        product_price = request.form['productPrice']
        location = request.form['location']

        
        con = mysql.connection.cursor()
        query = "INSERT INTO products (brand_name, product_name, category, quantity, product_price, location) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (brand_name, product_name, category, quantity, product_price, location)
        con.execute(query, values)
        mysql.connection.commit()
        con.close()
        
        
    return render_template('admin/product.html')

    
@app.route("/detials",methods=['GET', 'POST'])
def details():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM products")
    data = con.fetchall()
    con.close()

    if request.method == 'POST':
        sl_no = request.form.get('sl_no')
        new_location = request.form.get('new_location')

        cur = mysql.connection.cursor()
        cur.execute("UPDATE products SET location = %s WHERE sl_no = %s", (new_location, sl_no))
        mysql.connection.commit()
        cur.close()

    return render_template('admin/detail-product.html', data=data)




@app.route("/shop")
def shop():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM products WHERE location = 'shop'")
    data = con.fetchall()
    con.close()
    
    return render_template('admin/shop.html',data=data)

@app.route("/shop2")
def shop2():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM products WHERE location = 'shop 2'")
    data = con.fetchall()
    con.close()
    
    return render_template('admin/shop2.html',data=data)


@app.route("/warehouse")
def warehouse():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM products WHERE location = 'warehouse'")
    data = con.fetchall()
    con.close()
    
    return render_template('admin/warehouse.html',data=data)





@app.route("/inventory")
def inventory():
    return render_template('admin/inventory.html')

@app.route("/inventory/shop")
def inventoryShop():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM products WHERE location = 'shop'")
    data = con.fetchall()
    con.close()
    
    return render_template('admin/inventory-shop.html',data=data)
    

@app.route("/inventory/warehouse")
def inventoryWarehouse():
    con = mysql.connection.cursor()
    con.execute("SELECT * FROM products WHERE location = 'Warehouse'")
    data = con.fetchall()
    con.close()
    
    return render_template('admin/inventory-warehouse.html',data=data)
    
            



























if __name__ == "__main__":
    app.run(debug=True)
