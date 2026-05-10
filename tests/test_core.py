import cluster_manager.core


def test_say_hello_default() -> None:
    assert cluster_manager.core.say_hello() == "Hello, World!"


def test_say_hello_custom() -> None:
    assert cluster_manager.core.say_hello("Andre") == "Hello, Andre!"
