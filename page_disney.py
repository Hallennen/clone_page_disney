from flask import Flask , render_template , request
from conexao_bd import conecta_no_banco


page = Flask(__name__)

@page.route("/", methods=['GET'])
def teste():

    return render_template('disney.html')

@page.route("/passo2", methods=['POST'])
def validar():
    global email_formulario 
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


@page.route("/main", methods=['POST'])
def tela_principal():


    return render_template('main.html', email = email_formulario)


@page.route("/cadastro", methods=['POST'])
def cadastro_email():
    global senha_user_email
    senha_user_email = request.form['senha_email_novo_user']
    # conecta_no_banco.connect_banco('INSERT ITO ')

    return render_template('cadastro_email.html')


@page.route("/testando_cadastro", methods=['POST'])
def cadastro():
    nome = request.form['name']
    idade = request.form['IDADE']
    cidade = request.form['CIDADE']
    rua = request.form['RUA']
    cpf= request.form['CPF']
    cpf_arrumado = cpf[:3]  + '.'  + cpf[3:6] + '.'+ cpf[6:9]+'-' + cpf[9:]
    
    telefone= request.form['TELEFONE']
    telefone_arrumado = telefone[:2]  + ' '  + telefone[2:7] + '-' + telefone[7:]
    permissao = 'padrão'

    # print(nome, idade, cidade, rua, cpf, telefone, email_formulario, senha_user_email, permissao )
    print('deu certo, passou no teste1')
    conecta_no_banco.connect_banco(f'''INSERT INTO logins (user_id,nome,idade,cidade,rua,cpf,telefone,email,senha,permissao)
                                        VALUES ('22','{nome}','{idade}','{cidade}', '{rua}', '{cpf_arrumado}', '{telefone_arrumado}','{email_formulario}', '{senha_user_email}', '{permissao}') ''', 'insert')


    return teste()
    # return ('<H1> TESTE OK </H1>')

page.run(host='localhost',port=5000 , debug=True)











# class cadastro_de_user():
#     def cadastro_email(self):

#         return render_template('cadastro_email.html')

#     def cadastro_no_banco(self):

#         return render_template('disney.html')