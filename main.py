from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp

MODEL_PATH = "./models/llama-2-7b-chat.Q8_0.gguf"


callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
llm = LlamaCpp(
    model_path=MODEL_PATH,
    temperature=0.75,
    max_tokens=50,
    top_p=1,
    callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
)

prompt = """
Who are you?
"""
llm.invoke(prompt)

prompt = """
Why are you gay?
"""
llm.invoke(prompt)