from models import session, User


def create_boss(first_name: str, last_name: str, username: str, password: str):
    if not session.query(User).filter_by(username=username).first():
        boss: User = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            is_hr=False,
        )
        session.add(boss)
        session.commit()


if __name__ == '__main__':
    create_boss(
        first_name=input('Ваше имя '),
        last_name=input('Ваша фамилия '),
        username=input('username '),
        password=input('password '),
    )