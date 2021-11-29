# 파이썬 설치
```bash
sudo apt-get update --yes

sudo apt-get install --yes git

sudo apt-get install --yes libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libgdbm-dev lzma lzma-dev tcl-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev wget curl make build-essential python-openssl

git clone https://github.com/pyenv/pyenv.git ~/.pyenv

echo -e "\n\n# pyenv environment variables\nexport PYENV_ROOT=\"\$HOME/.pyenv\"\nexport PATH=\"\$PYENV_ROOT/bin:\$PATH\"\n\n# pyenv initialization\nif command -v pyenv 1>/dev/null 2>&1; then\n  eval \"\$(pyenv init --path)\"\nfi\n\n" >> ~/.bashrc

exec $SHELL

 python -m venv ~/.venv/dev

source ~/.venv/dev/bin/activate

deactivate

```



pip install djangorestframework
pip install markdown
pip install django-filter


