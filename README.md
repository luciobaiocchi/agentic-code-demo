### Prerequisites 

- Python 3.10+ installed (see the bookbot project for help if you don't already have it)
- uv project and package manager (download on https://github.comastral-sh/uv)
- Access to a Unix-like shell (e.g. zsh or bash)

### Startup

Create a virtual environment at the top level of your project directory:

```bash
uv venv
```

Activate the env
```bash
source .venv/bin/activate
```

Add dependencies:
```bash
uv add google-genai==1.12.1
uv add python-dotenv==1.1.0
```

launch main:
```bash 
uv run main.py
```

also create a .env file in the working dir and add:
```bash
GEMINI_API_KEY="your_api_key"
```

