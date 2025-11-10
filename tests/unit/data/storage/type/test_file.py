from utilix.data.storage.type.file.file import File
from utilix.os.path.path import Path

class TestFile:
    def test_get_ram(self) -> None:
        path = Path("to_test.txt")
        file = File(path)
        assert file.get_ram() is not None
        assert file.get_ram().strip() == "Call me Ismael"