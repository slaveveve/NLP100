# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. 
# New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置
# （先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

def chemical_symbol(sentence: str) :
    chemical_symbol_list = {}
    splitted_sentence = sentence.split()
    first_str_only = (1, 5, 6, 7, 8, 9, 15, 16, 19)

    for i, word in enumerate(splitted_sentence, 1) :
        if i in first_str_only :
            chemical_symbol_list[word[:1]] = i
        else :
            chemical_symbol_list[word[:2]] = i            

    return chemical_symbol_list

chemical_symbol("Hi He Lied Because Boron Could Not Oxidize Fluorine.\
 New Nations Might Also Sign Peace Security Clause. Arthur King Can.")