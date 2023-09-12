import os

client_id = os.environ.get("CLIENT_ID")
print(client_id)
client_secret = os.environ.get("CLIENT_SECRET")
print(client_secret)
realm_id = os.environ.get("REALM_ID")
auth_code = os.environ.get("AUTH_CODE")
refreshToken = os.environ.get("REFRESHTOKEN")
accessToken = os.environ.get("ACCESSTOKEN")
client_secrets = {
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl",
    "environment": "production"
}

qBooksAssets = {
    "authentication_assets" : {
        "realm_id": int(realm_id),
        "auth_code": auth_code
    }
}

refreshToken = refreshToken

qBData = {
    "realm_id":realm_id,
    "accessToken":accessToken
}
