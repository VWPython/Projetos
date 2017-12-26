from datetime import timedelta


class Conversor(object):
    """
    Classe que trata de conversões de tipos.
    """

    COMPRIMENTO = 1
    VELOCIDADE = 2
    TEMPERATURA = 3
    PESO = 4
    AREA = 5
    VOLUME = 6
    TEMPO = 7

    def __init__(self, operacao):
        """
        Construtor do conversos para especificar as operações.
        """

        if operacao == self.COMPRIMENTO:
            self.metrica = Comprimento()

        elif operacao == self.VELOCIDADE:
            self.metrica = Velocidade()

        elif operacao == self.TEMPERATURA:
            self.metrica = Temperatura()

        elif operacao == self.PESO:
            self.metrica = Peso()

        elif operacao == self.TEMPO:
            self.metrica = Tempo()

        # elif operacao == self.AREA:
        #     self.metrica = Area()
        # m^2, km^2, cm^2

        # elif operacao == self.VOLUME:
        #     self.metrica = Volume()
        # m^3, km^3, cm^3, L, ML

        else:
            raise NameError("Operação Invalida!")

    def converter(self, valor=None, tipo=None, destino=None):
        """
        Converter resultados.
        """

        return self.metrica.converter(valor, tipo, destino)


class Comprimento(object):
    """
    Métrica de comprimento (CM, M, KM) para conversão.
    """

    CM = 1
    M = 2
    KM = 3

    def converter(self, valor, tipo, destino):
        """
        Converter resultados.
        """

        if tipo == self.CM:
            valor = self.cm_para(valor, destino)
        elif tipo == self.M:
            valor = self.m_para(valor, destino)
        elif tipo == self.KM:
            valor = self.km_para(valor, destino)
        else:
            raise NameError("Argumentos invalidos")

        return valor

    def cm_para(self, valor, destino):
        """
        Converte centimetros para kilometros ou metros.
        """

        if destino == self.M:
            valor /= 1000
        elif destino == self.KM:
            valor /= 1000000
        elif destino == self.CM:
            return valor
        else:
            raise NameError("Argumentos invalidos")

        return valor

    def km_para(self, valor, destino):
        """
        Converte kilometros para metros ou centimetros
        """

        if destino == self.M:
            valor *= 1000
        elif destino == self.CM:
            valor *= 1000000
        elif destino == self.KM:
            return valor
        else:
            raise NameError("Argumentos invalidos")

        return valor

    def m_para(self, valor, destino):
        """
        Converte metros para centimetros ou kilometros
        """

        if destino == self.KM:
            valor /= 1000
        elif destino == self.CM:
            valor *= 1000
        elif destino == self.M:
            return valor
        else:
            raise NameError("Argumentos invalidos")

        return valor


class Velocidade(object):
    """
    Métrica de velocidade (KMH, MS) para conversão.
    """

    KMH = 1  # km/h
    MS = 2   # m/s

    def converter(self, valor, tipo, destino=None):
        """
        Converter resultados de km/h para m/s caso o tipo for MS ou
        m/s para km/h caso o tipo for KMS.
        """

        if tipo == self.KMH:
            valor *= 3.6
        elif tipo == self.MS:
            valor /= 3.6
        else:
            raise NameError("Argumentos invalidos")

        return valor


class Temperatura(object):
    """
    Métrica de temperatura (C, F, K) para conversão.
    """

    C = 1
    F = 2
    K = 3

    def converter(self, valor, tipo, destino):
        """
        Converter resultados entre graus Celsius, Fahrenheit e Kelvin
        """

        if tipo == self.C:
            valor = self.celsius_para(valor, destino)
        elif tipo == self.F:
            valor = self.fahrenheit_para(valor, destino)
        elif tipo == self.K:
            valor = self.kelvin_para(valor, destino)
        else:
            raise NameError("Argumentos invalidos")

        return valor

    def celsius_para(self, valor, destino):
        """
        Converte graus Celsius para Fahrenheit ou Kelvin.
        """

        C = valor

        if destino == self.F:
            F = C*1.8 + 32
            valor = F
        elif destino == self.K:
            K = C + 273.15
            valor = K
        else:
            raise NameError("Argumentos invalidos")

        return valor

    def fahrenheit_para(self, valor, destino):
        """
        Converte graus Fahrenheit para Celsius ou Kelvin.
        """

        F = valor

        C = (F - 32)/1.8

        if destino == self.C:
            valor = C
        elif destino == self.K:
            K = C + 273.15
            valor = K
        else:
            raise NameError("Argumentos invalidos")

        return valor

    def kelvin_para(self, valor, destino):
        """
        Converter graus Kelvin para Celsius ou Fahrenheit.
        """

        K = valor

        C = K - 273.15

        if destino == self.C:
            valor = C
        elif destino == self.F:
            F = C*1.8 + 32
            valor = F
        else:
            raise NameError("Argumentos invalidos")

        return valor


class Peso(object):
    """
    Métrica de peso (KG, G) para conversão.
    """

    KG = 1  # Kilogramas
    G = 2   # Gramas

    def converter(self, valor, tipo, destino=None):
        """
        Converter resultados de KG para G caso o tipo for G ou
        G para KG caso o tipo for KG.
        """

        if tipo == self.KG:
            valor /= 1000
        elif tipo == self.G:
            valor *= 1000
        else:
            raise NameError("Argumentos invalidos")

        return valor


class Tempo(object):
    """
    Métrica de tempo (SS, MM, HH, DIA, MES, ANO) para conversão.
    """

    SS = 1   # Segundos
    MM = 2   # Minutos
    HH = 3   # Horas
    DD = 4  # Dias

    def converter(self, valor, tipo, destino):
        """
        Converte resultados entre segundos, horas, minutos, dias, meses e anos
        """

        segundos = self.converte_para_segundos(tipo, valor)
        valor = self.segundos_para(segundos, destino)

        return valor

    def converte_para_segundos(self, tipo, valor):
        """
        Converte dias, minutos e horas para segundos.
        """

        if tipo == self.SS:
            return timedelta(seconds=valor).total_seconds()
        elif tipo == self.MM:
            return timedelta(minutes=valor).total_seconds()
        elif tipo == self.HH:
            return timedelta(hours=valor).total_seconds()
        elif tipo == self.DD:
            return timedelta(days=valor).total_seconds()
        else:
            raise NameError("Argumentos invalidos")

    def segundos_para(self, valor, destino):
        """
        Converte resultado de segundos para minutos, horas, ou dias.
        """

        minutos, segundos = divmod(valor, 60)
        horas, minutos = divmod(minutos, 60)
        dias, horas = divmod(horas, 24)

        resultado = {
            'SS': segundos,
            'MM': minutos,
            'HH': horas,
            'DD': dias
        }

        return resultado
