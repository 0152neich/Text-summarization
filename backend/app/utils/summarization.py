from functools import cached_property
from shared.base import BaseModel, BaseService
from .text_processing import TextProcessing

class TextSummaryModelInput(BaseModel):
    text: str

class TextSummaryModelOutput(BaseModel):
    summary: str

class TextSummarizationModel(BaseService):

    @cached_property
    def text_processing_model(self) -> TextProcessing:
        return TextProcessing()

    def process(self, inputs: TextSummaryModelInput) -> TextSummaryModelOutput:
        """ process text summary

        Args:
            inputs (TextSummaryModelInput): text input

        Returns:
            TextSummaryModelOutput: summary output
        """
        text = self.text_processing_model.clean_text(inputs.text)
        # text = self.text_processing_model.process_sentences(text)
        summary = self.text_processing_model.textrank_summary(text)
        return TextSummaryModelOutput(summary=summary)
