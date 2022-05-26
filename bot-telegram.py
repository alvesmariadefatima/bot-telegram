from click import command
import telebot

CHAVE_API = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=['manha'])
def consultamanha(mensagem):

        print(mensagem)
        texto = '''
Selecione o melhor horário disponível: 
/0700 - Sete horas da manhã
/0750 - Sete e cinquenta da manhã
/0800 - Oito horas da manhã
/0850 - Oito e cinquenta da manhã
/0900 - Nove horas da manhã
/0950 - Nove e cinquenta da manhã
/1000 - Dez horas da manhã
/1050 - Dez e cinquenta da manhã
/1100 - Onze horas da manhã
/1150 - Onze e cinquenta da manhã

        '''
        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1400'])
def horariomarcado1400(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1450'])
def horariomarcado1450(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1500'])
def horariomarcado1500(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1550'])
def horariomarcado1550(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1600'])
def horariomarcado1600(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1650'])
def horariomarcado1650(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1700'])
def horariomarcado1700(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1750'])
def horariomarcado1750(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1800'])
def horariomarcado1800(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1850'])
def horariomarcado1850(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1900'])
def horariomarcado1900(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1950'])
def horariomarcado1950(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['2000'])
def horariomarcado2000(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['2050'])
def horariomarcado2050(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['2100'])
def horariomarcado2100(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['2150'])
def horariomarcado2150(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['tarde'])
def consultatarde(mensagem):

        print(mensagem)
        texto = '''
Selecione o melhor horário disponível: 
/1400 - Duas horas da tarde
/1450 - Duas e cinquenta da tarde
/1500 - Três horas da tarde
/1550 - Três e cinquenta da tarde
/1600 - Quatro horas da tarde
/1650 - Quatro e cinquenta da tarde
/1700 - Cinco horas da tarde
/1750 - Cinco e cinquenta da tarde
/1800 - Seis horas da tarde
/1950 - Sete e cinquenta da noite
/2000 - Oito horas da noite
/2050 - Oito e cinquenta da noite
/2100 - Nove horas da noite
/2150 - Nove e cinquenta da noite
        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['0700'])
def horario0700(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['0750'])
def horariomarcado0750(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['0800'])
def horariomarcado0800(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['0850'])
def horariomarcado0850(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['0900'])
def horariomarcado0900(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['0950'])
def horariomarcado0950(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''
        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1000'])
def horariomarcado1000(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''
        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1050'])
def horariomarcado1050(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''
        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1100'])
def horariomarcado1100(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''
        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['1150'])
def horariomarcado1150(mensagem):
        print(mensagem)
        texto='''
SELECIONE O DIA DISPONÍVEL (Para o mês de Junho):

/dia01: 01/06
/dia10: 10/06
/dia15: 15/06
/dia20: 20/06
/dia25: 25/06

        '''
        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['dia01'])
def consultadia01(mensagem):
        print(mensagem)
        texto='''
Agendamento feito com sucesso!!! 
        
Compareça ao hospital no dia e horário agendado pelo assistente virtual.

Clique em /finalizaratendimento para encerrar.
        '''
        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['dia10'])
def consultadia10(mensagem):
        print(mensagem)
        texto='''
Agendamento feito com sucesso!!! 
        
Compareça ao hospital no dia e horário agendado pelo assistente virtual.

Clique em /finalizaratendimento para encerrar.
        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['dia15'])
def consultadia15(mensagem):
        print(mensagem)
        texto='''
Agendamento feito com sucesso!!! 
        
Compareça ao hospital no dia e horário agendado pelo assistente virtual.

Clique em /finalizaratendimento para encerrar.

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['dia20'])
def consultadia20(mensagem):
        print(mensagem)
        texto='''
Agendamento feito com sucesso!!! 
        
Compareça ao hospital no dia e horário agendado pelo assistente virtual.

Clique em /finalizaratendimento para encerrar.

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['dia25'])
def consultadia25(mensagem):
        print(mensagem)
        texto='''
Agendamento feito com sucesso!!! 
        
Compareça ao hospital no dia e horário agendado pelo assistente virtual.

Clique em /finalizaratendimento para encerrar.

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['perguntasfrequentestriagem'])
def perguntasfrequentestriagem(mensagem):
        print(mensagem)

        bot.send_message(mensagem.chat.id, '1) Quem (paciente/acompanhante) e quando deve fazer a troca da MÁSCARA?')
        bot.send_message(mensagem.chat.id, 'R: Paciente: deve ser trocada ao entrar na instituição, neste momento é oferecido uma máscara de procedimento.')
        bot.send_message(mensagem.chat.id, 'Acompanhante: a troca da máscara não precisa ser realizada, mas se ele quiser, pode ser realizada.')

        bot.send_message(mensagem.chat.id, '2) O que devo fazer quando houver recusa para a troca da MÁSCARA?')

        bot.send_message(mensagem.chat.id, 'R: Orientar o paciente, explicar o porquê da troca, garantimos que ela possui certificações de filtragem, oferece maior segurança em relação à máscara de tecido')

        bot.send_message(mensagem.chat.id, '3) Como devo oferecer a MÁSCARA para que seja feita a troca?')

        bot.send_message(mensagem.chat.id, 'R: Abordar o paciente de forma cordial, oferecer e explicar o motivo da troca. Recomendamos que segure pelo elástico lateral da máscara e peça para o paciente pegar pelo elástico do lado contrário ao que você está segurando.')

        bot.send_message(mensagem.chat.id, '4) O que fazer quando o acompanhante estiver com MÁSCARA com válvula?')
        bot.send_message(mensagem.chat.id, ' R: Oferecer a troca da máscara e explicar o motivo da mesma dever ser trocada. A válvula serve para facilitar a retirada do ar quente de dentro da máscara. Não é indicada em ambientes hospitalares e em pessoas com suspeitas de síndrome gripal, pois no momento da expiração a válvula abre e pode liberar alguma partícula no ar.')

        bot.send_message(mensagem.chat.id, '5) O que fazer quando faltar ÁLCOOL com acionamento automático?')
        bot.send_message(mensagem.chat.id, 'R: No momento estamos passando por mudança da marca de álcool na instituição. O álcool a ser utilizado será a bag em dispenser distribuídos nas unidades ou em frascos, quando a apresentação for em frascos, ressaltamos a importância de o colaborador colocar na mão do paciente/acompanhante sem tocar na saída do frasco, assim evitamos que eles toquem nos frascos.')

        bot.send_message(mensagem.chat.id, '6) Como proceder quando PACIENTE relatar que está aguardando o RESULTADO do EXAME para detectar COVID-19, como protocolo pré-operatório?')
        bot.send_message(mensagem.chat.id, 'R: Segue fluxo paciente sem sintomas.')

        bot.send_message(mensagem.chat.id, '7) Como proceder quando PACIENTE não possui sintoma e relata que está aguardando o RESULTADO do EXAME para detectar COVID-19?')
        bot.send_message(mensagem.chat.id, 'R: Questionar o motivo da coleta do exame e qual exame coletado (desconsiderar sorologia - sangue, considerar apenas PCR-swab nasal orofaringe). Se coleta ocorreu devido sinais sugestivos de COVID-19, comunicar área de atendimento e verificar possibilidade de reagendamento. Se coleta em paciente assintomático seguir o atendimento.')

        bot.send_message(mensagem.chat.id, '8) Como proceder quando o PACIENTE relatar que está com COVID-19 e tem procedimento agendado (curativo, QT, RXT)?')
        bot.send_message(mensagem.chat.id, 'R: Curativo: já existe fluxo definido para atendimento. O setor confere os pacientes com COVID-19, que serão atendidos no dia anterior, a recepção é informada e encaminha o paciente direto ao consultório, informar e confirmar com o setor QT e RXT: informar e confirmar com o setor.')

        bot.send_message(mensagem.chat.id, '9) Como proceder quando o ACOMPANHANTE relatar que está com COVID-19 ou aguardando o resultado do exame para detectar COVID-19?')
        bot.send_message(mensagem.chat.id, 'R: Orientar ao mesmo que por razões de suspeita ou confirmação de COVID-19, não pode adentrar na instituição, pois ele deveria estar em isolamento social, seguindo as recomendações de prevenção de transmissão do vírus. Seguindo as orientações do fluxo de triagem ambulatorial.')

        bot.send_message(mensagem.chat.id, '10. Como proceder em relação à MÁSCARA quando paciente for criança?')
        bot.send_message(mensagem.chat.id, 'R: Criança a partir dos 6 anos devem utilizar máscara. Para crianças que já chega utilizando a máscara de tecido, não efetuar a troca devido à dificuldade de ajustar a mascara de procedimento no rosto e possível dificuldade de aceitação pela criança.')

        bot.send_message(mensagem.chat.id, ' 11. Como deve ser o acondicionamento da MÁSCARA em uso pelo paciente, quando é necessária a troca?')
        bot.send_message(mensagem.chat.id, ' R: A máscara deve ser condicionada em saco plástico pelo paciente e ou acompanhante.')

        bot.send_message(mensagem.chat.id, '12. O que fazer quando o paciente solicitar ajuda para acondicionar a MÁSCARA no saco plástico?')
        bot.send_message(mensagem.chat.id, 'R: Ajuda deve ser fornecida de forma que o colaborador não manipule a máscara do paciente, e após higienizar as mãos.')

        bot.send_message(mensagem.chat.id, '13. Como proceder com uso de MÁSCARA em paciente traqueostomizado?')
        bot.send_message(mensagem.chat.id, 'R: Oferecer duas máscaras uma para cobrir boca e nariz e a outra para cobrir a traqueostomia. Neste caso utilizar a máscara cirúrgica, que possui as tiras adequadas para serem amarradas na região cervical.')

        bot.send_message(mensagem.chat.id, '14. Como proceder quando paciente e ou acompanhante estiver de LUVA?')
        bot.send_message(mensagem.chat.id, 'R: Orientar para retirar as luvas e higienizar higienização as mãos. Caso recuse retirar as luvas não permitir a entrada.')

        bot.send_message(mensagem.chat.id, '15. Quando devo HIGIENIZAR as MÃOS durante a realização da triagem?')
        bot.send_message(mensagem.chat.id, 'R: Antes e após o contato com o paciente, e após auxiliar na guarda da máscara no saco plástico.')

        bot.send_message(mensagem.chat.id, '16. Quando o paciente e acompanhante deve HIGIENIZAR as MÃOS?')
        bot.send_message(mensagem.chat.id, 'R: Ao entrar no hospital ambos devem higienizar as mãos.')

        bot.send_message(mensagem.chat.id, '17.O que são SINAIS e SINTOMAS leves?')
        bot.send_message(mensagem.chat.id, ' R: Calafrio, tosse e coriza crônica (mais de 15 dias), dor no corpo generalizada e um pico de febre referida.')

        bot.send_message(mensagem.chat.id, '18. O que são SINAIS e SINTOMAS graves?')
        bot.send_message(mensagem.chat.id, 'R: Falta de ar, febre maior que 37.8°C, dor ao respirar e sonolência associada a sintoma leve.')

        bot.send_message(mensagem.chat.id, '19. Quais os SINAIS e SINTOMAS específicos para COVID-19?')
        bot.send_message(mensagem.chat.id, 'R: Dor de garganta, perda do olfato e do paladar, coriza ou tosse menos de 15 dias.')

        bot.send_message(mensagem.chat.id, '20. Como proceder quando PACIENTE relatar sinais e sintomas leves (Calafrio, tosse e coriza crônica (mais de 15 dias), dor no corpo generalizada e um pico de febre referida)?')
        bot.send_message(mensagem.chat.id, 'R: Liberar o paciente para o atendimento.')

        bot.send_message(mensagem.chat.id, '21.Como proceder quando PACIENTE apresentar temperatura ≥37,8 e ou relatar sinais e sintomas graves e específicos de COVID-19 (Falta de ar, febre maior que 37.8°C, dor ao respirar e sonolência associada a sintoma leve, dor de garganta, perda do olfato e do paladar, coriza ou tosse menos de 15 dias)?')
        bot.send_message(mensagem.chat.id, 'R: Encaminhar para o pronto socorro.')

        bot.send_message(mensagem.chat.id, '22. Como proceder quando ACOMPANHANTE relatar sinais e sintomas leves ou graves sugestivos de COVID-19 ou apresentar temperatura ≥ 37,8?')
        bot.send_message(mensagem.chat.id, 'R: Orientar que ele não pode entrar na instituição, que deve ficar em isolamento social ou procurar atendimento médico para uma melhor avaliação. Seguindo as orientações do fluxo de triagem ambulatorial.')

        bot.send_message(mensagem.chat.id, '23.Como proceder quando ACOMPANHANTE relatar que está aguardando o resultado do exame para detectar COVID-19 e não segue a orientação de retornar para casa?')
        bot.send_message(mensagem.chat.id, 'R: Neste caso comunicar responsáveis da triagem para apoio.')

        bot.send_message(mensagem.chat.id, '24. Como proceder caso o PACIENTE ou ACOMPANHANTE seja AGRESSIVO na triagem?')
        bot.send_message(mensagem.chat.id, 'R: Solicitar apoio da supervisão de cada unidade.')

        bot.send_message(mensagem.chat.id, '25. Como proceder caso o PACIENTE ou ACOMPANHANTE se recuse a cumprir as medidas preventivas contra o COVID-19?')
        bot.send_message(mensagem.chat.id, 'R: Não permitir entrada na instituição e solicitar apoio da supervisão de cada unidade.')

        bot.send_message(mensagem.chat.id, '26. Quais EPIs devem ser utilizados para realizar a triagem?')
        bot.send_message(mensagem.chat.id, 'R: Máscara de procedimento e óculos de proteção individual.')

        bot.send_message(mensagem.chat.id, '27. Pode ser utilizado UNIFORME PRIVATIVO pelo profissional que realiza a triagem?')
        bot.send_message(mensagem.chat.id, 'R: Do ponto de vista do SCIH pode utilizar, porém não é necessário para realizar a triagem, a questão do uso seria um ponto discutido pela área responsável pela triagem.')

        bot.send_message(mensagem.chat.id, 'Caso queira encerrar o atendimento virtual, clique em /finalizaratendimento.')


        bot.reply_to(mensagem)


@bot.message_handler(commands=['realizarcadastro'])
def realizarcadastro(mensagem):
    texto = '''
Para realizar o cadastro, vá até a recepção do hospital e traga seu RG, CPF e Comprovante de Residência Atualizado (dos últimos 6 meses).

Caso queira encerrar o atendimento virtual, clique em /finalizaratendimento.
    '''        
    
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['clinicogeral'])
def consultaclinicogeral(mensagem):
        
        print(mensagem)
        texto = '''
AGENDAMENTO - CLÍNICO GERAL

SELECIONE O TURNO DESEJADO:

/manha: Agendar para o turno matutino
/tarde: Agendar para o turno vespertino

Caso queira encerrar o atendimento virtual, clique em /finalizaratendimento.

    ''' 

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['pediatra'])
def consultapediatra(mensagem):

        print(mensagem)
        texto = '''
AGENDAMENTO - PEDIATRA

SELECIONE O TURNO DESEJADO:

/manha: Agendar para o turno matutino
/tarde: Agendar para o turno vespertino

Caso queira encerrar o atendimento virtual, clique em /finalizaratendimento.

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['nutricionista'])
def consultanutricionista(mensagem):

        print(mensagem)
        texto = '''
AGENDAMENTO - NUTRICIONISTA

SELECIONE O TURNO DESEJADO:

/manha: Agendar para o turno matutino
/tarde: Agendar para o turno vespertino

PARA VOLTAR AO MENU PRINCIPAL, CLIQUE EM /menu ou /finalizaratendimento para encerrar.

        '''

        bot.reply_to(mensagem, texto)


@bot.message_handler(commands=['psiquiatra'])
def consultapsiquiatra(mensagem):

        print(mensagem)
        texto = '''
AGENDAMENTO - PSIQUIATRA

SELECIONE O TURNO DESEJADO:

/manha: Agendar para o turno matutino
/tarde: Agendar para o turno vespertino

Caso queira encerrar o atendimento virtual, clique em /finalizaratendimento.
        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['dentista'])
def consultapsiquiatra(mensagem):

        print(mensagem)
        texto = '''
AGENDAMENTO - DENTISTA  

SELECIONE O TURNO DESEJADO:

/manha: Agendar para o turno matutino
/tarde: Agendar para o turno vespertino

Caso queira encerrar o atendimento virtual, clique em /finalizaratendimento.
        '''
        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['ginecologista'])
def consultaginecologista(mensagem):

        print(mensagem)
        texto = '''
AGENDAMENTO - CLÍNICO GERAL

SELECIONE O TURNO DESEJADO:

/manha: Agendar para o turno matutino
/tarde: Agendar para o turno vespertino

Para voltar ao menu principal, CLIQUE EM /menu ou /finalizaratendimento para encerrar.

        '''
        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['fisioterapia'])
def consultafisioterapia(mensagem):

        print(mensagem)
        texto='''
AGENDAMENTO - FISIOTERAPIA

SELECIONE O TURNO DESEJADO:

/manha: Agendar para o turno matutino
/tarde: Agendar para o turno vespertino

Caso queira encerrar o atendimento virtual, clique em /finalizaratendimento.
        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['agendarconsulta'])
def perguntasfrequentestriagem(mensagem):
        print(mensagem)
        texto = '''
AGENDAMENTO/MARCAÇÃO DE CONSULTA

Selecione a especialidade médica desejada:

/clinicogeral: Marcar consulta clínico geral
/pediatra: Marcar consulta pediatra
/nutricionista: Marcar consulta nutricionista
/psiquiatra: Marcar consulta psiquiatra
/dentista: Marcar consulta dentista
/ginecologista: Marcar consulta ginecologista
/fisioterapia: Marcar consulta fisioterapia

Caso queira encerrar o atendimento virtual, clique em /finalizaratendimento.

        '''

        bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['horariofuncionamento'])
def horariofuncionamento(mensagem):
        print(mensagem)
        bot.send_message(mensagem.chat.id, 'Horário de funcionamento: 7h às 22h')
        bot.send_message(mensagem.chat.id, 'Caso queira encerrar o atendimento virtual, clique em /finalizaratendimento.')

@bot.message_handler(commands=['finalizaratendimento'])
def finalizaratendimento(mensagem):
        print(mensagem)
        bot.send_message(mensagem.chat.id, 'Seu atendimento virtual foi finalizado!!!')

def verificar(mensagem):
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
Olá, sou seu assistente virtual e irei te ajudar por aqui.

Escolha uma das opções para continuar (clique no item):
/realizarcadastro: Fazer cadastro
/agendarconsulta: Realizar marcação de consulta médica
/horariofuncionamento: Mostrar horário de funcionamento
/perguntasfrequentestriagem: Exibir perguntas frequentes para triagem
/finalizaratendimento: Encerrar atendimento
    """
    bot.reply_to(mensagem, texto)

bot.polling()
