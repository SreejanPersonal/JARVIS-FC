# JARVIS-FC: Your AI-Powered Personal Assistant

<p align="center">
  <img src="https://your-image-url-here.com/jarvis-logo.png" alt="JARVIS-FC Logo" width="200"/>
</p>

<p align="center">
  <a href="https://github.com/SreejanPersonal/JARVIS-FC/stargazers"><img src="https://img.shields.io/github/stars/SreejanPersonal/JARVIS-FC?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/SreejanPersonal/JARVIS-FC/network/members"><img src="https://img.shields.io/github/forks/SreejanPersonal/JARVIS-FC?style=flat-square" alt="Forks"></a>
  <a href="https://github.com/SreejanPersonal/JARVIS-FC/issues"><img src="https://img.shields.io/github/issues/SreejanPersonal/JARVIS-FC?style=flat-square" alt="Issues"></a>
  <a href="https://github.com/SreejanPersonal/JARVIS-FC/blob/main/LICENSE"><img src="https://img.shields.io/github/license/SreejanPersonal/JARVIS-FC?style=flat-square" alt="License"></a>
</p>

<p align="center">
  <b>An advanced AI assistant powered by Groq's LLM, capable of performing various tasks and providing intelligent responses.</b>
</p>

## 📑 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)
- [YouTube Series](#-youtube-series)

## 🌟 Features

- 🤖 AI-powered conversational interface
- 📁 File operations (read, write, list, delete)
- 💻 System information retrieval
- 🔍 Process management
- 🌤️ Weather information
- 💱 Currency conversion
- 📝 Quick notes management
- 🧠 Conversation history management

## 🚀 Installation

1. Clone the repository:
   ```
   git clone https://github.com/SreejanPersonal/JARVIS-FC.git
   ```

2. Navigate to the project directory:
   ```
   cd JARVIS-FC
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

6. Set up your Groq API key:
   - Create a `.env` file in the project root
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

## 🖥️ Usage

To start JARVIS-FC, run the following command:

```
python main.py
```

Once started, you can interact with JARVIS using natural language commands. Here are some special commands:

- `exit`: Quit the program
- `clear`: Start a new conversation (preserves history)
- `new`: Start fresh (clears all history)

## 📂 Project Structure

```
JARVIS-FC/
├── core/
│   ├── assistant.py
│   └── conversation.py
├── config/
│   └── tools_config.py
├── functions/
│   ├── currency_ops.py
│   ├── file_ops.py
│   ├── note_ops.py
│   ├── system_ops.py
│   └── weather_ops.py
├── utils/
│   ├── history_manager.py
│   ├── logger.py
│   └── message_formatter.py
├── main.py
├── requirements.txt
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎥 YouTube Series

This project is part of an ongoing YouTube series on the [Devs Do Code](https://www.youtube.com/channel/UCYourChannelID) channel. Follow along as we build and improve JARVIS-FC, exploring various aspects of AI development, natural language processing, and system integration.

New videos are regularly uploaded, covering topics such as:
- Setting up the project
- Implementing new features
- Optimizing performance
- Exploring advanced AI concepts

Subscribe to the channel to stay updated with the latest developments in the JARVIS-FC project!

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/SreejanPersonal">Sreejan</a>
</p>
