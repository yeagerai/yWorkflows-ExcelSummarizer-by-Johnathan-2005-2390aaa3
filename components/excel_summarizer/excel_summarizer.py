
import typing
from typing import Any
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class ExcelSummarizerIn(BaseModel):
    excel_workbook: bytes


class ExcelSummarizerOut(BaseModel):
    word_document: bytes


class ExcelSummarizer(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: ExcelSummarizerIn, callbacks: typing.Optional[Any]
    ) -> ExcelSummarizerOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        word_document = results_dict[list(results_dict.keys())[-1]].word_document
        out = ExcelSummarizerOut(word_document=word_document)
        return out

load_dotenv()
excel_summarizer_app = FastAPI()


@excel_summarizer_app.post("/transform/")
async def transform(
    args: ExcelSummarizerIn,
) -> ExcelSummarizerOut:
    excel_summarizer = ExcelSummarizer()
    return await excel_summarizer.transform(args, callbacks=None)
