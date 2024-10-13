import os, dotenv
from openai import OpenAI
dotenv.load_dotenv()

openai = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

print("Bienvenido a ChatGPT")
print("Que quieres saber?")
prompt = input("User: ")

while True:
    if (
        prompt.lower() == "exit" or \
        prompt.lower() == "salir" or \
        prompt.lower() == "es todo" or \
        prompt.lower() == "nada" or \
        prompt.lower() == "nothing" or \
        prompt.lower() == "olvidalo" or \
        prompt.lower() == "olvida lo"
        ):
        break
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'system',
                'content': 'Eres un asistente que da respuestas cortas y concretas'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ],
        # stream=True
    )
    # Impresion de respuesta
    print("ChatGPT: ",response.choices[0].message.content, "\n")

    prompt = input("Deseas saber algo mas?\nUser: ")

print("Good bye ;)")
