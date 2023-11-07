<h1>Sistema de Login com Python e SQLite3</h1>

## Descrição
Sistema de Login com Python utilizando a biblioteca tkinter com integração do banco de dados SQLite3.

<b>Tela de Login</b>

![login](https://github.com/daos12/Login-com-Python-e-sqLite/assets/112141783/520b6a14-8b98-45c1-aff0-0f9b4f5a75d0)


<b>Registro</b>

![registro](https://github.com/daos12/Login-com-Python-e-sqLite/assets/112141783/3cca63bc-f4a2-4292-83d9-6442bbe168f6)


## Funcionalidades
* <b>Login</b>: Realiza a busca com integração a base de dados;
* <b>Registro</b>: Registro com integração com base de dados;
* <b>Verificação de endereço de e-mail</b>: Verifica se o endereço cadastrado e realmente um email valido.


## Tecnologias utilizadas
* Python;
* SQLite2 (Banco de dados);
* Visual Studio Code;
* DB Browser (SQLite) Para acompamento de inserções de dados;
* Configuração de servidor SMTP (Para realizar o encaminhamento do codigo de verificação do cadastro).


## Rodando o projeto
1. Para rodar o repositório é necessário clonar o mesmo em sua maquina local;
2. Instalar a IDE de sua preferência, no exemplo foi utilizado o Visual Studio Code;
3. Instalar o banco de dados SQLite. [Tutorial de instalação](https://www.alura.com.br/artigos/sqlite-da-instalacao-ate-primeira-tabela?utm_term=&utm_campaign=%5BSearch%5D+%5BPerformance%5D+-+Dynamic+Search+Ads+-+Artigos+e+Conteúdos&utm_source=adwords&utm_medium=ppc&hsa_acc=7964138385&hsa_cam=11384329873&hsa_grp=111087461203&hsa_ad=645853715422&hsa_src=g&hsa_tgt=aud-456779235754:dsa-843358956400&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjwtJKqBhCaARIsAN_yS_k4ys176y1O1yiNsuYhyfZs5gOl_RF9lLglshTTBzlxvJ5UBR3J4TgaAmM2EALw_wcB)
4. Para funcionalidade de envio de código de verificação, e necessario criar uma senha de aplicativo.  [Tutorial senha de aplicativo](https://atendimento.tecnospeed.com.br/hc/pt-br/articles/4418115119127-Como-criar-senha-de-aplicativo-para-email)
5. Altere as configurações do servidor SMTP do arquivo [Functions.py](https://github.com/daos12/Login-com-Python-e-sqLite/blob/main/Functions.py) para o seu email e senha de aplicativo.
![image](https://github.com/daos12/Login-com-Python-e-sqLite/assets/112141783/7ceff08d-fdd6-42fd-bb31-f010bce22e5d)


## Implementação futura
* <b>Código de Verificação</b>: Encaminhamento de código de verificação com integração do email (gmail) e python;
* <b>Organização das Funções e Métodos</b>: Realizar a separação de funções e metodos em outra classe para melhor organização do código.


## Status do projeto
Em desenvolvimento.
