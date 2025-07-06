from flask import Flask, redirect , render_template,url_for
from contact import contact

app=Flask(__name__)
app.secret_key="kfgngfjnbjfgnjgbrnrbgjnr"

@app.route("/")

@app.route("/home")
def home():
    return render_template("home.html",title="Home") #ninja==jinja page

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/contact")
def call():
    return render_template("new.html")


# @app.route("/contact",methods=['GET','POST'])
# def call():
#     cont=contact()
#     if cont.validate_on_submit():
#         return redirect(url_for("home"))
#     return render_template("contact.html",title="Contact",contact=cont)

@app.route("/project")
def project():
    return render_template("project.html")


if __name__=="__main__":
    app.run(debug=True)