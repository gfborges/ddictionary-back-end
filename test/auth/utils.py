def get_headers(jwt_token):
    return {
        "Authorization": f"Bearer {jwt_token}",
    }
