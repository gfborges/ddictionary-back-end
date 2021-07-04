from app.domain.service import DomainService
import bcrypt


class AuthService:
    @staticmethod
    def authenticate(domain_name: str, password: str) -> bool:
        if domain := DomainService.find_one(domain_name=domain_name):
            return bcrypt.checkpw(password.encode(), domain.password)
