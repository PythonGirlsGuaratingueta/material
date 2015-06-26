# Instalação

Lista de Arquivos para instalar o Python e Spyder no Windows

Ordem para a instalação:

1 - python-3.4.3.msi

2 - PyQt4-4.11.4-gpl-Py3.4-Qt4.8.7-x32.exe ou PyQt4-4.11.4-gpl-Py3.4-Qt5.4.2-x64.exe
	
	De acordo com o sistema Operacional instalado na máquina
	
3 - spyder-2.3.5.2.win32-py3.4.exe

# Configuração da Variável de Ambiente

Depois de instalado é bom configurarmos a variável de ambiente no Windows para reconhecer o comando $ python no Prompt de Comando. Vamos lá!

	Clique no Menu Iniciar > Clique com o lado direito do mouse no "Meu computador" > Clique na opção "Propriedades".
	
Istes passos irão abrir a janela de informações básicas do computador.

Agora clique no link "Alterar Configurações" que está do lado direito da tela.

Abrindo a janela de "Propriedades do sistema" clique na aba "Avançado" e depois no botão "Variáveis de Ambiente".

Localize a váriavel "Path" dentro das váriaveis do sistema, selecione e clique em editar.

Copie o seguite texto no final da linha.

	;C:\Python34.3\;C:\Python34.3\Scripts\;
	
Copie da forma que está ai e cole sem que haja nenhum espaço.

Clique em "Ok" Duas vezes.

Abra o "Prompt de comando" do Windows

	Clique no menu iniciar e na caixa de pesquisa digite "cmd", aperte o "Enter".
	
Digite:

	python
	
Aperte o "Enter"

Se seguiu os paços corretamente deverá aparecer a versão do Python e uma linha com:

	Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (In
	tel)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	>>>
	








