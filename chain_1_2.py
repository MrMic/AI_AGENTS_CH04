from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from llm_models import get_llm
from prompts import (
    ASSISTANT_SELECTION_PROMPT_TEMPLATE,
)
from utilities import to_obj

assistant_instructions_chain = (
    {"user_question": RunnablePassthrough()}
    | ASSISTANT_SELECTION_PROMPT_TEMPLATE
    | get_llm()
    | StrOutputParser()
    | to_obj
)
