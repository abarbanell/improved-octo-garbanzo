# improved-octo-garbanzo

Prototype web application built with Flask and Google OAuth. Used for exploring AI-assisted development workflows with Ona.

## Features

- Google OAuth login/logout
- Profile page showing user data from Google

## Setup

### 1. Install dependencies

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Google OAuth

Create OAuth credentials in the [Google Cloud Console](https://console.cloud.google.com/) under **APIs & Services > Credentials**:

- Application type: Web application
- Authorized redirect URI: `https://<your-environment-host>/callback`

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

| Variable | Description |
|---|---|
| `GOOGLE_CLIENT_ID` | OAuth client ID from Google Cloud Console |
| `GOOGLE_CLIENT_SECRET` | OAuth client secret from Google Cloud Console |
| `FLASK_SECRET_KEY` | Random string for session signing |

### 3. Run

```bash
. venv/bin/activate
python app.py
```

The server starts on port 5000.