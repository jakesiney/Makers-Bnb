from lib.user import User


def test_create_new_user():
    user = User(1, "Jim@mail.com", "1234567!")
    assert user.id == 1
    assert user.email == "Jim@mail.com"
    assert user.password == "1234567!"


def test_users_are_equal():
    user1 = User(1, "Jim@mail.com", "1234567!")
    user2 = User(1, "Jim@mail.com", "1234567!")
    assert user1 == user2


def test_users_format():
    user1 = User(1, "Jim@mail.com", "1234567!")
    assert str(user1) == "User(1, Jim@mail.com, 1234567!)"