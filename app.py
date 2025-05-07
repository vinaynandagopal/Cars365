from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Add this line


# MySQL configuration (change accordingly)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Password1029384756!'
app.config['MYSQL_DB'] = 'cars365'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        address = request.form["address"]
        dob = request.form["dob"]
        password = request.form["password"]
        role = "Public"
        reg_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        query = """
        INSERT INTO users (Name, Email, PhoneNumber, Address, Role, DateOfBirth, RegistrationDate, Password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (name, email, phone, address, role, dob, reg_date, password)

        cursor = mysql.connection.cursor()
        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()


        return redirect(url_for("login"))


    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE Email = %s AND Password = %s", (email, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            session["user"] = user[2]  # assuming Name is the third column (index 2)
            return redirect(url_for("dashboard"))  # redirecting to dashboard
        else:
            flash("Invalid email or password!", "error")
            return render_template("login.html")

    return render_template("login.html")


@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route('/buyusedcars')
def buy_used_cars():
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT Model, Make, CarCondition, Engine, Price FROM cars")
    cars = cursor.fetchall()
    cursor.close()
    return render_template('buyusedcars.html', cars=cars)

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html")
    else:
        return redirect(url_for("login"))

@app.route("/sell_car", methods=["GET", "POST"])
def sell_car():
    if "user" not in session:
        flash("Please log in to sell a car.", "error")
        return redirect(url_for("login"))

    if request.method == "POST":
        make = request.form.get("make")
        model = request.form.get("model")
        year = request.form.get("year")
        carcondition = request.form.get("car_condition")
        engine = request.form.get("engine")
        price = request.form.get("price")

        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cars (Make, Model, Year, CarCondition, Engine, Price )
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (make, model, year, carcondition, engine, price))
        conn.commit()
        cursor.close()

        flash("Car listed for sale successfully!", "success")
        return redirect(url_for("home"))

    return render_template("sell_car.html")

@app.route("/carfinance.html", methods=["GET", "POST"])
def finance():
    if request.method == "POST":
        price = request.form["price"]
        down_payment = request.form["down_payment"]
        interest_rate = request.form["interest_rate"]
        tenure = request.form["tenure"]

        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO CarFinanceApplications (price, down_payment, interest_rate, tenure)
            VALUES (%s, %s, %s, %s)
        """, (price, down_payment, interest_rate, tenure))
        conn.commit()

        return "Finance application submitted successfully!"
    return render_template("carfinance.html")






if __name__ == "__main__":
    app.run(debug=True)
