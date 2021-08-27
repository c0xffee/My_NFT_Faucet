from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    title = 'Claiming NFTs Here'
    return render_template("home.html", title=title)


@app.route("/payment", methods=['POST'])
def payment():
    title = "Waiting FOR your Payment"
    slp_addr = request.form["slp_addr"]
    amount = request.form["amount"]
    return render_template("payment.html", title=title, slp=slp_addr, amount=amount)
    # return title + slp_addr + pay_addr
    # return redirect(url_for("payment", title=title, slp=slp_addr, pay=pay_addr))


@app.route("/dbck", methods=['POST'])
def dbck():
    buyer_slp = request.form["buyer_slp"]
    tx = request.form["tx"]
    return render_template("dbck.html", buyer_slp=buyer_slp, tx=tx)


@app.route("/wait2pay")
def wait2pay():
    title = 'wait2pay'
    return render_template("wait2pay.html", title=title)


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/t")
def t():
    return render_template("t.html")


@app.route("/paybutton")
def paybutton():
    return render_template("paybutton.html")


if __name__ == "__main__":
    app.debug = True
    app.run(port=9487)
