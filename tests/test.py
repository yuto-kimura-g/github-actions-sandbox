import pytest
from src.main import echo, Person


def test_echo():
    assert echo("bob") == "msg: bob"
    with pytest.raises(TypeError):
        echo(-1)
    return


@pytest.mark.parametrize(("msg, expect"), [
    ("hoge", "msg: hoge"),
    ("hige", "msg: hige"),
    ("foobar", "msg: foobar")
])
def test_echo_with_mark(msg, expect):
    assert echo(msg) == expect
    return


def test_person():
    p = Person("ted", 10)
    assert p.get_name() == "ted"
    assert p.get_age() == 10
    with pytest.raises(AssertionError) as e:
        p.set_age("alice")
        e.value == "[TypeError]"
    p.set_age(100)
    assert p.get_age() == 100
    return
