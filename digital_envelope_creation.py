#imports necessarios
from base64 import b64decode, b64encode
from operator import indexOf
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import DES
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA

def envelope_creation(file_in_message, file_out_key, file_out_message, place_public_key_rec, algorithm_cryt):
        
        #mensagem a ser criptofrada
        plaintext = file_in_message.read().encode("utf-8")
        #criptografa usando o AES
        if(algorithm_cryt == ("aes" or "AES")):
                #criacao da chave assimetrica
                session_key = get_random_bytes(16)
                #PRIMEIRA PARTE DO ENVELOPE REALIZADA
                cipher_aes = AES.new(session_key, AES.MODE_EAX)
                cipher_text = cipher_aes.encrypt(plaintext)
                #salvar criptograma no arquivo
                file_out_message.write( b64encode(cipher_aes.nonce + cipher_text)) 
        #criptografa usando o DES
        if(algorithm_cryt == ("des" or "DES")):
                #criacao da chave assimetrica
                session_key = get_random_bytes(8)
                #PRIMEIRA PARTE DO ENVELOPE REALIZADA
                cipher_des = DES.new(session_key, DES.MODE_EAX)
                cipher_text = cipher_des.encrypt(plaintext)
                #salvar criptograma no arquivo
                file_out_message.write(b64encode(cipher_des.nonce + cipher_text))
        #criptografa usando o RC4
        if(algorithm_cryt == ("rc4" or "RC4")):
                #criacao da chave assimetrica
                session_key = get_random_bytes(16)
                #PRIMEIRA PARTE DO ENVELOPE REALIZADA
                nonce_rc4 = get_random_bytes(16)
                tempkey = SHA.new(session_key+nonce_rc4).digest()
                cipher_rc4 = ARC4.new(tempkey)
                cipher_text = cipher_rc4.encrypt(plaintext)
                #salvar criptograma no arquivo
                file_out_message.write(b64encode(nonce_rc4 + cipher_text))
        #SEGUNDA PARTE DO ENVELOPE REALIZADA
        #chave publica de bob
        public_key_bob = RSA.import_key(open(place_public_key_rec).read())
        #criptografa chave simetrica gerada com a chave publica de bob usando o RSA
        cipher_rsa = PKCS1_OAEP.new(public_key_bob)
        enc_session_key= cipher_rsa.encrypt(session_key)
        #grava chave criptografada em arquivo
        file_out_key.write(b64encode(enc_session_key))
        #fechar arquivos
        file_out_message.close()
        file_out_key.close()
        file_in_message.close()
        #TERCEIRA PARTE DO ENVELOPE REALIZADA
        print("A mensagem foi criptografada com sucesso")

#menu e inputs pelo teclado
print("Digite os caminhos solicitados, caso queira usar os caminhos padroes, so clicar em enter sem digitar nada")
print("Digite o caminho do texto em claro: ")
input_file_message = input()

print("Digite o caminho da chave publica do destinatario: ")
input_file_public_key_rec = input()

print("Escolha o algoritmo de criptografia da menssagem:")
algorithm_cryt = input()

while(algorithm_cryt != "aes" and algorithm_cryt != "AES"  and algorithm_cryt != "des" and algorithm_cryt != "DES" and algorithm_cryt != "RC4" and algorithm_cryt != "rc4" ):
        print("Por favor digite uma entrada valida:")
        algorithm_cryt = input()

#abertura do texto em claro, arquivo que tera a chave encriptada e o texto encriptado
if(input_file_message != ""):
        file_in_message = open(input_file_message,"rt")
else:
        file_in_message = open("alice_sender/plaintext.txt","r")
        
if(input_file_public_key_rec == ""):
        place_public_key_rec = "alice_sender/public_key_bob.pem"

file_out_key = open("bob_receiver/encrypted_key.base64", "wb")
file_out_message = open("bob_receiver/encrypted_message.base64", "wb")

envelope_creation (file_in_message, file_out_key, file_out_message, place_public_key_rec, algorithm_cryt)