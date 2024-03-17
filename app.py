# Importar a bibliotecas
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from user import login, password
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Navegar até o site desejado
class SpacemanBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('https://www.betsson.com/br/cadastrar')
        time.sleep(15)
        self.dados()
        self.pesquisando_jogo()
        self.enviando_msg_chat()

    # Usuário e senha
    def dados(self):
        print("Vou logar")
        usuario = self.driver.find_element(By.XPATH, '//input[@test-id="login-username"]')
        usuario.click()
        print("Vou digitar")
        self.digite_como_uma_pessoa(login, usuario)
        time.sleep(random.randint(1, 7))
        print("Agora a senha")
        senha = self.driver.find_element(By.XPATH, '//input[@test-id="login-password"]')
        senha.click()
        print("Estou digitando a senha")
        self.digite_como_uma_pessoa(password, senha)
        time.sleep(random.randint(1, 7))
        print("Vamos entrar")
        botao_entrar = self.driver.find_element(By.XPATH, '//button[@test-id="login-submit"]')
        botao_entrar.click()
        time.sleep(random.randint(4, 7))

    def pesquisando_jogo(self):
        print("Abrindo o jogo")
        self.driver.get('https://glauncher.bpsgameserver.com/?gameId=pragmaticPlaySpaceman&brandId=e123be9a-fe1e-49d0-9200-6afcf20649af&marketCode=br&forReal=true&depositUrl=deposit&accountHistoryUrl=transaction-history&host=https%3A%2F%2Fwww.betsson.com&x-obg-device=Desktop&x-obg-channel=Web&x-obg-country-code=BR&sessionToken=ewogICJhbGciOiAiSFMyNTYiLAogICJ0eXAiOiAiSldUIgp9.ewogICJ1c2VySWQiOiAiNjZjNmZjM2ItOGEyZi00YjU4LTlmYzktYTQ0NzEwZWM3OTU3IiwKICAibG9naW5TZXNzaW9uSWQiOiAiMjFmOWJmOGEtYjM3My00YTgwLWFjYzEtYzQ0Y2UwMGIxYzQxIiwKICAianVyaXNkaWN0aW9uIjogIk1nYSIKfQ.Mhwu5qwG3ozdtoC31zGf7SOOSLP4huiUw7Gr_CpI86A&lobbyUrl=casino.game-launcher')
        time.sleep(30)

    def enviando_msg_chat(self):
        print("Mais 15 segundos vou digitar as mensagens")
        time.sleep(15)
        chat_msg = self.driver.find_element(By.XPATH, '//input[@id="chatMsgId"]')
        chat_msg.click()
        qts_msg = 0
        while qts_msg < 5000:
            chat_msg.send_keys(Keys.CONTROL+"V")
            print("Digitei")
            time.sleep(2)
            print("Vou enviar")
            enviar_chat_msg = self.driver.find_element(By.XPATH, '//*[@class="chat_submit"]')
            enviar_chat_msg.click()
            print("Enviei")
            time.sleep(2)
            qts_msg += 1

    @staticmethod
    def digite_como_uma_pessoa(frase, campo_input_unico):
        print("Digitando...")
        for letra in frase:
            campo_input_unico.send_keys(letra)
            time.sleep(random.randint(1, 5) / 30)


bot = SpacemanBot()
bot.dados()
