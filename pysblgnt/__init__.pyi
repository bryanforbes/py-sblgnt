from typing import Any, Iterator
from typing_extensions import TypedDict

_BaseRow = TypedDict('_BaseRow', { "ccat-pos": str, "ccat-parse": str })

class _MorphRow(_BaseRow):
    bcv: str
    robinson: str
    text: str
    word: str
    norm: str
    lemma: str

def morphgnt_filename(book_num: int) -> str: ...
def morphgnt_rows(book_num: int) -> Iterator[_MorphRow]: ...
