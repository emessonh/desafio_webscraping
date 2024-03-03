SISTEMA PARA EXTRAÇÃO DE DADOS

Link do site de extração: http://www.infraestrutura.mg.gov.br/component/gmg/page/102-consulta-a-planilha-preco-setop

INSTALAÇÃO E VERSÕES:

    1. Versões

        - Versão do Python:
            1. Python 3.11.4

        - Versão ChromeDriver:  
            1. 122.0.6261.94

        - Versão do DJango: 
            1. 5.0.2

    2. Instalação:

        1. Baixe o repositorio:
            1. git clone https://github.com/emessonh/desafio_webscraping.git

        2. Baixe as dependências: 
            1. pip install -r requirements.txt

        3. Web driver:
            1. Certifique-se que o webdriver que está na aplicação é compatível com a versão do seu navegador Google 
                - Caminho webdriver: webscraping/chromedriver/chromedriver.exe
            2. Link para verificar as versões do webdriver e seu respectivo Google compatíve:
                - https://chromedriver.chromium.org/downloads

ESTRUTURA DO CÓDIGO:

    1. Utilização do django para criação dos filtros;
        - APP pagina_principal
    2. Utilização de HTML, CSS e Bootstrap, via CDN, para construção da página web;
        - Ao iniciar a aplicação e abrir no navegador a página de index é renderizada
    3. Extração dos arquivos via selenium e requests;
        - Ao clicar em pesquisar, depois de selecionar os filtros a funcão buscar dados é iniciada
        - Usa-se request para confirmar a existencia do arquivo (link extraído do site)
        - Faz download do arquivo, que é armazenado em Downloads
        - Após o tratamento os dados são iterados e salvos no banco com a biblioteca django-pandas 
    4. Tratamentos dos dados com Pandas;
        - Após o download começa o tratamento com pandas, retirando os dados úteis e criando um dataframe
    5. Envio das informações tratadas para o banco;
        - Ao final uma mensagem de retorno é enviada, pode ser de sucesso ou erro, sendo redirecionado para página web


