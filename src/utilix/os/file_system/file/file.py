from utilix.os.file_system.file.mime import Mime
from utilix.os.file_system.path.file import File as FilePath


class File:
    def __init__(self, file_path:FilePath, mime:Mime):
        self._path = file_path
        self._mime = mime

        self._name = None
        self._mime = None

    def get_name(self) -> str:
        pass

    def get_mime(self) -> Mime:
        pass

    @classmethod
    def init_from_path(path:Path):
        pass

    def sanitize_filename(self) -> str:
        """
        Replace filesystem-problematic characters, trim spaces,
        and return a safe filename component. Returns 'unnamed' if empty.
        """
        bad = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        cleaned = self._name.strip()
        for ch in bad:
            cleaned = cleaned.replace(ch, '_')
        cleaned = " ".join(cleaned.split())
        return cleaned if cleaned else "unnamed"