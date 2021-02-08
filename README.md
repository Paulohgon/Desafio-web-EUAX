# Desafio Web Developer
Resolução do desafio da empresa EUAX

## Problema
Você precisa criar um cadastro de projetos com a data de início e data final para a entrega, esse projeto pode ter 1 ou N atividades que também precisam ser cadastradas com as datas de início e data de fim. Após ter feito todos os cadastros precisamos saber quantos % dos projetos já temos finalizados e também se o projeto terá atrasos ou não. Para saber a % de andamento do projeto deve ser considerado o número de atividades finalizadas e quantidade de atividades ainda sem finalizar. Para saber se o projeto terá atraso considere a maior data final das atividades e compare com a data final do projeto, se for maior que a data final, o projeto terminará com atrasos.
##  Tecnologias ulitizadas
- Python3
- SQL

## Funcionamento 
Ao executar o código, uma tabela no banco de dados será criado, caso ainda não exista, então o usuário será levado a um menu onde poderá escolher se quer inserir um novo projeto, verificar o status de algum projeto, deletar algum projeto ou simplismente parar a execução,após a escolha da primeira opção será pedido para que ele insira os dados do projeto e logo depois os dados das atividades do mesmo, essas serão atreladas pelo id no banco de dados.Caso escolha a segunda opção(verificar o status) será pedido que ele entre com o id do projeto e para isso será lhe mostrado todos os projetos cadastrados, então depois de escolhido o programa dara todas as informações cadastradas do projeto e das atividades e informará a porcentagem que ele está completo. Se for escolhido a opção de deletar algum projeto, será pedido ao usuário que informe o id do projeto que deseja ser deletado e então será deletado o projeto e todas as atividades relacionadas a ele. Por fim, se escolhido a opção de parar a execução o programa para sem fazer nada. Ao fim de qualquer uma das três primeiras escolhas o usuário será levado ao meno inicial novamente.

## Experiência de desenvolver
Assim que recebido o desafio, percebi que me faltava boa parte das habilidades requiridas, não sabia como trabalhar com SQL e banco de dados, nem sabia por onde começar e o que usar, então depois de alguns dias de pesquisa e estudo consegui fazer o código que fora entregue, porém, infelizmente, fugiu das minhas habilidades confeccionar uma interface gráfica com as tecnologias usadas ou aprender do zero uma nova tecnologia que poderia me proporcionar tal ferramenta, também tive dificuldades de implementar o cálculo que verifica se o projeto esta atrasado, então com a filosofia de dar o meu melhor implementei tudo que estava ao meu alcance com o conhecimento adquirido e sinto que me superei bastante nesses dias de desenvolvimento, além disso, agora sei onde estão minhas falhas como desenvolvedor procurarei corrigi-las.

## Requisitos
- [x] Back-end
- [ ] Front-end e interface gráfica

- [x] ID Projeto
- [x] Nome Projeto
- [x] Anotar data Início
- [x] Anotar Data Fim
- [x] % Completo
- [ ] Atrasado

- [x] ID Atividade
- [x] ID Projeto
- [x] Nome Atividade
- [x] Anotar data Início
- [x] Anotar Data Fim
- [x] Finalizada
