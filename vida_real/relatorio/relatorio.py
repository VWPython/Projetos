"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em
disco no seu servidor de arquivos. Para tentar resolver este problema, o
Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado. Através de um programa,
baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado
"usuarios.txt":

    alexandre       456123789
    anderson        1245698456
    antonio         123456456
    carlos          91257581
    cesar           987458
    rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo,
você deve criar um programa que gere um relatório, chamado "relatório.txt", no
seguinte formato:

    ACME Inc.               Uso do espaço em disco pelos usuários
    ------------------------------------------------------------------------
    Nr.  Usuário        Espaço utilizado     % do uso

    1    alexandre       434,99 MB             16,85%
    2    anderson       1187,99 MB             46,02%
    3    antonio         117,73 MB              4,56%
    4    carlos           87,03 MB              3,37%
    5    cesar             0,94 MB              0,04%
    6    rosemary        752,88 MB             29,16%

    Espaço total ocupado: 2581,58 MB
    Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em
memória, caso sejam necessários, de forma a agilizar a execução do programa.
A conversão de espaço ocupado em disco, de bytes para megabytes deverá ser feita
através de uma função separada, que será chamada pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através de uma função,
que será chamada pelo programa principal.
"""


def main():
    BLANK_LINE = ''
    MEMORY = 1

    user_file = open('usuarios.txt', 'r')
    line = user_file.readline()

    total_memory = 0
    users = []

    while line != BLANK_LINE:
        line_separator = line.split()
        __remove_white_space(line_separator)

        total_memory += int(line_separator[MEMORY])

        users.append(line_separator)

        line = user_file.readline()

    user_file.close()

    total_memory /= (1024**2)

    generate_report(users, total_memory)


def __remove_white_space(splitter):
    # Removes all whitespaces that are present in the list of strings present in the file line

    while splitter.count('') != 0:
        splitter.remove('')


def generate_report(users, total_memory):
    """
    Generates the report with the users the amount of space used on disk in MB and the percentage of use of that space

    Parameters:

        @param users: List of users
        @type users: List<String>

        @param total_memory: Amount of space used on disk
        @type total_memory: Integer

    Return:

        Write the report in report file

    Example Input:

        alexandre       456123789
        anderson        1245698456
        antonio         123456456
        carlos          91257581
        cesar           987458
        rosemary        789456125

    Example Output:

        ACME Inc.               Uso do espaço em disco pelos usuários
        ------------------------------------------------------------------------
        Nr.  Usuário        Espaço utilizado     % do uso

        1    alexandre       434,99 MB             16,85%
        2    anderson       1187,99 MB             46,02%
        3    antonio         117,73 MB              4,56%
        4    carlos           87,03 MB              3,37%
        5    cesar             0,94 MB              0,04%
        6    rosemary        752,88 MB             29,16%

        Espaço total ocupado: 2581,58 MB
        Espaço médio ocupado: 430,26 MB

    """

    report = open('relatorio.txt', 'w')

    __calculate_used_memory(users)

    percentage = __calculate_percentage_memory(users, total_memory)

    __write_header(report)

    bigger = __get_the_biggest_memory(users)

    report.write('\n')

    user_list = range(len(users))

    for index in user_list:
        __report_formatting(index, users, percentage, bigger, report)

    report.write('\n')
    report.write('Espaço total ocupado: %.2f MB' % total_memory)
    report.write('\n')
    report.write('Espaço médio ocupado: %.2f MB' % (total_memory/len(users)))
    report.write('\n')
    report.close()


def __calculate_used_memory(users):
    # Calculates the memory space that the user occupies

    MEMORY = 1
    MB = (1024**2)

    for user_index in range(len(users)):
        users[user_index][MEMORY] = float(users[user_index][MEMORY])/MB


def __calculate_percentage_memory(users, total_memory):
    # Calculates the percentage of memory used by user

    percentage = []
    MEMORY = 1
    PERCENT = 100

    for user in users:
        user_memory = PERCENT*user[MEMORY]
        percentage.append(user_memory/total_memory)

    return percentage


def __write_header(report):
    # Write the header of report on report file

    report.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
    report.write(72*'-' + '\n')
    report.write('Nr.  Usuário        Espaço utilizado     % do uso\n')


def __get_the_biggest_memory(users):
    # get the size of the biggest memory string

    the_biggest_memory_string = 0
    MEMORY = 1

    for user in users:
        size_of_memory_string = len("%.2f" % user[MEMORY])

        if size_of_memory_string > the_biggest_memory_string:
            the_biggest_memory_string = size_of_memory_string

    return the_biggest_memory_string


def __report_formatting(index, users, percentage, bigger, report):
    # Format data of report like this: 1    alexandre       434,99 MB             16,85%

    WHITE_SPACE = ' '
    USER = 0
    MEMORY = 1

    # 1...
    line = '%i' % (index + 1)
    # 1    ...
    line += (5 - len(line)) * WHITE_SPACE

    # 1    alexandre       ...
    line += users[index][USER] + (15 - len(users[index][USER])) * WHITE_SPACE

    # 1    alexandre       434,99 MB...
    number = "%.2f" % users[index][MEMORY]
    initial_space = (bigger - len(number)) * WHITE_SPACE
    number += ' MB'

    # 1    alexandre       434,99 MB             ...
    final_space = (23 - len(initial_space) - len(number)) * WHITE_SPACE
    line += initial_space + number + final_space

    # 1    alexandre       434,99 MB             16,85%
    memory_percentage = "%.2f" % percentage[index]
    initial_space = (5 - len(memory_percentage)) * WHITE_SPACE
    line += initial_space + memory_percentage + "%"

    report.writelines(line + '\n')


if __name__ == '__main__':
    main()
