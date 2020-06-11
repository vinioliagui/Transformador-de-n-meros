from number_conversion_and_arithmetic import binario, decimal


def represent_semsinal(numero, num_de_bits):
    convert_bin = binario(numero, 1)
    if (len(convert_bin) > num_de_bits):
        retorna = 'Overflow! ' + convert_bin[len(convert_bin) - num_de_bits:]
        return retorna

    else:
        retorna = '0' * (num_de_bits - len(convert_bin)) + convert_bin
        return retorna


def represent_comsinal(numero, num_de_bits):
    if '-' in numero:
        convert_bin = binario(numero[1:], 1)
        convert_bin_new = '1' + convert_bin
        if (len(convert_bin_new) > num_de_bits):
            retorna = 'Overflow! ' + convert_bin_new[(len(convert_bin_new) - num_de_bits):]
            return retorna

        else:
            retorna = ('1' + ('0' * ((num_de_bits - len(convert_bin)) - 1)) + convert_bin)
            return retorna

    else:
        convert_bin2 = binario(numero, 1)
        convert_bin_new2 = '0' + convert_bin2
        if (len(convert_bin_new2) > num_de_bits):
            retorna = 'Overflow! ' + convert_bin_new2[len(convert_bin_new2) - num_de_bits:]
            return retorna

        else:
            retorna = ('0' * (num_de_bits - len(convert_bin2))) + convert_bin2
            return retorna


def complemento_dois(numero, num_de_bits):
    if '-' in numero:
        convert_bin = represent_semsinal(numero[1:], num_de_bits)
        convert_bin2 = [random for random in convert_bin]
        convert_bin2.reverse()
        flag = 0
        convert_bin_menor_num_bit = represent_comsinal(numero, num_de_bits)
        for index_count, varandom in enumerate(convert_bin2):
            if (varandom == '1' and flag == 0):
                flag = 1
            elif (varandom == '0' and flag == 0):
                pass

            else:
                convert_bin2[index_count] = '0' if (varandom == '1') else '1'

        convert_bin2.reverse()
        retorna = ''.join(convert_bin2) if (num_de_bits > len(numero)) else convert_bin_menor_num_bit
        return retorna

    else:
        return represent_semsinal(numero, num_de_bits)


def ops_arit_comple_2(numero, numero2):
    if '1' in (numero[0] or numero2[0]):
        num = (decimal(numero[1:], 1), numero) if '1' in numero else (decimal(numero2[1:], 1), numero2)
        da_para_represent = (2 ** len(numero) - 1) // 2
        if num[1][-1] != 2:
            soma = num[0] * -1 + decimal(numero2, 1)
            if ((soma <= da_para_represent) and (soma == da_para_represent)):
                return 'Overflow!' + str(soma)

            else:
                return soma

        else:
            soma = num[0] * -1 + decimal(numero, 1)
            return soma

    else:
        da_para_represent = (2 ** len(numero) - 1) // 2
        soma = decimal(numero, 1) + decimal(numero2, 1)
        if (soma > da_para_represent):
            return 'Overflow! ' + str(soma)

        else:
            return complemento_dois(str(soma), len(numero))
