Utilizando virtual env para isolar o python de cada
projeto
# instalacao
- pip install virtualenv
# criando ambiente virtual no projeto
- python3 -m venv .venv
# Se estiver no vscode, ele pergunta se deseja utilizar
# o ambiente virtual
- -> Sim
# ativar ambiente virtual
- source .venv/bin/activate
# para desativar ambiente virtual:
- deactivate

# ------------

ASDF necessario para gerenciar versoes do python

asdf plugin add python

asdf asdf install python 3.10.5

asdf list

asdf current

asdf local python 3.10.5