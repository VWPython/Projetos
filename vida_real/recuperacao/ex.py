"""
Rapaz eu to ferrado!

Isso aconteceu comigo de verdade! Meu computador possui um HD que eu particionei em 4
--> Uma partição de 100GB para o Ubuntu
--> Uma partição de 100GB para o Windows 7
--> Uma partição de 100GB para o OS X Mavericks
--> Uma partição de 600GB NTFS chamada 'HD' para ser acessado por qualquer um dos 3 sistemas anteriors

Só que, um belo dia, minha partição 'HD' endoidou e alguns arquivos foram excluídos do nada
Esses arquivos eram principalmente as aulas do canal

Só que meus arquivos não foram perdidos! Por alguma magia eles foram colocadas numa pasta
de nome found.000 que colocou outras pastas dentro delas

As pastas foram renomeadas com nomes totalmente estranhos, entretanto dentro delas
eu consegui encontrar arquivos familiares, de formato mp4, mp3, txt e kdenlive

Ufa! Eram justamente os meus arquivos das aulas do canal! Só que eles estavam
extremamentes bagunçados e com uns nomes bem estranhos! Mas eu sabia que podia arrumar

Infelizmente (ou felizmente) eu já gravei muitas aulas o que faz com que não seja possível
arrumar todos os arquivos na mão, então eu pensei "po, vo escreve um programa"

Nesta pasta você verá que existe a tal pasta found.000 e dentro dela há um resumo da
bagunça que aconteceu na minha partição. Eu excluí os arquivos mp4 e mp3, pois seriam
muito pesados para colocar no dropbox

Dentro das pastas você verá que todas contem um arquivo chamado Descrição.txt, esse
arquivo segue sempre o mesmo padrão para qualquer aula que eu faça

A partir do padrão contido no meu arquivo Descrição.txt escreva um programa que recupere
os arquivos contidos no found.000 e passe-os para uma pasta "recuperados" e depois exclua
a pasta "found.000" e todo o seu conteúdo

Dentro desta pasta recuperados organize as aulas em diretórios de maneira adequada, sendo
o nome da aula o nome contido no arquivo de Descrição

Use o os.walk para percorrer os diretórios em found.000, os.chdir para ficar mudando
de diretório, os.mkdir para fazer os diretórios de recuperação, os.system para executar
comandos como copy e os.rmdir para remover diretórios (só vazios)

Como desafio implemente o arquivo de recuperação de forma que o arquivo Descrição.txt sirva
de entrada para um outro script que obtenha todos os dados necessários para fazer a recuperação
dos arquivos no diretório
"""
