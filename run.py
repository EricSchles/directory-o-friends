from views import app

app.config["DATABASE"] = 'database.db'
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = "like I'd tell you"
app.config["USERNAME"] = "Eric"
app.config["PASSWORD"] = "Schles"
app.run(debug=True)
