import random
import string

def password_generator():
        
    while True:

        print('GERADOR DE SENHAS')
        print('------------------')
        digitos = int(input('Digite quantos digítos terá sua senha: '))
        if 4 <= digitos <= 10:
            print(f'Senha de {digitos} dígitos gerada com sucesso! Resultado abaixo:')
            print('------------------')
            
            # Criando uma lista com os caracteres obrigatórios da senha

            caracteres_obrigatorios = string.ascii_letters + string.digits + string.punctuation
            senha = [
                random.choice(string.punctuation),
                random.choice(string.ascii_uppercase),
                random.choice(string.ascii_lowercase),
                random.choice(string.digits)]
            
            senha += random.choices(caracteres_obrigatorios, k = digitos-4)
            random.shuffle(senha)
        else:
            print('Entrada inválida! Favor digitar número entre 4 e 10.')
            break
        return ''.join(senha) #transformando o array em string pra visualização ideal pra copiar

senha = password_generator()
print(senha)