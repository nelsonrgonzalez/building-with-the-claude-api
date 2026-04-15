from markitdown import MarkItDown, StreamInfo
from io import BytesIO
import os

SUPPORTED_EXTENSIONS = {".docx", ".pdf"}


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_path_to_markdown(file_path: str) -> str:
    """Convert a PDF or DOCX file on disk to markdown-formatted text.

    Reads the file at the given path and converts its contents to markdown.
    Supports .pdf and .docx file formats only.

    When to use:
    - When you have a file path to a document on disk and want its contents as markdown
    - Prefer binary_document_to_markdown when you already have the file's bytes in memory

    When not to use:
    - For file formats other than .pdf or .docx
    - When the file is not accessible on the local filesystem

    Examples:
    >>> document_path_to_markdown("/path/to/report.pdf")
    "# Report Title\\n\\nSome content..."
    >>> document_path_to_markdown("/path/to/notes.docx")
    "# Notes\\n\\n- Item one\\n- Item two"
    """
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    if ext not in SUPPORTED_EXTENSIONS:
        supported = ", ".join(sorted(SUPPORTED_EXTENSIONS))
        raise ValueError(
            f"Unsupported file type '{ext}'. Must be one of: {supported}"
        )

    with open(file_path, "rb") as f:
        binary_data = f.read()

    return binary_document_to_markdown(binary_data, ext.lstrip("."))
