# Trabalho 01 - Implementação de Transferência de Arquivos Confiável sobre UDP com Sockets

## Objetivo do Projeto:
Desenvolver uma aplicação cliente-servidor para transferência de arquivos utilizando o protocolo UDP. O foco principal é a implementação de mecanismos básicos de controle e confiabilidade diretamente sobre UDP, simulando funcionalidades que o TCP oferece nativamente.

## Requisitos Gerais:
1. Linguagem de Programação: A escolha da linguagem é livre (ex: Python, Java, C/C++, etc.).
2. Restrição de Bibliotecas: Não é permitido o uso de bibliotecas de alto nível que abstraiam a manipulação direta do protocolo UDP. A implementação deve utilizar a API de sockets do sistema operacional (ou da linguagem escolhida) para criar, enviar e receber datagramas UDP.
3. (Opcional/Sugestão) Recomenda-se iniciar com um exemplo simples “Hello World” cliente/servidor UDP para familiarização com a API de sockets antes de abordar a transferência de arquivos.
   
## Requisitos do Servidor UDP:
1. Inicialização: O servidor deve ser executado antes do cliente.
2. Porta: Deve operar em uma porta UDP especificada, com número maior que 1024 (portas abaixo de 1024 geralmente exigem privilégios de administrador).
3. Recepção e Protocolo:
   
    a- Aguardar conexões/mensagens de clientes.
    b- Interpretar as requisições recebidas. É necessário definir e implementar um protocolo de aplicação simples sobre UDP para que o cliente requisite arquivos (Exemplo de formato de requisição: GET /nome_do_arquivo.ext).
   
4. Processamento da Requisição:
   
    a- Verificar se o arquivo solicitado existe.
   
    b- Se o arquivo não existir: Enviar uma mensagem de erro claramente definida pelo seu protocolo para o cliente.
  
5. Transmissão do Arquivo (se existir):
   
    a- O arquivo a ser transmitido deve ser relativamente grande (ex: > 1 MB) para justificar a segmentação.

    b- Segmentação: Dividir o arquivo em múltiplos segmentos/pedaços para envio em datagramas UDP.
   
    c- Cabeçalho Customizado: Cada segmento enviado deve conter informações de controle definidas pelo seu protocolo (ver “Considerações de Protocolo” abaixo).
   
    d- Retransmissão: Implementar lógica para reenviar segmentos específicos caso o cliente solicite (devido a perdas ou erros).
   
## Requisitos do Cliente UDP:

1. Inicialização: O cliente deve ser executado após o servidor estar ativo.
   
2. Conexão: Permitir que o usuário especifique o endereço IP e a porta do servidor UDP ao qual deseja se conectar.
   
3. Requisição:
   
    a- Enviar uma requisição ao servidor, utilizando o protocolo de aplicação definido, para solicitar um arquivo específico (Exemplo de entrada do usuário: @IP_Servidor:Porta_Servidor/nome_do_arquivo.ext).
   
4. Simulação de Perda:
   
    a- Implementar uma opção (ex: via entrada do usuário ou configuração) que permita ao cliente descartar intencionalmente alguns segmentos recebidos do servidor. Isso é crucial para testar o mecanismo de recuperação de dados. A interface deve informar quais segmentos (ex: por número de sequência) estão sendo descartados.
   
5. Recepção e Montagem:
    
    a- Receber os segmentos do arquivo enviados pelo servidor.
   
    b- Armazenar e ordenar os segmentos recebidos corretamente.
   
    c- Verificar a integridade de cada segmento (ex: usando checksum ou resumos criptográficos como o MD5 e SHA.).
   
6. Verificação e Finalização:
    
    a- Após receber todos os segmentos esperados (ou um sinal de fim de transmissão do servidor), verificar a integridade e completude do arquivo.
    
    b- Se o arquivo estiver OK: Salvar o arquivo reconstruído localmente e informar o sucesso ao usuário. Opcionalmente, apresentar/abrir o arquivo.
    
    c- Se o arquivo estiver com erro ou incompleto:
    
        I.   Identificar quais segmentos estão faltando ou corrompidos.
        II.  Solicitar a retransmissão desses segmentos específicos ao servidor, utilizando o protocolo definido.
        III. Repetir o processo de recepção e verificação até que o arquivo esteja completo e correto.
        IV.  Interpretação de Erros: Interpretar e exibir mensagens de erro recebidas do servidor (ex: “Arquivo não encontrado”).
    

## Considerações Obrigatórias para o Design do Protocolo:
O aluno deve projetar e justificar as escolhas para os seguintes aspectos do protocolo de aplicação sobre UDP:

1. Segmentação e Tamanho do Buffer:
   
    a- Como o arquivo será dividido? Qual o tamanho máximo de dados por datagrama UDP (payload)?
   
    b- Este tamanho deve ser fixo ou variável? Como ele se relaciona com o MTU (Maximum Transmission Unit) da rede? (Pesquisar sobre MTU e fragmentação IP).
   
    c- Os buffers de envio (servidor) e recepção (cliente) precisam ter tamanhos relacionados?
   
2. Detecção de Erros:
   
    a- Como a integridade dos dados em cada segmento será verificada?
   
    b- É necessário implementar um checksum?
   
    c- Qual algoritmo usar? (Ex: CRC32, soma simples).
   
3. Ordenação e Detecção de Perda:
   
    a- Como o cliente saberá a ordem correta dos segmentos? É necessário um número de sequência?
   
    b- Como o cliente detectará que um segmento foi perdido (e não apenas atrasado)?
   
4. Controle de Fluxo/Janela (Opcional Avançado):
   
    a- Considerar como evitar que o servidor envie dados mais rápido do que o cliente consegue processar (embora um controle de fluxo completo seja complexo e possa estar fora do escopo inicial).
   
5. Mensagens de Controle:
    
    a- Definir claramente os formatos das mensagens de: requisição de arquivo, envio de segmento de dados (incluindo cabeçalhos com número de sequência, checksum, etc.), confirmação de recebimento (se houver), solicitação de retransmissão e mensagens de erro.
