from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re

#teste envio
import smtplib
import random
import string

def verificaEmail(email):
    # Expressão regular para validar o formato do e-mail
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Verifica se o e-mail corresponde ao padrão
    if re.match(pattern, email):
        return True
    else:
        return False


# Exemplo de uso
# email = "exemplo@email.com"
# if verifica_email(email):
#     print("O e-mail é válido.")
# else:
#     print("O e-mail é inválido.")

#=== Teste de funções ==================================


def gerar_codigo_verificacao():
    # Gera um código de verificação aleatório de 6 dígitos
    return ''.join(random.choices(string.digits, k=6))

def enviar_email_verificacao(destinatario, codigo):
    # Configurações do servidor SMTP
    smtp_server = "smtp.gmail.com"  # Substitua com o servidor SMTP apropriado
    smtp_port = 587  # Porta do servidor SMTP
    smtp_user = "testeprogramacaodiego@gmail.com"  # Seu endereço de e-mail
    smtp_password = "ycfljjwjlrxnjidh"  # Sua senha

    # Cria a mensagem de e-mail
    assunto = "Código de Verificação"
    mensagem = f"Seu código de verificação é: {codigo}"

    
    
    # Cria um objeto MIMEMultipart para compor o email
    email = MIMEMultipart()
    email["From"] = smtp_user
    email["To"] = smtp_user
    email["Subject"] = assunto
    
    # Adiciona o corpo do email (mensagem) e codifica com utf-8
    email.attach(MIMEText(mensagem, "plain", "utf-8"))
    

    # Conecta ao servidor SMTP e envia o email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, destinatario, email.as_string())
        server.quit()
        print("Email de verificação enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar o email: {e}")

# Exemplo de uso
email_destino = "daosptc@gmail.com"  # Substitua pelo endereço de email real
codigo = gerar_codigo_verificacao()
enviar_email_verificacao(email_destino, codigo)