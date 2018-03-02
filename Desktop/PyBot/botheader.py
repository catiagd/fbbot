# coding=utf-8
import os,sys,json,random,requests,unicodedata
from fbmq import Page, Attachment, QuickReply, utils
from fbmq import template as Template
from datetime import datetime
from flask import Flask, request


token = "EAAXucKw0xEwBAGMKSa2ZBHy6kW2rCDJVz9ZBKioho7EiDOPNFJs3IvKcBrVWesDnYzZCfL4uytPnY2HYTTWdbPvPvIaT97RvTcuhRAJSZB2GJLV5RsZCfzLbeTkNSmWLgJhWyNNjgQkQxh0rciNhWo4Skv29CQjLZAZCeq5rysgyAZDZD"
page = Page(token)
QuestaoPaga=["quais sao as opcoes de pagamento?","como posso pagar?","pagar"]
QuestaoPreco=["quanto custam os produtos?","preco","quanto custa?","quanto e?", "quanto é que os teus serviços custam?"]
saudacoes = ["bom dia","boa tarde","boa noite","ola","boas"]
vidal = ["qual o segredo da vida?","qual o proposito de viver","existe um suprasumo da sapiencia"]
nome = ["como te chamas?","quem es tu?","qual o teu nome?"]
perg_area = ["em que areas opera?", "o que fazem?", "qual a area da empresa?"]
perg_servc=["posso saber mais sobre um serviço?", "que servicos tem em particular?","que servicos oferecem?"]
smile=[":D",":P",":)",";)",":*"]
#moderator = [2199242023423175] #ID Pedro e Cátia

class buttons:
    btnmenu = [
        Template.ButtonPostBack("Serviços", "MUSIC_PAYLOAD"),
        Template.ButtonPostBack('"Produtos recreativos"',"PROD_PAYLOAD"),
        Template.ButtonPostBack("Ajuda","AJUDA_PAYLOAD")
    ]

class quickReply:
        quick_musica = [{'title': 'Rock', 'payload': 'PICK_ROCK'},
                        {'title': "Rn'B", 'payload': 'PICK_RnB'},
                        {'title': 'Pop', 'payload': 'PICK_POP'},
                        {'title': 'Indie', 'payload': 'PICK_INDIE'},
                        {'title': 'Classic', 'payload': 'PICK_CLASSIC'},
                        {'title': 'Metal', 'payload': 'PICK_METAL'}]
        default_menu = [{'title': 'Menu','payload': 'PICK_MENU'},
                        {'title': 'Preços','payload': 'PICK_PRECO'},
                        {'title': 'Música do dia','payload':'PICK_MUS'}]
        def get_music(genre):
            if genre == "PICK_ROCK":
                playlist = ["https://www.youtube.com/watch?v=YR5ApYxkU-U&list=RDYR5ApYxkU-U&t=1","https://www.youtube.com/watch?v=fJ9rUzIMcZQ&list=RDEMbHaAxpOZhcVmmF6I3y0siA","https://www.youtube.com/watch?v=s88r_q7oufE&list=RDEMu-D7kEFynn1tn5qmluVnhw","https://www.youtube.com/watch?v=v2AC41dglnM&list=RDEMDs8vWIQKMflBG8QUQQaUrw"]
            elif genre == "PICK_INDIE":
                playlist = ["https://www.youtube.com/watch?v=VEpMj-tqixs&list=RDQMLJaf3zcef1I","https://www.youtube.com/watch?v=A-Tod1_tZdU&list=RDEMhK9GwO7FT3oWyTWGsPuSrg","https://www.youtube.com/watch?v=_DjE4gbIVZk&list=RD_DjE4gbIVZk&t=2","https://www.youtube.com/watch?v=bpOSxM0rNPM&list=RDEMThYJ2VcXXNp3GM7AwT24UQ","https://www.youtube.com/watch?v=_lMlsPQJs6U&list=RD_lMlsPQJs6U&t=2"]
            elif genre == "PICK_POP":
                playlist = ["https://www.youtube.com/watch?v=Zi_XLOBDo_Y&list=RDEMe12_MlgO8mGFdeeftZ2nOQ","https://www.youtube.com/watch?v=EDwb9jOVRtU&list=RDEMaN9C20MoM3K8E1iVi3CAmg","https://www.youtube.com/watch?v=v0KpfrJE4zw&list=RDEM_0ItSElzQ0VS4lssmoXyeg"]
            elif genre == "PICK_RnB":
                playlist = ["https://www.youtube.com/watch?v=rywUS-ohqeE&list=RDEMWzjnvwhEBiIfo26pzdGUgw","https://www.youtube.com/watch?v=0CFuCYNx-1g&list=RD0CFuCYNx-1g"]
            elif genre == "PICK_METAL":
                playlist = ["https://www.youtube.com/watch?v=CD-E-LDc384&list=RDEMAkKpoB62G5Wmtp0nQxfrDg","https://www.youtube.com/watch?v=F_6IjeprfEs&list=RDF_6IjeprfEs&t=1","https://www.youtube.com/watch?v=KF96MQbDkMQ&list=RDKF96MQbDkMQ","https://www.youtube.com/watch?v=Ff54AQaDGbs&list=RDFf54AQaDGbs&t=1","https://www.youtube.com/watch?v=CSvFpBOe8eY&list=RDEMRoCx7NEN4B1lXoHSAiz26w"]
            elif genre == "PICK_CLASSIC":
                playlist = ["https://www.youtube.com/watch?v=O6NRLYUThrY","https://www.youtube.com/watch?v=W-fFHeTX70Q","https://www.youtube.com/watch?v=6JQm5aSjX6g",""]
            return random.choice(playlist)

class Handle:
    def get_num(): #Obtem um numero random entre 1 e 2
        numbergen=[1,2]
        return random.choice(numbergen)
    def get_att(tipo): #Obtem uma imagem random para enviar
        if tipo == 'image':
            exemplos = ["https://cdn.shopify.com/s/files/1/0862/4240/products/1_0d691e32-3771-402a-aaee-dc004ea1b2c3.jpeg?v=1441091543","https://vignette.wikia.nocookie.net/harrypotter/images/2/27/Happy-guy-thumbs-up-300x237.gif/revision/latest?cb=20121019041406"]

        if tipo == 'thumbs':
            exemplos =["http://static.twentytwowords.com/wp-content/uploads/Thumbs-and-Ammo-02.jpg","http://4.bp.blogspot.com/-EGzuN7Jcj0I/UUnR1Y0xWQI/AAAAAAAAA2Q/XMK6_yMNYPo/s1600/ChuckNorristhumbsup+Emil+P.jpg"]
        return random.choice(exemplos)

    def get_message(tipo): #Obtem uma msg random para enviar
        if tipo == 'image':
            exemplos= ["Lindo/a","Que giro","Wow"]
        elif tipo == 'video':
            exemplos=["ja vejo esse video", "video giro", "spectalucaaah"]
        elif tipo == 'audio':
            exemplos=["já oiço", "voz sexy", "say whaaaaa!"]
        elif tipo == 'smile':
            return random.choice(smile)
        elif tipo  == 'text':
            exemplos = ["Peço imensa desculpa, não pense que sou um bot burro.....DITO ISTO.... Não faço ideia do que disse... sorry, mas os nossos donos serão avisados :D","Não sei essa palavra :c Desculpa! Mas os nossos donos foram avisados!","Bolas, peço imensa desculpa mas não o consigo ajudar, os meus donos serão avisados "]
        return (random.choice(exemplos)+' -signed bot')

@page.handle_message
def message_handler(event): #Trabalha as msg
    sender_id = event.sender_id #O id da pessoa que envia a msg
    timestamp = event.timestamp #timestamp
    message = event.message #A mensagem
    page.typing_on(sender_id) #Faz com que aquelas bolinhas fancy aparecam
    page_id = page.page_id #O id da nossa pagina
    page_name = page.page_name #O nome da nossa pagina
    user_profile = page.get_user_profile(sender_id) #Infos do user em formato de dicionario
    nomeuser=(user_profile.get("first_name")+" "+user_profile.get("last_name")) #Log sobre o user
    print(user_profile)
    if message.get("attachments"): #se a msg é um attachments
        if 'image' in str(message.get("attachments")): #Se e uma imaghem
            if '369239263222822' in str(message.get("attachments")): #Se e o fixezinho
                image_url=Handle.get_att('thumbs')
                page.send(sender_id,Attachment.Image(image_url))
            else: #Imagem normal
                if Handle.get_num() == 1: #Envia txt
                    msg=Handle.get_message('image')
                    page.send(sender_id,msg)
                else: #Envai imagem
                    image_url=Handle.get_att('image')
                    page.send(sender_id,Attachment.Image(image_url))
        elif 'video' in str(message.get("attachments")): #Se for video
            msg=Handle.get_message('video')
            page.send(sender_id,msg)
        elif 'audio' in str(message.get("attachments")): #Se for audio
            msg=Handle.get_message('audio')
            page.send(sender_id,msg)
        elif 'file' in str(message.get("attachments")): #Se for file
            page.send(sender_id,"Files são dubios")
        else: #Fault tolerance
            page.send(sender_id,"Já o vou ver! :D")
    elif message.get("quick_reply"): #Se for um quick_reply
        if "PICK_MENU" in str(message.get("quick_reply")): #Se tiver escolhido o menu
            page.send(sender_id,Template.Buttons("Nosso menu",buttons.btnmenu))
        elif "PICK_MUS" in str(message.get("quick_reply")): #Se tiver escolhido o menu de musica
            page.send(sender_id,"Qual é o seu genero de música favorito?",quick_replies=quickReply.quick_musica,metadata="TEST")
        elif "PICK_PRECO" in str(message.get("quick_reply")): #Se tiver escolhido o Preço
            page.send(sender_id,"Deste momento não disponibilizamos preços. Obrigado.")
        else: #Se for de um genero musical
            video_url=quickReply.get_music((message.get("quick_reply")).get('payload'))
            page.send(sender_id,video_url)
    elif message.get("text"): #Se for texto
        message = event.message_text #Guarda o texto
        print(message)
        message = unicodedata.normalize('NFKD', message).encode('ASCII', 'ignore').decode().lower() #nomralliza a string
        if message.upper() in smile:
            page.send(sender_id,Handle.get_message('smile'))
        elif message in QuestaoPreco:
            page.send(sender_id,"o range é de 10 a 100 euros")
        elif message in saudacoes:
            page.send(sender_id,"Saudações")
        elif message in vidal:
            page.send(sender_id, "a resposta é sempre DARIO\n https://www.youtube.com/watch?v=vTIIMJ9tUc8")
        elif message in nome:
            page.send(sender_id, "eu sou o Bot, um robot simpático")
        elif message == ('gostas de pigoitinhas?'):
            page.send(sender_id, "eu sim, o marco só deles duros")
        elif message in perg_area:
            page.send(sender_id, "estamos na area da diversão, vendemos produtos recriativos :)")
        elif message in perg_servc:
           page.send(sender_id, "questões mais especificas serão remetidas para os administradores da págida e respondidas com a maior brevidade possivel")
        elif message == "menu":
            page.send(sender_id,Template.Buttons("Nosso menu",buttons.btnmenu))
        else: #Mensagem default caso o bot nao saiba o que fazer
            msg = Handle.get_message('text')
            page.send(sender_id,msg,quick_replies=quickReply.default_menu,metadata="TEST")
##            for x in moderator: #manda para os donos a dizer que houve porcaria
##                page.send(x,"Ocorreu um problema hoje, não soube responder a algo que o {} perguntou-me. Sorry :(".format(nomeuser))
@page.handle_postback #Quando recebe um postback
def received_postback(event):
    sender_id = event.sender_id
    recipient_id = event.recipient_id
    time_of_postback = event.timestamp
    payload = event.postback_payload #Obtem a payload
    print("Postback de {} recebido. Payload de :{}".format(sender_id,payload)) #LOG
    if payload == "START_PAYLOAD": #Se o get started ter sido pressionado
        page.send(sender_id,Template.Buttons("Nosso menu",buttons.btnmenu))
    elif payload == "MUSIC_PAYLOAD": #Se o butao de musica ser pressionado
        page.send(sender_id,"Qual é o seu genero de música favorito?",quick_replies=quickReply.quick_musica,metadata="TEST")
    elif payload == "AJUDA_PAYLOAD": #Se for de ajuda
        page.send(sender_id,"Pode-me dizer, a qualquer altura 'menu' e eu irei te mostrar o menu! :D")
    elif payload == "PROD_PAYLOAD": #Se for de "Produtos recreativos"
        page.send(sender_id,"Temos uma variada range de produtos.\nCarregue no menu ao seu lado esquerdo, para ir ao nosso website")

@page.handle_delivery #Para verificar que a msg e enviada com sucesso
def received_delivery_confirmation(event):
    delivery = event.delivery
    message_ids = delivery.get("mids")
    if message_ids:
        for message_id in message_ids:
            print("O user recebeu a msg nº %s" % message_id)

@page.handle_read #Para verificar se o user le a msg
def received_message_read(event):
    print("O user leu a mensagem")
