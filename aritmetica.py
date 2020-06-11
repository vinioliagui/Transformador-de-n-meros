# FUNCAO QUE CONVERTE INDIVIDUALMENTE P/ OCTA,HEXA E BIN #
def convert_func_decimal2(num_entry, option):
    numconvertido = []
    new_option = (((2 ** option) + (2 ** option)) // 2) * option
    while True:
        if (new_option > 10):
            if ((int(num_entry) // 16) == 0):
                numconvertido.append(str(num_entry))
                break

            else:
                numconvertido.append(str(int(num_entry) % 16))
                num_entry = (int(num_entry) // 16)

        else:
            if ((int(num_entry) // new_option) == 0):
                numconvertido.append(str(num_entry))
                break

            else:
                numconvertido.append(str(int(num_entry) % new_option))
                num_entry = (int(num_entry) // new_option)

    substituir = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    for indexelement, varandom in enumerate(numconvertido):
        if int(varandom) in substituir:
            numconvertido[indexelement] = substituir[int(varandom)]

        else:
            pass

    numconvertido.reverse()
    return ''.join(numconvertido)


# ------------------------------------------------------ #

#      CONVERSORES DECIMAL PARA OCTAL, HEXA E BINARIO    # 
def binario(numdecim, opcao):  #
    return convert_func_decimal2(numdecim, opcao)  #
    #


def octal(numdecim, opcao):  #
    return convert_func_decimal2(numdecim, opcao)  #
    #


def hexadecimal(numdecim, opcao):  #
    return convert_func_decimal2(numdecim, opcao)  #


##########################################################


#      FUNCAO QUE CONVERTE INDIVIDUALMENTE P/ DECIMAL    #
def convert_func_decimal(num_entry, option):
    numqualquer_lista = [varandom.capitalize() for varandom in str(num_entry)]
    numqualquer_lista.reverse()
    new_option = (((2 ** option) + (2 ** option)) // 2) * option
    numdecimal = 0
    substituir = {"A": '10', "B": '11', "C": '12', "D": '13', "E": '14', "F": '15'}
    for index_count, varandom2 in enumerate(numqualquer_lista):
        if (varandom2 == '0'):
            pass

        else:
            if (new_option > 10):
                if (varandom2 in substituir):
                    varandom3 = varandom2.replace(varandom2, substituir[varandom2])
                    numdecimal += int(varandom3) * (16 ** index_count)

                else:
                    numdecimal += int(varandom2) * (16 ** index_count)

            else:
                numdecimal += int(varandom2) * (new_option ** index_count)

    return numdecimal


# ------------------------------------------------------ #

#    CONVERSORES DE HEXA, OCTAL E BINARIO PARA DECIMAL   #
def decimal(numqualquer, opcao):  #
    if (opcao == 1):  #
        return convert_func_decimal(numqualquer, opcao)  #
        #
    elif (opcao == 2):  #
        return convert_func_decimal(numqualquer, opcao)  #
        #
    elif (opcao == 3):  #
        return convert_func_decimal(numqualquer, opcao)  #


##########################################################

#       FUNCAO QUE CONVERTE DE KMG...Bit<=>KMG...Bit     #
def bytebit(numqualquer, opcao):
    if (opcao == 1):
        return ("\nBit: " + str(int(numqualquer) * 8), "KiB: " + str(int(numqualquer) / 1024),
                "MiB: " + str(int(numqualquer) / (1024 ** 2)), "GiB: " + str(int(numqualquer) / (1024 ** 3)),
                "TiB: " + str(int(numqualquer) / (1024 ** 4)), "PiB: " + str(int(numqualquer) / (1024 ** 5)),
                "EiB: " + str(int(numqualquer) / (1024 ** 6)))

    elif (opcao == 2):
        return ("\nByte: " + str(int(numqualquer) / 8), "KiB: " + str(int(numqualquer) / (8 * 1024)),
                "MiB: " + str(int(numqualquer) / (8 * 1024 ** 2)), "GiB: " + str(int(numqualquer) / (8 * 1024 ** 3)),
                "TiB: " + str(int(numqualquer) / (8 * 1024 ** 4)), "PiB: " + str(int(numqualquer) / (8 * 1024 ** 5)),
                "EiB: " + str(int(numqualquer) / (8 * 1024 ** 6)))

    elif (opcao == 3):
        return ("\nBit: " + str(int(numqualquer) * (8 * 1024)), "Byte: " + str(int(numqualquer) * (1024)),
                "MiB: " + str(int(numqualquer) / (1024)), "GiB: " + str(int(numqualquer) / (1024 ** 2)),
                "TiB: " + str(int(numqualquer) / (1024 ** 3)), "PiB: " + str(int(numqualquer) / (1024 ** 4)),
                "EiB: " + str(int(numqualquer) / (1024 ** 5)))

    elif (opcao == 4):
        return ("\nBit: " + str(int(numqualquer) * (8 * 1024 ** 2)), "Byte: " + str(int(numqualquer) * (1024 ** 2)),
                "KiB: " + str(int(numqualquer) * (1024)), "GiB: " + str(int(numqualquer) / (1024)),
                "TiB: " + str(int(numqualquer) / (1024 ** 2)), "PiB: " + str(int(numqualquer) / (1024 ** 3)),
                "EiB: " + str(int(numqualquer) / (1024 ** 4)))

    elif (opcao == 5):
        return ("\nBit: " + str(int(numqualquer) * (8 * 1024 ** 3)), "Byte: " + str(int(numqualquer) * (1024 ** 3)),
                "KiB: " + str(int(numqualquer) * (1024 ** 2)), "MiB: " + str(int(numqualquer) * (1024)),
                "TiB: " + str(int(numqualquer) / (1024)), "PiB: " + str(int(numqualquer) / (1024 ** 2)),
                "EiB: " + str(int(numqualquer) / (1024 ** 3)))

    elif (opcao == 6):
        return ("\nBit: " + str(int(numqualquer) * (8 * 1024 ** 4)), "Byte: " + str(int(numqualquer) * (1024 ** 4)),
                "KiB: " + str(int(numqualquer) * (1024 ** 3)), "MiB: " + str(int(numqualquer) * (1024 ** 2)),
                "GiB: " + str(int(numqualquer) * (1024)), "PiB: " + str(int(numqualquer) / (1024)),
                "EiB: " + str(int(numqualquer) / (1024 ** 2)))

    elif (opcao == 7):
        return ("\nBit: " + str(int(numqualquer) * (8 * 1024 ** 5)), "Byte: " + str(int(numqualquer) * (1024 ** 5)),
                "KiB: " + str(int(numqualquer) * (1024 ** 4)), "MiB: " + str(int(numqualquer) * (1024 ** 3)),
                "GiB: " + str(int(numqualquer) * (1024 ** 2)), "TiB: " + str(int(numqualquer) * (1024)),
                "EiB: " + str(int(numqualquer) / (1024)))

    elif (opcao == 8):
        return ("\nBit: " + str(int(numqualquer) * (8 * 1024 ** 6)), "Byte: " + str(int(numqualquer) * (1024 ** 6)),
                "KiB: " + str(int(numqualquer) * (1024 ** 5)), "MiB: " + str(int(numqualquer) * (1024 ** 4)),
                "GiB: " + str(int(numqualquer) * (1024 ** 3)), "TiB: " + str(int(numqualquer) * (1024 ** 2)),
                "PiB: " + str(int(numqualquer) * (1024)))


# ------------------------------------------------------ #

def encurta_linha(numdigitado, un_medida):
    conversao = (bytebit(numdigitado, 1 + un_medida))
    varhold = ""
    for varandom in conversao:
        varhold += varandom + "\n"

    return varhold


##########################################################

flag = True  # repeticao das perguntas

while (flag == True):