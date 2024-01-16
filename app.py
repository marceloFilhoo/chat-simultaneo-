import flet as ft

def main(pagina):
    # forma de criar um texto
    titulo = ft.Text('Chat')

    campo_de_chat = ft.Column()

    def enviar_mensagem_tunel(informacoes):
        campo_de_chat.controls.append(ft.Text(informacoes))
        pagina.update()

    #criando a função de enviar a mensagem do chat para o tunel, para o outro usuario
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        
        # colocando antes da mensagem o nome do usuario, tem que usar o f"" serve para formatar/concatenar a string
        mensagem = f"{nome_usuario.value}: {campo_digitar.value}"

        #adicionando texto no campo do chat
        pagina.pubsub.send_all(mensagem)

        #limpando valor da caixa de input
        campo_digitar.value = ""
        pagina.update()
        
    enviar = ft.ElevatedButton("enviar",on_click=enviar_mensagem)

    #evento submit pode ser adiconado nos campos te input para conseguir enviar clicando enter
        #forma para criar um input pro usuario
    campo_digitar = ft.TextField(label="digite sua mensagem aqui", on_submit=enviar_mensagem)
    
    def entrar_chat(evento):
        #fechar popup
        popup.open = False

        #fechar botao inicial
        pagina.remove(butao_iniciar)   

        #adicionando campo de chat  
        pagina.add(campo_de_chat)   

        #enviando a mensagem de entrada no chat
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")

        #adicionando campo de digitar e botao de enviar
            # tem que adicionar uma linha de mensagem com o row para fazer uma fica do lado da outra
        linha_de_mensagem = ft.Row([campo_digitar, enviar])
        pagina.add(linha_de_mensagem)
          
        pagina.update() 

    #criando campo para input do nome do usuario
    nome_usuario =ft.TextField(label='digite seu nome aqui', on_submit=entrar_chat) 

    #criando layout do popup
    popup = ft.AlertDialog( 
        open=False, 
        modal = True, 
        title= ft.Text('chat'),
        content= nome_usuario,
        actions=[ 
            ft.ElevatedButton("entrar", on_click= entrar_chat)
          ])
    
    #iniciando chat
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update() 

    # sempre para fazer a funcionalidade do butao tem que criar uma função
    butao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click= iniciar_chat) 

    #sempre tem que adicionar na pagina 
    pagina.add(titulo)
    pagina.add(butao_iniciar)
    
 
      




ft.app(main) #assim de padrao ele vem como app
#ft.app(main, view=ft.WEB_BROWSER) ele ajusta para web 