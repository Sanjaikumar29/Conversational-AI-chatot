# Python
This is for your vscode, juypter notebook terminals by this code you can run on those platforms

# pip install ollama (install this,or else you get an error)

from ollama import chat

response = chat(model='gemma4', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response.message.content)
