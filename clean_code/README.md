## TDD com Técnicas de programação e debbuging
***

**Teste**: processo de detectar o erro inicial

* Para rodar os testes execute: ```python3 -m pytest```

    - **pytest --maxfail=2**: Para a execução no segundo método que falhar
    - **pytest test_mod.py::TestClass::test_method**: Roda um método de teste dentro de uma classe de um arquivo
    - **pytest --pyargs directory**: Roda todos os testes dentro de um diretorio
    - **pytest --tb=line**: Somente uma linha por falha
    - **pytest -x --pdb**: Executa o debugger na primeira falha
    - **pytest.set_trace()**: No código de teste invoca o debbuger com o breakpoint nesse ponto onde foi inserido o código

***
#### Debbuging
***

Depuração é o processo de identificar a causa raiz de um erro e corrigi-lo

1. **Estabilizar a falha**: 

    - Simplificar ao máximo o caso de teste, eliminando fatores que não influencia na geração da falha

2. **Localizar a fonte da falha (defeito)**

    - Levantar as informações que produziram a falha

    - Analisar as informações e formular uma hipótese sobre o defeito

    - Determinar como confirmar ou invalidar a hipótese (através de teste ou inspeção do código)

    - Confirmar ou invalidar a hipótese

3. **Corrigir o defeito**

4. **Testar a correção**

5. **Procurar por erros similares**

***
#### Técnicas de programação importantes
***

Programação defensiva é o reconhecimento de que os programas terão problemas e serão modificados

Oferece um conjunto de técnicas para prevenir potenciais problemas de código e tem como objetivo produzir códigos resilientes que respondam adequadamente em situações inesperadas e que seja compreensivel e fácil de dar manutenção

* **Estilo e Desing**: Comentarios (linhas, paragrafos, funções e estruturas de controle), nomes de variáveis, métodos e classes significativas, folha de estilo ...

* **Priorizar a clareza ao inves da concisão**: Tornar o código um livro e sempre priorize a simplicidade do código

* **Não deixe os outros mexerem onde não devem**: Abuse de encapsulamentos privados ou publicos e etc...

* **Verifique todos os valores de retorno**: Os testes devem verificar todos os valores possíves de retorno, utilize uma amostragem pequena que engloba praticamente todos os casos

* **Manipule recursos**: Sempre que abrir um arquivo ou conexão ou etc... feche-o

* **Inicialize todas as variáveis ao declarar**: Todas as variáveis devem ser inicializadas

* **Declare as variáveis o mais tarde possível**: Sempre declare elas o mais perto possível de seu uso.

* **Use sempre recursos padrões da linguagem**: Não reinvente a roda, a menos que seja necessário

* **Use um sistema de logging**: Abuse dos logs/prints e etc...

* **Siga o idioma da linguagem**: Códifique em inglês sempre.

* **Verifique os limites númericos**: Faça um código defensivo que não quebre em um determinado limite númerico

* **Use constantes**: Acabe com os números mágicos

* **Decomposição em funções atômicas**: Sempre deixe as funções com o minimo de código possivel realizando apenas o que ela deve realizar.

* **Utilize paragrafos de função**: Dentro de uma função separe-a em paragrafos

* **Utilize tipagem**: Se a linguagem for de tipagem dinâmica tente arranjar um jeito de fazer o usuário usar somente o tipo desejado com código defensivo

* **Cabeçalhos e docstring**: Documente seu código

* **Tratamente de erros apropriados**: Trate os erros em nível apropriados usando exceptions

* **Assertivas**: use em partes do código em que o erro não pode ser permitido, tendo que fechar a aplicação caso ocorra.

* **Assuma o pior**: Sempre assuma que o pior pode acontecer no seu código e prepare-o para suportar esses eventos.

***
#### Code clean
***

* **Composição de método**: Os métodos devem ser simplificados chamando outros métodos dentro dele, cada qual fazendo algo especifico

* **Métodos explicativos**: Os métodos devem encapsula alguma operação dentro de outro método que seja não muito clara, normalmente são operações associadas a um comentario que explique ela

* **Métodos como condicionais**: Criar um método ou atributo que encapsula uma expressão booleana para obter condicionais mais claros

* **Evitar estruturas encadeadas**: Para cada estrutura de controle (if, switch, laços) crie um método para simplificar e não deixar elas encadeadas

* **Cláusulas guarda**: Criar um **return if condicao(): ...** para que não precise criar um else sem nada

* **Objeto Método**: Criar uma classe que encapsula uma operação complexa simplificando a original (cliente), basicamente toda a implementação ficará nessa classe nova e a classe que o cliente irá usar só tem os métodos necessários para o cliente saber, o padrão de projeto adapter faz isso.

* **Evite flags como argumentos**: Para casos que tenha que passar flags de comparação como argumento para usar no if crie uma função para cada condição do if e retorne o resultado

* **Objeto como parâmetro**: Quando tiver passando vários argumentos passados para o construtor de uma classe, verifique se esses argumentos podem ser transformados em variáveis de instancia de outra classe para ser usado nela.

* **Parâmetros como variáveis de instáncia**: Localizar parâmetros muito utilizados pelos métodos de uma classe e transformá-lo em variável de instância  da propria classe (self.variavel).

* **Maximizar coesão**: Quebrar uma classe que não segue principios da responsabilidade única.

* **Delegação de tarefa**: Transferir um método que utiliza dados de uma classe B para a classe B, se o método da classe A usa muitos dados da classe B, então provavelmente ele deve ser um método da classe B e não da A.

* **Objeto centralizador**: Criar uma classe que encapsula uma operação com alta dependencia entre classes, será um intermediario que fará a relação entre duas classes para diminuir o acoplamento de ambas, essa classe deve centralizar a comunicação dos objetos

***
#### SOLID
***

* **Single responsability principle**: Cada classe/metodo devem ter responsabilidades únicas

* **Open-closed principle**: Uma classe deve ser aberta a extensão (herança) e fechadas a modificações

* **Liskov substitution principle**: O cliente deve usar o serviço da classe abstrata (geral) sem saber que ta usando um serviço especifico concreto

* **Interface segregation principle**: Uma interface não deve obrigar quem a implementar a implementar métodos que não agrega valor a ela

* **Dependency Inversion Principle**: Uma classe deve depender de classes abstratas/interface e não de suas classes concretas que ta a implementação

***
#### GRASP
***

* **Alta coesão**: É fator de qualidade de projeto e representa que cada classe tem sua respectiva responsabilidade bem definida

* **Baixo acoplamento**: é fator de qualidade em um projeto que busca a medida de interdependência entre modulos, modulos com baixo acoplamento são mais independentes

* **Controller**: Controladora de fachada na qual controla vários sub-sistemas, ou pode ter várias controladoras, uma para cada caso de uso e etc...

* **Polimorfismo**: Crie uma classe abstrata e utilize o poder do polimorfismo para gerar códigos mais limpos

* **Invenção pura**: Criar uma classe específica para lidar com alguma preocupação, tornando a modelagem mais coesa, deixando cada classe com responsabilidades únicas

* **Indireção**: Criar classes que intermediar a comunicação entre duas classes caso elas estejam muito dependentes uma da outra, diminuindo o acoplamento entre elas, é uma invenção pura.

* **Variação protegida**: É a combinação do uso de Polimorfismo, indireção e invenção, escopo protegido com atributos privados e acesso controlado a mecanismos de autenticação e autorização, 

* **Criador**: É quem tem a responsabilidade de criar uma nova instância de uma classe

* **Especialista**: É a classe que tem a informação necessária para satisfazer a responsabilidade, ele atribui a responsabilidade ao especialista
