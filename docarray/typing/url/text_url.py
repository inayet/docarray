from typing import Optional, TypeVar

from docarray.typing.proto_register import _register_proto
from docarray.typing.url.any_url import AnyUrl

T = TypeVar('T', bound='TextUrl')


@_register_proto(proto_type_name='text_url')
class TextUrl(AnyUrl):
    """
    URL to a text file.
    Can be remote (web) URL, or a local file path.
    """

    def load(self, charset: str = 'utf-8', timeout: Optional[float] = None) -> str:
        """
        Load the text file into a string.


        ---

        ```python
        from docarray import BaseDoc
        from docarray.typing import TextUrl


        class MyDoc(BaseDoc):
            remote_url: TextUrl


        doc = MyDoc(
            remote_url='https://de.wikipedia.org/wiki/Brixen',
        )

        remote_txt = doc.remote_url.load()
        ```

        ---


        :param timeout: timeout (sec) for urlopen network request.
            Only relevant if URL is not local
        :param charset: decoding charset; may be any character set registered with IANA
        :return: the text file content
        """
        _bytes = self.load_bytes(timeout=timeout)
        return _bytes.decode(charset)