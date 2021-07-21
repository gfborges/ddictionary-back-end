import app.domain.service as DomainService
import bcrypt


class AuthService:
    @staticmethod
    def authenticate(domain_slug: str, password: str) -> bool:
        if domain := DomainService.find_one(domain_slug=domain_slug):
            return bcrypt.checkpw(
                password.encode(), domain.get("password").encode()
            )
