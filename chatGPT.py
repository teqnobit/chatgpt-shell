import os, dotenv
from openai import OpenAI
dotenv.load_dotenv()

openai = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

print("Bienvenido a ShellGPT")
print("Que quieres saber?")
prompt = input("User: ")
historyChat = [
    {
        'role': 'system',
        'content': 'Eres un asistente que da respuestas cortas y concretas, preferentemente en español'
    },
    {
        'role': 'user',
        'content': prompt
    }
]


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

    # Generacion de la respuesta 
    response = openai.chat.completions.create(
        model='gpt-4o',
        messages=historyChat
        ### MODIFICADO para mantener una conversacion con historyChat[]
        # messages=[
        #     {
        #         'role': 'system',
        #         'content': 'Eres un asistente que da respuestas cortas y concretas, preferentemente en español'
        #     },
        #     {
        #         'role': 'user',
        #         'content': prompt
        #     }
        # ],
        ## Para imprimir las palabras por partes
        # stream=True

    )

    # Impresion de respuesta
    print("ChatGPT: ",response.choices[0].message.content, "\n")
    historyChat.append(
        {
            'role': 'assistant',
            'content': response.choices[0].message.content
        }
    )

    # Nueva consulta
    prompt = input("Deseas saber algo mas?\nUser: ")
    historyChat.append(
        {
            'role': 'user',
            'content': prompt
        }
    )

print("Good bye ;)")
