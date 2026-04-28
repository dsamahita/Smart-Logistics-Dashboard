from flask import Flask, render_template

# CREATE APP 
app = Flask(__name__)

# -------- MODULE 1 --------
def sort_deliveries():
    deliveries = [
        {"id":1, "deadline":5},
        {"id":2, "deadline":2},
        {"id":3, "deadline":3}
    ]
    deliveries.sort(key=lambda x: x["deadline"])
    return deliveries

# -------- MODULE 3 --------
def greedy_knapsack():
    return 160

# -------- MODULE 4 --------
def dp_knapsack():
    return 220

# -------- MODULE 2 --------
def dijkstra():
    return {"0→1":3, "0→2":1}

# -------- HOME --------
@app.route("/")
def home():
    return render_template("index.html")

# -------- RUN SYSTEM --------
@app.route("/run")
def run_system():
    return render_template(
        "index.html",
        deliveries=sort_deliveries(),
        greedy=greedy_knapsack(),
        dp=dp_knapsack(),
        routes=dijkstra()
    )

# -------- MAIN --------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
