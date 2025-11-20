from typing import Optional

from utilix.os.file_system.file.mime.mime import Mime
from utilix.os.file_system.file.format.format import Format
from utilix.os.file_system.path.file import File as FilePath


class File:
    def __init__(self, file_path:FilePath, format:Optional[Format], mime:Optional[Mime]):
        self._path = file_path
        self._format = format
        self._mime = mime

        self._name:Optional[str] = None

    def get_name(self) -> Optional[str]:
        if self._name is None:
            # build it from the path
            pass
        return self._name

    @classmethod
    def init_from_path(cls, path: FilePath) -> "File":
        """
        Must guess the mime and the format and name and extension from the  _raw_path
        """
        return cls(path, None, None)
    def get_format(self) -> Format:
        return self._format


    def get_mime(self) -> Mime:
        return self._mime

    def get_path(self) -> FilePath:
        return self._path



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
        if cleaned:
            return cleaned
        else:
            return "unnamed"