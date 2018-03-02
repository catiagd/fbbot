# coding=utf-8
import os,sys,json,random,requests
from fbmq import Page, Attachment, QuickReply, utils
from fbmq import template as Template
from datetime import datetime
from flask import Flask, request
from botheader import buttons, Handle, quickReply
import botheader

page = botheader.page #Alias
app = Flask(__name__) #Guarda o flask em uma app

@app.route('/', methods=['GET'])
def verify():
    # Vai ao endpoint e verifica os tokens, para o webhook
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200

@app.route('/', methods=['POST']) #Caso exista um POST no index do webhook chama a função e decorater seguintes
def webhook():
    page.greeting("Bem vindo, a página da impermonti, empresa de isolamentos, está a falar com respostas automaticas, por favor pergunte-me algo!") #Info da pagina que o bot disponibiliza
    page.show_starting_button("START_PAYLOAD") #Butão de começar que me deu uma dor de cabeça do clrh
    #page.show_persistent_menu([Template.ButtonWeb('Website', 'https://www.leafly.com/')]) #Mostra um menu todo pimposo ao lado
    payload = request.get_data(as_text=True) #Faz um request ao webhook e obtem a data
    print(payload) #Cria o log
    # Processa msg
    page.handle_webhook(payload)
    return "ok", 200

if __name__ == '__main__':
    app.run(debug=True)
