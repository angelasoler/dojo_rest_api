# Dojo rest api
Feat Marcelo e Jhonatan

## Sobre o que a gente estava falhando:
- No lado da api apenas estavamos retornando a frase e no lado html estavamos esperando um objeto *JSON* com propriedade *message*
- No lado do html, estavamos passando o end-point na raiz "/", porem no lado da API estavamos passando o endpoint "/conselhos"
- Estava faltando configurar o CORS para ter as permissões
- tambem já deixe um lupinho mais bonito que pega as frases do arquivo, em dez de manualmente como estavamos fazendo :P

## Sobre configuração de CORS:

> O CORS (Cross-Origin Resource Sharing) é uma política de segurança implementada pelos navegadores da web para controlar as solicitações feitas por scripts em uma página da web para recursos de outro domínio.
> 
>Quando você está executando um aplicativo da web em um domínio (por exemplo, http://localhost:2700) e faz uma solicitação para um servidor em um domínio diferente (por exemplo, http://localhost:8080), o navegador impõe as regras do CORS para garantir a segurança e evitar ataques de origem cruzada.
>
>Por padrão, o navegador impede solicitações de recursos de outro domínio (origem) que não tenham permissão explícita para acessá-los. Isso significa que, se você fizer uma solicitação AJAX de uma página em um domínio para um servidor em um domínio diferente, o navegador bloqueará a solicitação.
>
>Para permitir solicitações entre diferentes domínios, você precisa configurar o CORS no servidor para informar ao navegador quais origens têm permissão para acessar os recursos do servidor. Essa configuração é feita usando cabeçalhos HTTP especiais, como o cabeçalho "Access-Control-Allow-Origin".
>
>No seu código, você está usando o FastAPI para criar a API e o Starlette para adicionar o middleware CORS. A configuração que você adicionou com o CORSMiddleware especifica que todas as origens (allow_origins=["*"]) têm permissão para acessar os recursos da sua API. Isso é útil durante o desenvolvimento, mas em um ambiente de produção, é recomendado restringir as origens permitidas apenas aos domínios específicos que você deseja permitir.
>
>Em resumo, a configuração do CORS é necessária para permitir que o navegador faça solicitações de recursos em domínios diferentes. Sem essa configuração, o navegador bloquearia essas solicitações por motivos de segurança.
>
> *Source chatgpt*
