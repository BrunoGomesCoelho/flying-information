# Como você organizaria a arquitetura da aplicação/dados?
Sub-dividir o sistema em diversos layers menores, idealmente o mais independentes um dos outros,
	ou seja, provavelmente seguindo a ideia de arquitetura de microserviços.
Por exemplo:
Dividir a parte relacionada ao armazenamento de dados num layer de banco de dados em si;
Outro layer relacionado ao scraping/crawling em sí;
Conforme necessário, outro layer relacionado à estruturação dos dados/inteligencia artificial.
Outro layer para o frontend/a aplicação.
Idealmente os diferentes serviços se comunicam de uma forma bem modularizada usando APIs e todo serviço tem uma definição bem clara de escopo, além de cada um ser individualmente "deployable".


# O que deixaria automatizado/agendado?
Um script periódico para checar novos produtos no site, e se sim atualizar a base;
Se necessário, outro script relacionado a pegar mudanças na estrutura dos dados/páginas antes de isso quebrar o scraping.

# O que monitorar pra acompanhar a saúde/qualidade da aplicação?
Quantidade de dados capturados por frequência de uso do scraper; Alguns checks básicos sobre a qualidade desses dados;
A constante aquisição/apresentação de dados do banco de dados; A qualidade desses dados como não duplicação.
O acesso continuo a esses dados

# Na sua opinião, quais são os principais riscos que podem causar erros na execução desse script?
Mudanças na estrutura de alguma das páginas devido a sua aquisição estástica/hard coded.
Possibilidade de mudanças no próprio armazenamento de uma loja/empresa.
Mudança de tipos de dados/conteúdo nulos que podem dificultar a vida do modelo de aprendizado.

