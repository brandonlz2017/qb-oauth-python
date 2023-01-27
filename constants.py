client_id = ""
client_secret = ""
realm_id = "9130355669228116"
auth_code = ""
refreshToken = ""
accessToken = ""
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
