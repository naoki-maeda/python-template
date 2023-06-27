from src import __version__


def test_init() -> None:
    assert __version__ == "0.1.0"
