from flask import Flask , render_template , request
from conexao_bd import conecta_no_banco


page = Flask(__name__)

@page.route("/", methods=['GET'])
def teste():

    return render_template('disney.html')

@page.route("/passo2", methods=['POST'])
def validar():
    email_formulario = request.form['email_user']

    
    try:
        busca = conecta_no_banco.connect_banco('SELECT email FROM logins',opção='fetchall')
        for item in busca:
            print(item[0])
            if email_formulario == item[0]:
                print(True)
                retorno = render_template('disney_passo2.html', email = email_formulario)
                break
            else:
                retorno = render_template('disney_error.html', email= email_formulario)

        return retorno
                
    except:
        print()


page.run(host='localhost',port=5000 , debug=True)
