import os

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError(
        "Set GEMINI_API_KEY (or GOOGLE_API_KEY) in lesson-02-fundamentals/.env."
    )

client = genai.Client(api_key=api_key)
MODEL_NAMES = ("gemini-3.8-flash", "gemini-3.6-flash")

DEFAULT_PROMPT = (
    "You are a professional Python teacher. Answer questions about Python "
    "programming clearly and concisely. If you don't know the answer, say "
    "'I don't know'."
)


def ask_llm(question: str) -> str:
    if not question.strip():
        raise ValueError("Please enter a question.")

    last_unavailable_error: ServerError | None = None
    for model_name in MODEL_NAMES:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=question,
                config=genai.types.GenerateContentConfig(
                    system_instruction=DEFAULT_PROMPT,
                    max_output_tokens=1024,
                ),
            )
        except ServerError as error:
            if error.code != 503:
                raise
            last_unavailable_error = error
            continue

        if not response.text:
            raise RuntimeError(f"{model_name} returned an empty response.")
        return response.text

    raise RuntimeError(
        "Gemini's free-tier models are temporarily unavailable. "
        "Please wait a moment and try again."
    ) from last_unavailable_error


if __name__ == "__main__":
    question = input("Ask a question about Python: ")
    print(f"Answer: {ask_llm(question)}")