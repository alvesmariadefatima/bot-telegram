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
/finalizaratendimento: Encerrar atendimento
    """
    bot.reply_to(mensagem, texto)

bot.polling()
