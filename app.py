import os

from dotenv import load_dotenv

load_dotenv()

from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, render_template, session, url_for
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-change-me")

oauth = OAuth(app)
oauth.register(
    name="google",
    client_id=os.environ.get("GOOGLE_CLIENT_ID"),
    client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

oauth.register(
    name="infomaniak",
    client_id=os.environ.get("INFOMANIAK_CLIENT_ID"),
    client_secret=os.environ.get("INFOMANIAK_CLIENT_SECRET"),
    server_metadata_url="https://login.infomaniak.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile accounts"},
)

INFOMANIAK_ORG_ID = os.environ.get("INFOMANIAK_ORG_ID")


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
    session["user"]["provider"] = "google"
    return redirect(url_for("profile"))


@app.route("/login/infomaniak")
def login_infomaniak():
    redirect_uri = url_for("callback_infomaniak", _external=True)
    return oauth.infomaniak.authorize_redirect(redirect_uri)


@app.route("/callback/infomaniak")
def callback_infomaniak():
    token = oauth.infomaniak.authorize_access_token()
    userinfo = token.get("userinfo")

    # Verify the user belongs to the required Infomaniak organization
    if INFOMANIAK_ORG_ID:
        resp = oauth.infomaniak.get(
            "https://api.infomaniak.com/1/account", token=token
        )
        accounts = resp.json().get("data", [])
        org_id = int(INFOMANIAK_ORG_ID)
        if not any(a.get("id") == org_id for a in accounts):
            return render_template("denied.html"), 403

    session["user"] = dict(userinfo)
    session["user"]["provider"] = "infomaniak"
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
