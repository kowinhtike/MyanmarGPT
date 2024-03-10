from googletrans import Translator
from openai import OpenAI
client = OpenAI(api_key="your_openai_api_key")
def translator(text, languages):
    return Translator().translate(text, src=languages[0], dest=languages[1]).text
def question(text):
    response = client.completions.create(model="gpt-3.5-turbo-instruct", prompt=text, max_tokens=50, temperature=0.7)
    return response.choices[0].text.strip()
while True:
    input_text = input("give any question or to exit 'q' :")
    if input_text == "q":
        break
    print(translator(question(translator(input_text, ["my", "en"])), ["en", "my"]))
