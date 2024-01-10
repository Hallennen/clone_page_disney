import psycopg2


class conecta_no_banco:
    def connect_banco(script,opção=['fetchall','fetchone' or 'insert' ]):
        banco = psycopg2.connect(database='user', user='postgres', password='1804')
        cursor= banco.cursor()
        cursor.execute(script)

        if opção == 'fetchall':
            response = cursor.fetchall()

        elif opção == 'fetchone':
            response = cursor.fetchone()
        
        elif opção == 'insert':
            response = banco.commit()
            print('usuario cadastrado')
        # print(response)
        return response
    