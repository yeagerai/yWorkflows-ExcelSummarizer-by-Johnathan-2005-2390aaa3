
import pytest
from fastapi.testclient import TestClient
from dotenv import load_dotenv
from pydantic import ValidationError
from typing import Any
from .main import excel_summarizer_app, ExcelSummarizerIn, ExcelSummarizerOut

load_dotenv()
client = TestClient(excel_summarizer_app)

# Define test cases
test_cases = [
    {
        "input": ExcelSummarizerIn(excel_workbook=b"excel_data_1"),
        "output": ExcelSummarizerOut(word_document=b"word_document_1"),
    },
    {
        "input": ExcelSummarizerIn(excel_workbook=b"excel_data_2"),
        "output": ExcelSummarizerOut(word_document=b"word_document_2"),
    },
    {
        "input": ExcelSummarizerIn(excel_workbook=b"excel_data_3"),
        "output": ExcelSummarizerOut(word_document=b"word_document_3"),
    },
    {
        "input": ExcelSummarizerIn(excel_workbook=b"bad_input_data"),
        "output": ValidationError,
    },
]

# Use parametrize to create multiple test scenarios
@pytest.mark.parametrize("test_case", test_cases)
def test_transform(test_case: Any) -> None:
    input_data = test_case["input"]
    expected_output = test_case["output"]

    # If the expected_output is a ValidationError, handle it in a try-except block
    if expected_output == ValidationError:
        with pytest.raises(ValidationError):
            response = client.post("/transform/", data=input_data)
    else:
        response = client.post("/transform/", data=input_data)
        output_data = ExcelSummarizerOut(**response.json())

        # Assert output matches expected_output
        assert output_data == expected_output

