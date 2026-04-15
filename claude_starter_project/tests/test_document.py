import os
import shutil
import pytest
from tools.document import binary_document_to_markdown, document_path_to_markdown


class TestBinaryDocumentToMarkdown:
    # Define fixture paths
    FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
    DOCX_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.docx")
    PDF_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.pdf")

    def test_fixture_files_exist(self):
        """Verify test fixtures exist."""
        assert os.path.exists(self.DOCX_FIXTURE), (
            f"DOCX fixture not found at {self.DOCX_FIXTURE}"
        )
        assert os.path.exists(self.PDF_FIXTURE), (
            f"PDF fixture not found at {self.PDF_FIXTURE}"
        )

    def test_binary_document_to_markdown_with_docx(self):
        """Test converting a DOCX document to markdown."""
        # Read binary content from the fixture
        with open(self.DOCX_FIXTURE, "rb") as f:
            docx_data = f.read()

        # Call function
        result = binary_document_to_markdown(docx_data, "docx")

        # Basic assertions to check the conversion was successful
        assert isinstance(result, str)
        assert len(result) > 0
        # Check for typical markdown formatting - this will depend on your actual test file
        assert "#" in result or "-" in result or "*" in result

    def test_binary_document_to_markdown_with_pdf(self):
        """Test converting a PDF document to markdown."""
        # Read binary content from the fixture
        with open(self.PDF_FIXTURE, "rb") as f:
            pdf_data = f.read()

        # Call function
        result = binary_document_to_markdown(pdf_data, "pdf")

        # Basic assertions to check the conversion was successful
        assert isinstance(result, str)
        assert len(result) > 0
        # Check for typical markdown formatting - this will depend on your actual test file
        assert "#" in result or "-" in result or "*" in result

    def test_document_path_to_markdown_with_docx(self):
        """Test converting a DOCX file path to markdown."""
        result = document_path_to_markdown(self.DOCX_FIXTURE)
        assert isinstance(result, str)
        assert len(result) > 0
        assert "#" in result or "-" in result or "*" in result

    def test_document_path_to_markdown_with_pdf(self):
        """Test converting a PDF file path to markdown."""
        result = document_path_to_markdown(self.PDF_FIXTURE)
        assert isinstance(result, str)
        assert len(result) > 0
        assert "#" in result or "-" in result or "*" in result

    def test_document_path_to_markdown_unsupported_type(self):
        """Test that an unsupported file extension raises a descriptive ValueError."""
        with pytest.raises(ValueError, match=r"Unsupported file type '\.txt'"):
            document_path_to_markdown("/some/file.txt")


class TestDocumentPathToMarkdown:
    FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
    DOCX_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.docx")
    PDF_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.pdf")

    def test_docx_returns_string(self):
        """DOCX path produces a non-empty string."""
        result = document_path_to_markdown(self.DOCX_FIXTURE)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_pdf_returns_string(self):
        """PDF path produces a non-empty string."""
        result = document_path_to_markdown(self.PDF_FIXTURE)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_docx_content(self):
        """DOCX conversion includes known content from the fixture file."""
        result = document_path_to_markdown(self.DOCX_FIXTURE)
        assert "Model Context Protocol" in result

    def test_pdf_content(self):
        """PDF conversion includes known content from the fixture file."""
        result = document_path_to_markdown(self.PDF_FIXTURE)
        assert "Model Context Protocol" in result

    def test_uppercase_docx_extension(self, tmp_path):
        """Uppercase .DOCX extension is accepted (extension check is case-insensitive)."""
        dest = tmp_path / "test.DOCX"
        shutil.copy(self.DOCX_FIXTURE, dest)
        result = document_path_to_markdown(str(dest))
        assert isinstance(result, str)
        assert len(result) > 0

    def test_uppercase_pdf_extension(self, tmp_path):
        """Uppercase .PDF extension is accepted (extension check is case-insensitive)."""
        dest = tmp_path / "test.PDF"
        shutil.copy(self.PDF_FIXTURE, dest)
        result = document_path_to_markdown(str(dest))
        assert isinstance(result, str)
        assert len(result) > 0

    def test_unsupported_extension_raises_value_error(self):
        """Unsupported extension raises ValueError naming the bad extension."""
        with pytest.raises(ValueError, match=r"Unsupported file type '\.txt'"):
            document_path_to_markdown("/some/file.txt")

    def test_unsupported_extension_lists_supported_types(self):
        """ValueError message lists all supported extensions."""
        with pytest.raises(ValueError, match=r"\.docx"):
            document_path_to_markdown("/some/file.png")
        with pytest.raises(ValueError, match=r"\.pdf"):
            document_path_to_markdown("/some/file.png")

    def test_no_extension_raises_value_error(self):
        """Path with no extension raises ValueError."""
        with pytest.raises(ValueError, match=r"Unsupported file type ''"):
            document_path_to_markdown("/some/file_without_extension")

    def test_missing_file_raises_file_not_found(self):
        """Path to a non-existent file raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            document_path_to_markdown("/nonexistent/path/file.pdf")
