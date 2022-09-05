from Crypto.PublicKey import RSA
#imports
#CHAVES DE ALICE
key_alice = RSA.generate(2048)
#cria chave privada de alice e coloca na pasta de alice
private_key_alice = key_alice.export_key()
file_out = open("alice_sender/private_key_alice.pem", "wb")
file_out.write(private_key_alice)
file_out.close()
#cria chave public de alice e coloca na pasta de bob para ficar 'visivel para ele'
public_key_alice = key_alice.publickey().export_key()
file_out = open("bob_receiver/public_key_alice.pem", "wb")
file_out.write(public_key_alice)
file_out.close()

#CHAVES DE BOB

#cria chave privada de bob e coloca na pasta de bob
print("As chaves de Alice foram criadas nas devidas pastas")
key_bob = RSA.generate(2048)
private_key_bob = key_bob.export_key()
file_out = open("bob_receiver/private_key_bob.pem", "wb")
file_out.write(private_key_bob)
file_out.close()
#cria chave public de bob e coloca na pasta de alice para ficar 'visivel para ela'
public_key_bob = key_bob.publickey().export_key()
file_out = open("alice_sender/public_key_bob.pem", "wb")
file_out.write(public_key_bob)
file_out.close()

print("As chaves de Bob foram criadas com sucesso e estao nas devidas pastas")