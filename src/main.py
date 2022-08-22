
def echo(msg: str) -> str:
    if type(msg) != str:
        raise TypeError
    return f"msg: {msg}"


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        return

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def set_age(self, age: int) -> None:
        assert type(age) == int, "[TypeError]"
        self.age = age
