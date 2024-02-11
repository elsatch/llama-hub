"""Archivebox reader class.

Pass in the path to an ArchiveBox Data folder and it will parse all PDF
files into a List of Documents, with each Document containing the PDF contents.

"""
import os
from pathlib import Path
from typing import Any, List, TYPE_CHECKING

if TYPE_CHECKING:
    from langchain.docstore.document import Document as LCDocument

# from llama_index import SimpleDirectoryReader

from llama_index.readers.base import BaseReader
from llama_index.readers.file.pdf import PDFReader
from llama_index.readers.schema.base import Document


class ArchiveboxReader(BaseReader):
    """Utilities for loading data from an Archivebox Data folder.

    Args:
        input_dir (str): Path to the data folder.

    """

    def __init__(self, input_dir: str):
        """Init params."""
        self.input_dir = Path(input_dir)

    def load_data(self, *args: Any, **load_kwargs: Any) -> List[Document]:
        """Load data from the input directory."""
        docs: List[Document] = []
        for dirpath, dirnames, filenames in os.walk(self.input_dir):
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            for filename in filenames:
                if filename.endswith(".pdf"):
                    filepath = os.path.join(dirpath, filename)
                    content = PDFReader().load_data(Path(filepath))
                    docs.extend(content)
        return docs

    def load_langchain_documents(self, **load_kwargs: Any) -> List["LCDocument"]:
        """Load data in LangChain document format."""
        docs = self.load_data(**load_kwargs)
        return [d.to_langchain_format() for d in docs]