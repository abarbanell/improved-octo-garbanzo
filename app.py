import os

from dotenv import load_dotenv

load_dotenv()

from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, render_template, session, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-change-me")

oauth = OAuth(app)
oauth.register(
    name="google",
    client_id=os.environ.get("GOOGLE_CLIENT_ID"),
    client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)


@app.route("/")
def index():
    logged_out = session.pop("logged_out", False)
    return render_template("login.html", logged_out=logged_out)


@app.route("/login")
def login():
    redirect_uri = url_for("callback", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route("/callback")
def callback():
    token = oauth.google.authorize_access_token()
    userinfo = token.get("userinfo")
    session["user"] = dict(userinfo)
    return redirect(url_for("profile"))


@app.route("/profile")
def profile():
    user = session.get("user")
    if not user:
        return redirect(url_for("index"))
    return render_template("profile.html", user=user)


@app.route("/logout")
def logout():
    session.clear()
    session["logged_out"] = True
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "0") == "1", host="0.0.0.0", port=5000)
