#imports necessarios
from base64 import b64decode
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Cipher import DES
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA

def open_envelope(file_in_message, file_in_enc_key, place_private_key_rec, place_dec_message,algorithm_cryt):
        #importa chave privada de bob
        private_key_bob = RSA.import_key(open(place_private_key_rec).read())
        #ler chave de sessao encriptada e transfoma de b64 para o normal
        enc_session_key = b64decode(file_in_enc_key.read())
        #decripta chave de sessao
        cipher_rsa = PKCS1_OAEP.new(private_key_bob)
        session_key = cipher_rsa.decrypt(enc_session_key)
        #PRIMEIRA PARTE DA ABERTURA DO ENVELOPE REALIZADA
        #realizar descriptografia da mensagem usando o AES
        if(algorithm_cryt == ("aes" or "AES")):
                #ler menssagem criptografada
                nonce_aes_tag_cipher_text = b64decode(file_in_message.read())
                nonce_aes = nonce_aes_tag_cipher_text[:16]
                cipher_text = nonce_aes_tag_cipher_text[16:]
                #decripta menssagem
                cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce_aes)
                plaintext = cipher_aes.decrypt(cipher_text)
        #realizar descriptografia da mensagem usando o DES
        if(algorithm_cryt == ("des" or "DES")):
                #ler menssagem criptografada
                nonce_des_ciphertext = b64decode(file_in_message.read())
                nonce_des = nonce_des_ciphertext[0:16]
                cipher_text = nonce_des_ciphertext[16:]
                #decripta menssagem
                cipher_des = DES.new(session_key, DES.MODE_EAX, nonce_des)
                plaintext = cipher_des.decrypt(cipher_text)
        #realizar descriptografia da mensagem usando o RC4
        if(algorithm_cryt == ("rc4" or "RC4")):
                #ler menssagem criptografada 
                nonce_rc4_cipher_text = b64decode(file_in_message.read())
                #ler chave de sessao encriptada e transfoma de b64 para o normal
                nonce_rc4 =  nonce_rc4_cipher_text[0:16]
                cipher_text =  nonce_rc4_cipher_text[16:]
                #decripta menssagem
                tempkey = SHA.new(session_key+nonce_rc4).digest()
                cipher_rc4 = ARC4.new(tempkey)
                plaintext = cipher_rc4.decrypt(cipher_text)
        #SEGUNDA PARTE DA ABERTURA DO ENVELOPE REALIZADA
        #saida do testo em claro
        file_out_message = open(place_dec_message, "wt")
        file_out_message.write(plaintext.decode())
        print(plaintext.decode())
        #fechar arquivos
        file_out_message.close()
        file_in_message.close()
        file_in_enc_key.close()
#menu e inputs pelo teclado
print("Digite o caminhos solicitados, caso queira usar os caminhos padroes, so clicar em enter sem digitar nada")
print("Digite o caminho onde esta a mensagem encriptada: ")
input_file_enc_message = input()
print("Digite o caminho da chave encriptada: ")
input_file_enc_key = input()
print("Digite o caminho onde esta a chave privada do destinatario: ")
input_file_private_key = input()
print("Escolha o algoritmo utilizado na criptografia da menssagem:")
algorithm_cryt = input()
while(algorithm_cryt != "aes" and algorithm_cryt != "AES"  and algorithm_cryt != "des" and algorithm_cryt != "DES" and algorithm_cryt != "RC4" and algorithm_cryt != "rc4" ):
        print("Por favor digite uma entrada valida:")
        algorithm_cryt = input()

#abertura do texto encriptado e chave encriptada e selecao do caminho da chave privada e da menssagem descriptografada
if(input_file_enc_message != ""):
        file_in_enc_message = open(input_file_enc_message,"rb")
else:
        file_in_enc_message = open("bob_receiver/encrypted_message.base64","rb")

if(input_file_enc_key != ""):
        file_in_enc_key = open(input_file_enc_key,"rb")
else:
        file_in_enc_key = open("bob_receiver/encrypted_key.base64", "rb")

if(input_file_private_key == ""):
        input_file_private_key = "bob_receiver/private_key_bob.pem"


input_file_desc_message = "bob_receiver/decrypted_message.txt"

open_envelope(file_in_enc_message, file_in_enc_key, input_file_private_key, input_file_desc_message , algorithm_cryt)