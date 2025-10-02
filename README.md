#Assistente Virtual em Python

Projeto iniciado em **2023** como estudo e desenvolvimento de um **assistente virtual multiplataforma** (Linux/Windows), inspirado na ficção mas com aplicações práticas para o dia a dia.

## ✨ Funcionalidades

* Reconhecimento de voz (Google Speech API / Microfone local).
* Respostas por voz com **pyttsx3**.
* Integração com **Wikipedia** para consultas rápidas.
* Notificações no sistema (via `plyer`).
* Relatório de **CPU e bateria** usando `psutil`.
* Verificação de clima via **API externa**.
* Automação no Windows (atalhos com `pyautogui`).
* Interface gráfica em **PyQt5** com GIF animado do Jarvis.
* Funções personalizadas como abrir/fechar programas, repetir frases, contar piadas e até cantar parabéns 🎉.

## 🛠️ Tecnologias utilizadas

* **Linguagem:** Python 3.9+
* **Bibliotecas principais:**

  * `pyttsx3`
  * `speech_recognition`
  * `PyAudio`
  * `psutil`
  * `pyautogui`
  * `pyperclip`
  * `plyer`
  * `PyQt5`
  * `wikipedia`
  * `requests`

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/jarvis-assistente.git
cd jarvis-assistente
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python jarvis.py
```

## ⚙️ Configuração extra

* Configure a **latitude/longitude** no método `tempo()` para habilitar a previsão do tempo.
* Substitua os caminhos de **imagens/GIFs** da pasta `imagem/` de acordo com o seu sistema.

## 📌 Observações

* O projeto está em **versão Beta 4.2.1**.
* Algumas funções são específicas para Windows (atalhos via tecla Win).
* Para Linux, recomenda-se trocar o motor de voz `espeak` no `pyttsx3`.

## 🤝 Contribuições

Pull requests são bem-vindos. Para mudanças maiores, abra uma issue primeiro para discutir o que você gostaria de modificar.

---
