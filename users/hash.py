from passlib.context import CryptContext


pwt_ctx = CryptContext(schemes='bcrypt', deprecated='auto')


class Hash():
    def bcrypt(password: str):
        return pwt_ctx.hash(password)

    def verify(hashed_password, plain_password):
        return pwt_ctx(plain_password, hashed_password)