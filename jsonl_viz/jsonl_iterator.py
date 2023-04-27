from typing import Iterator, List


def _lines_generator(file_path: str) -> Iterator[str]:
    with open(file_path, "r", encoding="utf8") as f:
        for line in f:
            yield line


class JsonlIterator:
    def __init__(self, file_path: str) -> None:
        self._lines_generator = _lines_generator(file_path)

        self._seen_lines: List[str] = [
            next(self._lines_generator)
        ]
        self._total_lines_in_file = None
        self.current_line_idx = 0

    def forward(self) -> str:
        if self._total_lines_in_file is not None:
            if self.current_line_idx < self._total_lines_in_file - 1:
                self.current_line_idx += 1
            return self.current()

        try:
            line = next(self._lines_generator)
            self._seen_lines.append(line)
            self.current_line_idx += 1
            return line
        except StopIteration:
            self._total_lines_in_file = len(self._seen_lines)
            return self.current()

    def current(self) -> str:
        return self._seen_lines[self.current_line_idx]

    def backward(self) -> str:
        if self.current_line_idx > 0:
            self.current_line_idx -= 1
        return self.current()
