# Projeto de Automação com Selenium e PyAutoGUI / Automation Project with Selenium and PyAutoGUI

Este projeto realiza automações em um site de teste, utilizando Selenium para navegação e PyAutoGUI para capturas de tela e geração de PDF.  
This project automates tasks on a testing website, using Selenium for navigation and PyAutoGUI for screenshot capturing and PDF generation.

## Descrição / Description

O objetivo deste projeto é demonstrar a automação de um processo de login, seleção de produtos, preenchimento de dados de cliente e finalização de compra. O processo é acompanhado por prints de cada etapa, que são salvos em formato PNG e convertidos para um PDF ao final da execução.  
The goal of this project is to demonstrate the automation of a login process, product selection, customer data entry, and purchase completion. Screenshots of each step are captured, saved as PNG files, and converted into a PDF at the end.

## Tecnologias Utilizadas / Technologies Used

- **Selenium**: Automação da navegação no navegador. / Browser navigation automation.
- **PyAutoGUI**: Captura de tela e interação com o sistema. / Screenshot capturing and system interaction.
- **WebDriver Manager**: Para gerenciar o driver do Chrome automaticamente. / Automatically manages the Chrome driver.
- **Pillow (PIL)**: Para manipulação e conversão de imagens. / Image manipulation and conversion.

## Pré-requisitos / Prerequisites

Antes de rodar o projeto, você precisa ter o Python 3.x instalado. Além disso, será necessário criar um ambiente virtual (`venv`) e instalar as dependências listadas no arquivo `requirements.txt`.  
Before running the project, you need to have Python 3.x installed. Additionally, you'll need to create a virtual environment (`venv`) and install the dependencies listed in the `requirements.txt` file.

### Passos para instalação / Installation Steps:

1. Clone este repositório / Clone this repository:

    ```bash
    git clone https://github.com/patriciaregina24/selenium-pyautogui-automation.git
    ```

2. Navegue até a pasta do projeto / Navigate to the project folder:

    ```bash
    cd selenium-pyautogui-automation
    ```

3. Crie e ative o ambiente virtual / Create and activate the virtual environment:

    - No Windows / On Windows:

      ```bash
      python -m venv .venv
      .\.venv\Scripts\activate
      ```

    - No macOS/Linux / On macOS/Linux:

      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```

4. Instale as dependências / Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Como Rodar / How to Run

1. Após instalar as dependências, execute o script principal / After installing the dependencies, run the main script:

    ```bash
    python main.py
    ```

2. O script vai automatizar o processo de login, seleção de produtos, preenchimento de dados e finalização da compra. Durante o processo, prints das telas serão salvos e um arquivo PDF com todas as capturas será gerado na pasta `exemplo_PDF/`.  
    The script will automate the login process, product selection, customer data entry, and purchase completion. During the process, screenshots will be saved, and a PDF file with all the captures will be generated in the `exemplo_PDF/` folder.

## Estrutura do Projeto / Project Structure

- **main.py**: Arquivo principal que executa a automação. / Main file that runs the automation.
- **funcoes.py**: Funções auxiliares para navegação, login, e interação com a página. / Helper functions for navigation, login, and page interaction.
- **dados.py**: Armazena os dados do login, produtos e informações do cliente. / Stores login data, products, and customer information.
- **prints.py**: Funções para captura de tela e conversão em PDF. / Functions for screenshot capturing and PDF conversion.
- **config_coordenadas.py**: Auxilia na identificação das coordenadas da tela para uso utilizando o PyAutoGUI. / This script helps you identify screen coordinates to be used with PyAutoGUI.
- **exemplo_PDF/**: Pasta contendo PDF com prints de exemplo do processo. / Folder containing a PDF with example screenshots of the process.

## config_coordenadas.py

Este projeto usa um arquivo chamado config_coordenadas.py para armazenar as coordenadas da tela, utilizadas pelo PyAutoGUI para localizar e interagir com elementos visuais. Caso esteja utilizando uma tela diferente, você pode executar o script capturar_coordenadas.py para obter as coordenadas corretas do seu ambiente.
This project uses a file named config_coordenadas.py to store screen coordinates used by PyAutoGUI to locate and interact with visual elements.
If you're using a different screen, you can run the script capturar_coordenadas.py to capture the correct coordinates for your setup.

## Prints de Exemplo / Example Screenshots

Aqui estão alguns prints do processo automatizado:  
Here are some screenshots of the automated process:

![Print de exemplo 1](exemplo_PDF/prints_de_execucao.pdf)

## Contribuição / Contribution

Sinta-se à vontade para contribuir com este projeto! Para isso, basta fazer um fork, realizar suas alterações e abrir um pull request.  
Feel free to contribute to this project! Just fork it, make your changes, and open a pull request.

## Licença / License

Este projeto está licenciado sob a Licença MIT / 
This project is licensed under the MIT License
