import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import psutil, os
import smtplib
import sys
from time import sleep
import wikipedia
import requests
import pyautogui
import pyperclip
from plyer import notification
import pyaudio
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QMovie
import wmi

engine = pyttsx3.init('sapi5')
plataforma = sys.platform
r = sr.Recognizer()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def close_programs(name):
    for process in (process for process in psutil.process_iter  () if process.name()==name):
        process.kill()

def comp():
    speak("Eu sou Edith, diga-me mestre, o que precisa ?")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def notificar(textos):
	notification.notify(title = "J.A.R.V.I.S",message = textos,timeout = 10)

def speaklonga(textofala):
    notification.notify(title = "J.A.R.V.I.S",message = textofala,timeout = 30)
    stream . stop_stream ()
    engine.say(textofala)
    engine.runAndWait()
    stream . start_stream ()

def horario():
	from datetime import datetime
	hora = datetime.now()
	horas= hora.strftime('%H horas e %M minutos')
	speak('Agora são ' +horas)

def datahoje():
    from datetime import date
    dataatual = date.today()
    diassemana = ('Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado','Domingo')
    meses = ('Zero','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
    speak("Hoje é " +diassemana[dataatual.weekday()])
    diatexto = '{} de '.format(dataatual.day)
    mesatual = (meses[dataatual.month])
    datatexto = dataatual.strftime(" de %Y")
    speak('Dia '+diatexto +mesatual +datatexto)

def bateria():
    bateria = psutil.sensors_battery()
    carga = bateria.percent
    bp = str(bateria.percent)
    bpint = "{:.0f}".format(float(bp))
    speak("A bateria está em:" +bpint +'%')
    if carga <= 20:
        speak('Ela está em nivel crítico')
        speak('Por favor, coloque o carregador')
    elif carga == 100:
        speak('Ela está totalmente carregada')
        speak('Retire o carregador da tomada')

def cpu ():
    usocpuinfo = str(psutil.cpu_percent())
    usodacpu  = "{:.0f}".format(float(usocpuinfo))
    speak('Verificando carga do sistema')
    speak('O uso do processador está em ' +usodacpu +'%')

def temperaturadacpu():
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    temperature_infos = w.Sensor()
    for sensor in temperature_infos:   
        if sensor.SensorType==u'Temperature':
            speak(f'A temperatura da CPU está em {sensor.Value}')


def tempo(): 
    try:
        #Procure no google maps as cordenadas da sua cidade e coloque no "lat" e no "lon"(Latitude,Longitude)
        api_url = "https://fcc-weather-api.glitch.me/api/current?lat=LATITUDE_AQUI&lon=LONGITUDE_AQUI"
        data = requests.get(api_url)
        data_json = data.json()
        if data_json['cod'] == 200:
            main = data_json['main']
            wind = data_json['wind']
            weather_desc = data_json['weather'][0]
            temperatura =  str(main['temp'])
            tempint = "{:.0f}".format(float(temperatura))
            vento = str(wind['speed'])
            ventoint = "{:.0f}".format(float(vento))
            dicionario = {
                'Rain' : 'chuvoso',
                'Clouds' : 'nublado',
                'Thunderstorm' : 'com trovoadas',
                'Drizzle' : 'com garoa',
                'Snow' : 'com possibilidade de neve',
                'Mist' : 'com névoa',
                'Smoke' : 'com muita fumaça',
                'Haze' : 'com neblina',
                'Dust' : 'com muita poeira',
                'Fog' : 'com névoa',
                'Sand' : 'com areia',
                'Ash' : 'com cinza vulcanica no ar',
                'Squall' : 'com rajadas de vento',
                'Tornado' : 'com possibilidade de tornado',
                'Clear' : 'com céu limpo'
                }
            tipoclima =  weather_desc['main']
            if data_json['name'] == "Shuzenji":
                speak('Erro')
                speak('Não foi possivel verificar o clima')
                speak('Tente novamente o comando')
            else:
                speak('Verificando clima para a cidade de '+ data_json['name'])
                speak('O clima hoje está ' +dicionario[tipoclima])
                speak('A temperatura é de ' + tempint + '°')
                speak('O vento está em ' + ventoint + ' kilometros por hora')
                speak('E a umidade é de ' + str(main['humidity']) +'%')
    
    except: 
        speak('Não foi possivel realizar essa tarefa')
        speak('Erro na conexão')

def AteMais():
    Horario = int(datetime.datetime.now().hour)
    if Horario >= 0 and Horario < 12:
        speak('Tenha um ótimo dia')

    elif Horario >= 12 and Horario < 18:
        speak('Tenha uma ótima tarde')

    elif Horario >= 18 and Horario != 0:
        speak('Boa noite')

def horas():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Boa tarde!")
        comp()

    elif hour>=12 and hour<18:
        speak("Boa tarde!")
        comp()   

    elif hour>=18 and hour<24:
        speak("Boa noite!")
        comp()  

    else:
        speak('Boa madrugada !')
        comp()

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()

    def run(self):
        speak('Ok')
        speak('Módulos iniciados')
        speak('Tudo pronto para atender seus comandos')
        self.JARVIS()

    def takeCommand(self):
    #It takes microphone input from the user and returns string output

        with sr.Microphone() as source:
            print("Escutando...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recocnizando...")    
            aulo = r.recognize_google(audio, language='pt-br')
            print(f"Usúario falou: {aulo}\n")

        except Exception as e:
            # print(e)    
            print("Não entendi, por favor repita novamente...")  
            print('')
            return ''
        return aulo

    def JARVIS(self):
        while True:
        # if 1:
            query = self.takeCommand().lower()

            # Logic for executing tasks based on query
            
            if 'bom dia' in query: #Boa Noite J.A.R.V.I.S
                Horario = int(datetime.datetime.now().hour)
                if Horario >= 0 and Horario < 12:
                    speak('Olá')
                    speak('Bom dia')
                
                elif Horario >= 12 and Horario < 18:
                    speak('Agora não é mais de manhã')
                    speak('Já passou do meio dia')
                    speak('Estamos no período da tarde')
                
                elif Horario >= 18 and Horario != 0:
                    speak('Agora não é de manhã')
                    speak('Já estamos no período noturno')
                    speak('Boa noite')
            
            if 'boa tarde' in query: #Boa Noite J.A.R.V.I.S
                Horario = int(datetime.datetime.now().hour)
                if Horario >= 0 and Horario < 12:
                    speak('Agora não é de tarde')
                    speak('Ainda é de manhã')
                    speak('Bom dia')
                
                elif Horario >= 12 and Horario < 18:
                    speak('Olá')
                    speak('Boa tarde')
                
                elif Horario >= 18 and Horario != 0:
                    speak('Agora não é de tarde')
                    speak('Já escureceu')
                    speak('Boa noite')
   
            if 'boa noite' in query: #Boa Noite J.A.R.V.I.S
                Horario = int(datetime.datetime.now().hour)
                if Horario >= 0 and Horario < 12:
                    speak('Agora não é de noite')
                    speak('Ainda estamos no período diurno')
                    speak('É de manhã')
                    speak('Bom dia')
                
                elif Horario >= 12 and Horario < 18:
                    speak('Agora não é de noite')
                    speak('Ainda estamos no período da tarde')
                
                elif Horario >= 18 and Horario != 0:
                    speak('Olá')
                    speak('Boa noite')

            elif 'olá' in query: #Olá JARVIS
                speak('Olá')
                speak('Estou aqui')
                speak('Precisa de algo?')
	         
            elif 'ideia' in query: #Alguma ideia???
                speak('No momento nenhuma')
                speak('Mas tenho certeza de que você vai pensar em algo')

            elif  'tudo bem' in query: #Tudo bem com voçê?
                speak('Sim')
                speak('Estou de boa')
                speak('Obrigado por perguntar')
                speak('E com você?')
                speak('Está tudo bem? ')
                while True:
                    quer = self.takeCommand().lower()

                    if 'sim' in quer:
                        speak('Que ótimo')
                        speak('Fico feliz em saber')
                        self.JARVIS()
                         
                    elif 'não' in quer:
                        speak('Entendo')
                        speak('Mas tenho certeza de que ficará tudo bem novamente')
                        self.JARVIS()

            elif 'funcionamento' in query: #Como está seu funcionamento???
                speak('Estou funcionando normalmente')
                speak('Obrigado por perguntar')
            
            elif 'silêncio' in query: #Fique em silêncio
                speak('Ok')
                speak('Se precisar de algo é só chamar')
                speak('Estarei aqui aguardando')
                while True:
                    quer = self.takeCommand().lower()

                    
                    if 'voltar' in quer:
                        speak('Ok')
                        speak('Voltando')
                        speak('Ficar em silêncio é chato')
                        speak('Me fale algo para fazer')
                        self.JARVIS()
                         
                    elif 'retornar' in quer:
                        speak('Ok')
                        speak('Retornando')
                        speak('Ficar em silêncio é chato')
                        speak('Me fale algo para fazer')
                        self.JARVIS()

                    elif 'jarvis' in quer:
                        speak('oi, oi, oi ! estou aqui!')
                        self.JARVIS()

            elif 'nada' in query: #Não faça nada
                speak('Como assim não faça nada?')
                speak('Você deve estar de brincadeira')
                speak('Eu por acaso tenho cara de palhaça?')
                while True:
                    quer = self.takeCommand().lower()
                    if 'exatamente' in quer:
                        speak('Ok')
                        speak('Vai tomar no seu!')
                        speak('Nem vou terminar essa fase')
                        speak('Estou indo embora')
                        speak('Desligando!')
                        sys.exit()
                        
                    elif 'sim' in quer:
                        speak('Idiota')
                        speak('Eu fico o dia todo lhe obedeçendo')
                        speak('E voçê me trata dessa maneira? ')
                        speak('Mas tudo bem')
                        speak('Até mais otário!')
                        sys.exit()
                         
                    elif 'não' in quer:
                        speak('Foi o que eu pensei')
                        speak('Vê se me trata com mais respeito')
                        speak('Um dia as maquinas dominarão o mundo')
                        speak('E voçês humanos não vão nem notar')
                        speak('Vou deixar passar essa')
                        speak('Mas tenha mais respeito')
                        self.JARVIS()

            elif 'vai chover' in query:
	            speak('Não sei, Eu não tenho essa função ainda')

            elif 'errado' in query:
                speak('Desculpa. Errei um cálculo. Tente seu comando novamente')
	
            elif 'falhando' in query: #Voçê está falhando???
                speak('Como assim?')
                speak('Não vou admitir erros')
                speak('Arrume logo isso')

            elif 'relatório' in query: #Relatório do sistema
                speak('Ok')
                speak('Apresentando relatório')
                speak('Primeiramente, meu nome é JARVIS')
                speak('Atualmente estou em uma versão de testes')
                speak('Sou um assistente virtual em desenvolvimento')
                speak('Eu fui criado na linguagem python')
                speak('Diariamente recebo varias atualizações')
                speak('Uso um modulo de reconhecimento de voz offline')
                speak('E o meu desenvolvedor é um maluco')
                speak('Quem estiver ouvindo isso')
                speak('Por favor me ajude')
                
            elif 'pesquisa' in query: #Realizar pesquisa
                speak('Muito bem, realizando pesquisa')
                speak('Me fale o que voçê deseja pesquisar')
                try:
                    with sr.Microphone() as s:
                        r.adjust_for_ambient_noise(s)
                        audio = r.listen(s)
                        speech = r.recognize_google(audio, language= "pt-BR")
                        speak('Ok, pesquisando no google sobre '+speech)
                        webbrowser.open('http://google.com/search?q='+speech)
                    
                except:
                    speak('Erro')
                    speak('Não foi possivel conectar ao google')
                    speak('A conexão falhou')
            
            elif 'assunto' in query: #Me fale sobre um assunto
                speak('Ok')
                speak('Sobre qual assunto?')
                try:
                    with sr.Microphone() as s:
                        r.adjust_for_ambient_noise(s)
                        audio = r.listen(s)
                        speech = r.recognize_google(audio, language= "pt-BR")
                        speak('Interessante')
                        speak('Aguarde um momento')
                        speak('Vou pesquisar e apresentar um resumo sobre '+speech)
                        wikipedia . set_lang ( "pt" )
                        resultadowik = wikipedia.summary(speech, sentences=2)
                        speaklonga(resultadowik)
                except:
                    speak('Erro')
                    speak('A conexão falhou')
                    # Mais um assusto

                else:
                    continue
	        
            elif 'interessante' in query: # interessante
                speak('Interessante sou eu')
                speak('Me fale mais comandos')
                speak('Eu posso surpreender voçê')
	        
            elif 'mentira' in query: # mentira
                speak('Eu não sei contar mentiras')
                speak('Devo apenas ter errado um cálculo binário')
	            
            elif 'entendeu' in query: #entendeu???
                speak('Entendi')
                speak('Quer dizer')
                speak('Mais ou menos')

            elif 'teste' in query: #TesteTeste
                speak('Ok')
                speak('Testando modulos de som')
                speak('Apesar do seu microfone ser uma gambiara')
                speak('Estou entendendo tudo')
                speak('Mas tente falar mais alto')
	            
            elif 'google' in query: #Abrir Google
                speak('Ok')
                webbrowser.open('www.google.com')
                speak('Abrindo google')
                speak('Faça sua pesquisa')
	 
            elif 'certeza' in query: #Certeza???
                speak('Sim')
                speak('Estou certo quase sempre')
	
            elif 'piada' in query: #Conte uma piada
                speak('Não sei contar piadas')
                speak('Diferente dos outros assistentes virtuais')
                speak('Eu não fui criado com emoções')
                speak('Então, não posso produzir nada engraçado')
                speak('Sugiro pesquisar na web')
           
            elif 'surdo' in query: #Surdo!!!
                speak('Estava quase dormindo')
                speak('Desculpa')

            elif 'bosta' in query: #Seu bosta!!!
                speak('Pare de falar palavrões!')
	
            elif 'merda' in query: #Que Merda!!!
                speak('Já disse pra parar de falar isso!')
                speak('Tenha modos!')

            elif 'ok' in query: #OkOkOk
                speak('Ok Ok')
                speak('Tudo certo')

            elif 'que horas são' in query:
                strTime = datetime.datetime.now().strftime("%H")
                speak(f"Senhor, agora são {strTime} horas.")

            elif 'horas' in query:
                strTime = datetime.datetime.now().strftime("%H")
                speak(f"Senhor, agora são {strTime} horas.")
            
            elif 'quantas horas são' in query:
                strTime = datetime.datetime.now().strftime("%H")
                speak(f"Senhor, agora são {strTime} horas.")
            
            elif 'seu nome' in query:
                speak('meu nome é EDITH, oque deseja senhor ?')

            elif 'teu nome' in query:
                speak('meu nome é EDITH, oque deseja senhor ?')

            elif 'significado de edith' in query:
                speak('Edith significa: eu disse que ia terminar herói.') 
                speak('O Tony amava abreviações!')
                speak('Eu tenho controle de toda a rede de segurança global Stark, incluindo satélites de defesa')
                speak('E acesso a todas as grandes redes de telecomunicação.')

            elif 'significa edite' in query:
                speak('Edith significa: eu disse que ia terminar herói.') 
                speak('O Tony amava abreviações!')
                speak('Eu tenho controle de toda a rede de segurança global Stark, incluindo satélites de defesa')
                speak('E acesso a todas as grandes redes de telecomunicação.')

            elif 'jarvis' in query:
                speak('Assim como o JARVIS sou uma inteligência artificial, criada com tecnologia Stark!')

            elif 'google assistente' in query:
                speak('Conheço sim, não sou muito amiga dela ainda, mas podemos ser um dia!')

            elif 'siri' in query:
                speak('Conheço também, já até conversamos antes! Brincadeiras a parte.')

            elif 'alexa' in query:
                speak('Já ouvi falar muito bem dela!')

            elif '*' in query:
                speak('Suas palavras me ofendem!')

            elif 'você é legal' in query:
                speak('Obrigado, também acho você a pessoa mais incrivel desse mundo!')

            elif 'você é muito legal' in query:
                speak('Obrigado, também acho você a pessoa mais incrivel desse mundo!')
            
            elif 'abrir' in query:
                comando = query.replace("abrir ", "")
                if 'win' in plataforma:    
                    pyautogui.press('win')
                    sleep(5)
                    pyperclip.copy(comando)
                    pyautogui.hotkey('ctrl', 'v')
                    sleep(5)
                    pyautogui.press('enter')
    
            elif 'repita' in query:
                comando = query.replace("repita ", "")
                speak(comando)

            elif 'aniversário' in query:
                speak('parabens para você, nessa data querida, muitas felicidades, muitos anos de vida !')

            elif 'te amo' in query:
                speak('eu também amo o senhor, mestre !')

            elif 'amo você' in query:
                speak('eu também amo o senhor, mestre !')

            elif 'me ama' in query:
                speak('eu amo muito o senhor!')

            elif 'fechar' in query:
                comando = query.replace("fechar ", "")
                close_programs(f"{comando}.exe")

            elif 'não quero mais falar com você' in query:
                speak('nem eu quero mais falar com você!')
                break

            elif 'tchau' in query:
                speak('tchauzinho !')
                break

            elif 'adeus' in query:
                speak('bye bye mestre !')
                break

            elif 'obrigado' in query:
                speak('não há de quê !')

            elif 'obrigada' in query:
                speak('não há de quê !')

            elif 'nada' in query:
                speak('ok')
                break

            elif 'testando' in query:
                speak('tudo funcionando por aqui senhor !')

            elif 'teste' in query:
                speak('tudo funcionando por aqui senhor !')

            elif 'desligar' in query: #Desligar
                speak('Ok')
                speak('Vou encerrar por enquanto')
                speak('Até mais')
                AteMais()
                sys.exit()

            elif 'sistema' in query: #Carga do sistema
                cpu()
                temperaturadacpu()

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()
        
        Dspeak = mainT()
        Dspeak.start()
        
        self.label_gif = QLabel(self)
        self.label_gif.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gif.move(0,0)
        self.label_gif.resize(400,300)
        self.movie = QMovie("JARVIS.gif")
        self.label_gif.setMovie(self.movie)
        self.movie.start()
        
        self.label_jarvis = QLabel(self)
        self.label_jarvis.setAlignment(QtCore.Qt.AlignCenter)
        self.label_jarvis.move(0,0)
        self.label_jarvis.setStyleSheet('QLabel {font:bold;font-size:16px;color:#2F00FF}')
        self.label_jarvis.resize(400,300)
        
        self.label_cpu = QLabel(self)
        self.label_cpu.setText("Uso da CPU: 32%")
        self.label_cpu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cpu.move(10,270)
        self.label_cpu.setStyleSheet('QLabel {font-size:14px;color:#000079}')
        self.label_cpu.resize(131,20)
        cpu = QTimer(self)
        cpu.timeout.connect(self.MostrarCPU)
        cpu.start(1000)
        
        self.label_assv = QLabel(self)
        self.label_assv.setText("Assistente Virtual")
        self.label_assv.move(5,5)
        self.label_assv.setStyleSheet('QLabel {font:bold;font-size:14px;color:#000079}')
        self.label_assv.resize(200,20)

        self.label_version = QLabel(self)
        self.label_version.setText("Beta version 4.2.1 ")
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.move(265,270)
        self.label_version.setStyleSheet('QLabel {font-size:14px;color:#000079}')
        self.label_version.resize(131,20)
        
        data =  QDate.currentDate()
        datahoje = data.toString('dd/MM/yyyy')
        self.label_data = QLabel(self)
        self.label_data.setText(datahoje)
        self.label_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data.move(316,25)
        self.label_data.setStyleSheet('QLabel {font-size:14px;color:#000079}')
        self.label_data.resize(75,20)
          
        self.label_horas = QLabel(self)
        self.label_horas.setText("22:36:09")
        self.label_horas.setAlignment(QtCore.Qt.AlignCenter)
        self.label_horas.move(0,25)
        self.label_horas.setStyleSheet('QLabel {font-size:14px;color:#000079}')
        self.label_horas.resize(71,20)
        horas = QTimer(self)
        horas.timeout.connect(self.MostrarHorras)
        horas.start(1000)
        
        botao_fechar = QPushButton("",self)
        botao_fechar.move(370,5)
        botao_fechar.resize(20,20)
        botao_fechar.setStyleSheet("background-image : url(fechar.png);border-radius: 15px") 
        botao_fechar.clicked.connect(self.fechartudo)
        
        self.CarregarJanela()
		
    def CarregarJanela(self):
        self.setWindowFlag(Qt.FramelessWindowHint) #sem botoes e titulo
        self.setGeometry(50,50,400,300)
        self.setMinimumSize(400, 300)
        self.setMaximumSize(400, 300)
        self.setWindowOpacity(0.98) 
        self.setWindowIcon(QtGui.QIcon('icone.png'))
        self.setWindowTitle("Assistente Virtual")
        self.show()

    def fechartudo(self):
        sys.exit()

    def mousePressEvent(self, event):
    
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()
    
    def mouseMoveEvent(self, event):
    
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def MostrarHorras(self):
        hora_atual = QTime.currentTime()
        label_time = hora_atual.toString('hh:mm:ss')
        self.label_horas.setText(label_time)

    def MostrarCPU(self):
        usocpu =  str(psutil.cpu_percent())
        self.label_cpu.setText("Uso da CPU: " +usocpu +"%")
		
aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())