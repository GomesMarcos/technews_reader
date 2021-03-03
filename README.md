# Technews Reader

## Configuarndo gmail

- <a href="https://mail.google.com/mail/u/0/#settings/fwdandpop">Habilite o IMAP<a/> no cliente do GMAIL
- Habilite a verificação em 2 etapas no GMAIL (tutorial oficial da plataforma <a href="https://support.google.com/accounts/answer/185839?co=GENIE.Platform%3DDesktop&hl=pt-BR">aqui</a>)
- Gere uma senha de aplicativo do google (tutorial oficial do google <a href="https://support.google.com/chrome/answer/95606?co=GENIE.Platform%3DAndroid&hl=pt-BR">aqui</a>)


## Configurando ambiente

#### Dependências:
- Python 3.x
- virtualenv
- verificação de 2 pontas habilitada no gmail
- IMAP ativo nas configurações do gmail
- Senha de App

### Criando arquivo oculto com credenciais de e-mail (Linux / Mac):

- `touch credentials.py`
- `echo 'user = "usuário_do_gmail"'`
- `echo 'password = "senha_de_app_previamente_criada"'`

<strong>Importante pontuar que, caso as configurações do GMAIL acima citadas não sejam seguidas, existe a possibilidade de mal-funcionamento por travas de segurança do GMAIL.</strong>

### Criando ambiente virtual:

`virtualenv env`

### Ativando ambiente virtual:

##### Linux / Mac
`source env/bin/activate`

##### Windows
`env\Scripts\activate`

## Instalando pacotes:

`pip install -r requirements.txt`

## Executando projeto:

`python reader.py`

## Ajuste fino:

Procure no arquivo reader.py o trecho abaixo:

- velocidade, ajuste o valor no trecho 
- - sox_effects = ("speed", "1.1")`"


<strong>Inspirado no tutorial do Roger Santos:</strong>&nbsp; <a href="https://www.youtube.com/watch?v=wm82gDsKN0E" target="_blank"><img width="32x" src="https://cdn4.iconfinder.com/data/icons/social-media-2210/24/Youtube-512.png"/><a/>
