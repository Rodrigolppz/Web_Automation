from selenium import webdriver 
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

#Definindo caminho do firefox
caminho_executavel_firefox = "C:\\Users\\Rodrigo\\AppData\\Local\\Mozilla Firefox\\firefox.exe"

#Opções do firefox
opcoes_firefox = webdriver.FirefoxOptions()
opcoes_firefox.binary_location = caminho_executavel_firefox

#inicializando firefox

servico = Service(GeckoDriverManager().install())

navegador = webdriver.Firefox(service=servico, options=opcoes_firefox)

#passo 1 - abrir a pagina desejada
 
navegador.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_videoselenium")

#passo 2 - escrever no local certo
navegador.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys("Rodrigo Ascenção")
navegador.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys("rodrigobracens@gmail.com")
navegador.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys("21964763192")

#passo 3 - clicar pra acessar
navegador.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/button/span/b').click()