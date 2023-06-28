
# Digital envelope

Esta é uma implementação de um envelope digital em Python utilizando a biblioteca pycryptodome que é uma solução poderosa e segura para garantir a integridade e a confidencialidade de dados transmitidos eletronicamente. Um envelope digital é uma técnica criptográfica que combina criptografia simétrica e criptografia assimétrica para proteger informações sensíveis durante a transmissão.

O pycryptodome é uma biblioteca popular e robusta em Python que oferece uma ampla gama de funcionalidades criptográficas, incluindo algoritmos de criptografia simétrica e assimétrica, assinaturas digitais, hashes e muito mais. Com essa biblioteca, é possível implementar facilmente um envelope digital eficiente e seguro.


## Referência

 - [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/)
## Aprendizados

Com esse projeto projeto consegui assimilar melhor conceitos abstratos visto em sala de aula, compreendi como funciona a implementação de criptografia de dados, além de praticar o uso da biblioteca.


## Instalação

Clone o projeto

```bash
  git clone https://github.com/V1ntag3/digital-envelope.git
```

Entre no diretório do projeto

```bash
  cd digital-envelope
```

Instale a biblioteca

```bash
  pip install pycryptodome
```


## Tutorial

#### Opções de desenvolvimento:
- cada pasta representa a visão da Alice(remente) e Bob(destinatário).
- ao rodar o "creation_of_asymmetric_keys.py" são criadas novas keys, substituindo as antigas, logo será necessário encriptar novamente a mensagem.
- a mensagem / texto em claro esta disponível para ser vizualizado e modificado na pasta "alice_sender" e está com o nome de "plaintext.txt".
- é possivel mudar o caminho como é mostrado do menu mas caso não queira está tudo definido por padrão para testes.
- as entradas são feitas por teclado no console basta digitar a abreviação do algoritmo. 

#### Ordem de execução:
- "creation_of_asymmetric_keys.py" - cria as chaves assimetricas - Opicional.
- "digital_envelope_creation.py" - cria o envelope digital.
    - digitar o caminho do texto em claro Ex: "testes/texto.txt".
    - digitar o caminho da chave pública do destinatário Ex: "testes/chave_publica.pem".
    - digitar o algoritmo a ser utilizado Ex: "aes" ou "AES".
- "open_digital_envelope.py" - abre o envelope e mostra a mensagem.
    - digitar o caminho onde esta a mensagem encriptada Ex: "testes/texto_enc.base64".
    - digitar o caminho da chave encriptada Ex: "testes/chave_enc.base64".
    - digitar o caminho onde esta a chave privada do destinatário Ex: "testes/.chave_privada.pem"
    - digitar o algoritmo a ser utilizado Ex: "aes" ou "AES".
## Licença

MIT License

Copyright (c) 2023 Marcos Vinícius Ribeiro Alencar

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
