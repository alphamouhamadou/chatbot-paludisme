
from llama_cpp import Llama

llm = Llama(
    model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=4,
    n_batch=8,
    verbose=True
)

class MistralChain:
    def run(self, query):
        result = llm(
            prompt=f"[INST] Tu es un expert du paludisme. Réponds uniquement aux questions sur le paludisme. {query} [/INST]",
            stop=["</s>"],
            temperature=0.7,
            max_tokens=512,
        )
        return result["choices"][0]["text"]

    def invoke(self, inputs, **kwargs):
        question = inputs if isinstance(inputs, str) else inputs.get("query", "")
        return self.run(question)
