from prompts.system import SYSTEM_PROMPT
from prompts.templates import build_research_prompt
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


topic = input("Enter a topic to research: ")
level = input("Enter the audience level (e.g., beginner, intermediate, advanced): ")
output_format = input("Enter the desired output format (e.g., JSON, Markdown): ")   

prompt = build_research_prompt(topic, level, output_format)

print("System Prompt:")
print(SYSTEM_PROMPT) 
print("-----------------------------------------------------------------------")   

print("Research Prompt:")
print(prompt)
print("-----------------------------------------------------------------------")


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
                    system_instruction=SYSTEM_PROMPT,
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
    print(f"Answer: {ask_llm(prompt)}")
