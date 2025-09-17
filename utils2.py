import smtplib
import email.message



def enviar_email(aluno):  
    corpo_email = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Recuperação de Senha</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 500px;
                margin: 40px auto;
                background: #fff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                text-align: center;
            }
            h2 {
                color: #007bff;
            }
            p {
                color: #333;
                margin-bottom: 20px;
            }
            .btn {
                display: inline-block;
                padding: 12px 24px;
                background-color: #007bff;
                color: #fff;
                border-radius: 5px;
                text-decoration: none;
                font-weight: bold;
                font-size: 1.1em;
            }
            .footer {
                margin-top: 30px;
                color: #888;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Recuperação de Senha</h2>
            <p>Olá! Recebemos uma solicitação para redefinir sua senha.</p>
            <p>Para criar uma nova senha, clique no botão abaixo:</p>
            <a href="https://seusite.com/redefinir-senha?email={aluno}" class="btn">Redefinir Senha</a>
            <p>Se você não solicitou a recuperação, ignore este e-mail.</p>
            <div class="footer">
                &copy; 2025 Sua Empresa | Todos os direitos reservados
            </div>
        </div>
    </body>
    </html>
    """

    msg = email.message.Message()
    msg['Subject'] = "recover password"
    msg['From'] = 'hackathonlimitlesshax@gmail.com'
    msg['To'] = aluno
    password = 'hdtd aidi enpv jxli' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email("gabrielsouto12344321@gmail.com")
# eviar o acesso para o usuário
# buca no banco de dados o usuário que tem esse email
#