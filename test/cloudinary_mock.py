class CloudinaryMock:
    url = "http://bucket.com"
    url_secure = "https://bucket.com"
    is_test = True

    def __init__(self) -> None:
        self.options = []

    def upload(self, file, **options):
        self.options.append(options)
        return {
            "url": self.get_url(**options),
            "secure_url": self.get__secure_url(**options),
        }

    def get_url(self, **options):
        return (
            self.url
            + f"/ddict/image/upload/v1607/{options.get('public_id')}.png"
        )

    def get__secure_url(self, **options):
        return self.get_url(**options).replace(self.url, self.url_secure)
