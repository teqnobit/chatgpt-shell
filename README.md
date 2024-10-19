# chatgpt-shell
Aplicacion sencilla manipulando la API de ChatGPT para la consola de linux.

## Instalacion de dotenv
Para hacer funcionan la api es importante gestionar la key de la API de  forma segura, para ello se usa la libreria de dotenv.

Crearemos un archivo de nombre **.env** y le incluiremos la siguiente linea:

```shell
OPENAI_API_KEY='Aqui va tu key de chatgpt'
```

Modificando lo que es necesario. Ya deberiamos de tener acceso a la API de chatgpt.


## Instalacion de la aplicacion
Para ejecutar la aplicacion es tan sencillo como ejecutar el script de python en una terminal.
```shell
python3 chatGPT.py
```

Para optimizar la operacion de la aplicacion de forma eficiente dentro de nuestra terminal es importante tener la aplicacion accecible mediante un **alias**. Para ello sera necesario crear un entorno virtual *(de nombre venv)* e instalar los requerimientos.

Luego procedemos a abrir la configuracion de nuestra shell, **.bashrc** para la consola bash y **.zshrc** para la consola zsh. En mi caso usare zsh y podemos modificar la configuracion usando *nano*.

```shell
nano ~/.zshrc
```

Bajaremos hasta la parte del **# Example aliases**, e incluiremos la siguiente linea:

```shell
alias chatgpt="source ~/chatgpt-shell/venv/bin/activate & ~/chatgpt-shell/venv/bin/python ~/chatgpt-shell/chatGPT.py"
```
*(Suponiendo que la carpeta de la aplicacion se encuentre en la raiz del usuario)*

Y ahora podemos inicializar la aplicacion en nuestra terminal usando el comando *chatgpt*
