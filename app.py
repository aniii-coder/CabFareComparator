from flask import Flask, render_template, request

app = Flask(__name__)

# Constants for Fare Calculation
BASE_FARE = 50  # Fixed charge in ₹
PER_KM_RATE = 10  # Charge per km in ₹

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/best_path")
def compare():
    return render_template('bestPath.html')

@app.route("/faq")
def faq():
    return render_template('faq.html')

@app.route("/fare_estimation", methods=["GET", "POST"])
def fare_estimation():
    estimated_fare = None
    if request.method == "POST":
        try:
            distance = float(request.form["distance"])
            if distance < 0:
                return render_template("fare_estimation.html", error="Distance cannot be negative.")
            estimated_fare = BASE_FARE + (distance * PER_KM_RATE)
        except ValueError:
            return render_template("fare_estimation.html", error="Invalid input! Enter a number.")
    
    return render_template("fare_estimation.html", estimated_fare=estimated_fare)

@app.route("/contact_us")
def contact_us():
    return render_template('contact_us.html')

if __name__ == "__main__":
    app.run(debug=True)
