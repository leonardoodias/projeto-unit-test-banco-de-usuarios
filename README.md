# Banco-Usuarios
Disciplina de Testes Unitários do Curso de Especialização em Testes Ágeis - Cesar Schol

Este repositório tem como finalidade gerenciar os entregavéis de tarefas da disciplina de Testes Unitários, ministrado pelo professor Fabricio Torquato, para o curso ***Especialização ETA 2022.B***.

Este repositório contém um exemplo de código e testes unitários em Python para a classe ServiceUser do serviço de usuário.

# Tarefas - Hands On : ***16/06/2023***
# SETUP
- [x] Instalação PyCharm 
    - Link para baixar o PyCharm - https://www.jetbrains.com/pycharm/download/#section=windows
    - Dicas: https://www.jetbrains.com/help/pycharm/installation-guide.html
- [x] Instalação Conda
    - Link para baixar o Conda:  https://www.anaconda.com/download/ ou https://docs.conda.io/en/latest/miniconda.html
    - Dicas: https://conda.io/projects/conda/en/latest/user-guide/install/windows.html
- [x] Troubleshooting para Windows
    1- Run PowerShell as Administrator and do Set-ExecutionPolicy Unrestricted to allow running conda init script. 
    2- In PowerShell, do miniconda3/Scripts/conda.exe init powershell, restart the shell to make sure conda is properly initialized. 
    3- Start new project in PyCharm with a new Conda environment.

# DESENVOLVIMENTO
- [x] Criar os métodos no arquivo Service_User 
  - [x] Atualizar no método de adicionar usuário as condições de nulo e string
  - [x] Condição se nome adicionado já existe (não pode adicionar o mesmo nome com jobs diferentes
  - [x] Atualizar (apenas atualizar o job)
  - [x] Deletar (não pode deletar quem não existe)
  - [x] Recuperar o nome da pessoa de acordo com o trabalho dela

# TESTES
- [x] Testes unitários
* Esses testes visam garantir o correto funcionamento dos métodos da classe ServiceUser em diferentes cenários.
- A cobertura de testes da classe ServiceUser é abrangente e inclui os seguintes cenários:
    * Teste de adição de usuário com sucesso.
    * Teste de adição de usuário inválido.
    * Teste de adição de usuário já existente.
    * Teste de atualização de usuário com sucesso.
    * Teste de atualização de usuário inexistente.
    * Teste de listagem de nomes para um determinado trabalho.
    * Teste de exclusão de usuário.
    * Teste de exclusão de usuário inexistente.
    * Teste de verificação de usuário existente.
    * Teste de verificação de usuário inexistente.
    * Teste de listagem de nomes para um trabalho inexistente.
 
# Arquivos
- src/models/store.py: Implementação da classe Store que representa um armazenamento de dados para usuários.
- src/models/user.py: Implementação da classe User que representa um usuário.
- src/service/service_user.py: Implementação da classe ServiceUser que fornece serviços relacionados aos usuários.
- tests/test_service_user.py: Testes unitários para a classe ServiceUser.

Contribuição
Fique à vontade para contribuir com melhorias, correções ou novos recursos para este projeto. Sinta-se à vontade para abrir problemas ou enviar solicitações de recebimento. Seu feedback é bem-vindo!

Licença
Este projeto está licenciado nos termos da licença MIT. Consulte o arquivo LICENSE para obter mais informações.

Espero que este repositório seja útil para entender e praticar os testes unitários em Python. Se você tiver alguma dúvida ou precisar de mais informações, não hesite em entrar em contato.
