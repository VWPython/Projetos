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

2. Localizar a fonte da falha (defeito)

  - Levantar as informações que produziram a falha

  - Analisar as informações e formular uma hipótese sobre o defeito

  - Determinar como confirmar ou invalidar a hipótese (através de teste ou inspeção do código)

  - Confirmar ou invalidar a hipótese

3. Corrigir o defeito

4. Testar a correção

5. Procurar por erros similares

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
