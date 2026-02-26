# improved-octo-garbanzo
test the vibe of ona

## Purpose

Prototype web application with

- Login via Google, logout, profile page
- more to come...

## initial setup

### Google Auth

| What | Where |
|---|---|
| Create credentials | [Google Cloud Console](https://console.cloud.google.com/) > APIs & Services > Credentials |
| Redirect URI to register | `https://YOUR_CONTAINER.eu-central-1-01.gitpod.dev/callback` |
| Set `GOOGLE_CLIENT_ID` | Environment variable or `.env` file |
| Set `GOOGLE_CLIENT_SECRET` | Environment variable or `.env` file |

⚠️ The redirect URI must match exactly — including the `/callback` path and no trailing slash.