import smtplib
import email.message



def enviar_email(aluno):  
    corpo_email = """
    <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Workshop de Python com IA</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #333;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
        header h1 {
            font-size: 2.5em;
            margin: 0;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 30px;
        }
        .cta {
            background-color: #007bff;
            color: #fff;
            padding: 20px;
            text-align: center;
            border-radius: 5px;
            margin-top: 30px;
        }
        .cta a {
            color: #fff;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.2em;
        }
        .content {
            display: flex;
            justify-content: space-between;
            gap: 20px;
        }
        .content div {
            flex: 1;
        }
        .content h2 {
            color: #333;
        }
        .content p {
            line-height: 1.6;
            color: #555;
        }
        footer {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
            margin-top: 50px;
        }
    </style>
</head>
<body>

<header>
    <h1>Workshop de Python com Inteligência Artificial</h1>
    <p>Aprenda a programar e construir projetos com IA!</p>
</header>

<div class="container">
    <div class="content">
        <div>
            <h2>O que você vai aprender:</h2>
            <ul>
                <li>Introdução ao Python e bibliotecas essenciais</li>
                <li>Como usar IA para resolver problemas reais</li>
                <li>Processamento de dados com Python e IA</li>
                <li>Criação de modelos de Machine Learning</li>
                <li>Implementação de algoritmos de IA em projetos práticos</li>
            </ul>
        </div>

        <div>
            <h2>Por que participar?</h2>
            <p>Este workshop é ideal para iniciantes e desenvolvedores que desejam expandir seus conhecimentos sobre Python e Inteligência Artificial. Ao final, você terá as habilidades para criar soluções inovadoras usando IA em diversas áreas.</p>
            <p>Não perca a chance de melhorar seu currículo e se destacar no mercado de tecnologia!</p>
        </div>
    </div>

    <div class="cta">
        <p>Garanta sua v
aga agora! As inscrições estão abertas.</p>
        <a href="#">Inscreva-se Já!</a>
    </div>
</div>

<footer>
    <p>&copy; 2025 Workshop de Python com IA | Todos os direitos reservados</p>
</footer>

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

enviar_email("gabrielsouto.infinity@gmail.com")
# eviar o acesso para o usuário
# buca no banco de dados o usuário que tem esse email
# 