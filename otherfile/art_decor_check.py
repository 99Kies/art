# -*- coding: utf-8 -*-
"""Art and decors duplication and UTF-8 compatibility testing script."""
import sys
import art
from art.art_param import DECORATIONS_MAP as Decor_Dict
from art.art_dic import art_dic as Art_Dict

Failed1 = 0
Failed2 = 0
Failed3 = 0
Failed4 = 0
Message1 = "Art UTF-8 compatibility test "
Message2 = "Art duplication test "
Message3 = "Decor UTF-8 compatibility test "
Message4 = "Decor duplication test "


def is_utf8(s):
    """
    Check input string for UTF-8 compatibility.

    :param s: input string
    :type s: str
    :return: result as bool
    """
    try:
        if sys.version_info.major == 3:
            _ = bytes(s, 'utf-8').decode('utf-8', 'strict')
        else:
            return True
        return True
    except Exception:
        return False


def print_result(flag_list, message_list):
    """
    Print final result.

    :param flag_list: list of test flags
    :type flag_list: list
    :param message_list: list of test messages
    :type message_list: list
    :return: None
    """
    print("art version : {}\n".format(art.__version__))
    for index, flag in enumerate(flag_list):
        if flag == 0:
            print(message_list[index] + "passed!")
        else:
            print(message_list[index] + "failed!")


if __name__ == "__main__":
    Art_Keys = list(Art_Dict.keys())
    Art_Values = list(Art_Dict.values())
    for art_name in Art_Keys:
        if not is_utf8(Art_Dict[art_name]):
            Failed1 += 1
            print("UTF-8 compatibility error in art : " + art_name)
        if Art_Values.count(Art_Dict[art_name]) > 1:
            Failed2 += 1
            print("Art duplication error : " + art_name)

    Decor_Keys = list(Decor_Dict.keys())
    Decor_Values = list(Decor_Dict.values())
    for decor_name in Decor_Keys:
        if not is_utf8(
                Decor_Dict[decor_name][0]) or not is_utf8(
                Decor_Dict[decor_name][1]):
            Failed3 += 1
            print("UTF-8 compatibility error in decor : " + decor_name)
        if Decor_Values.count(Decor_Dict[decor_name]) > 1:
            Failed4 += 1
            print("Decor duplication error : " + decor_name)

    print_result([Failed1, Failed2, Failed3, Failed4], [
                 Message1, Message2, Message3, Message4])
    sys.exit(Failed1 + Failed2 + Failed3 + Failed4)
