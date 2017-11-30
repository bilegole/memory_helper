# integar_formula = [

integar_ret_formula11 = [
    ("sin[x]","-cos[x]"),
    ("cos[x]","sin[x]"),
    ("tan[x]","-ln|cosx|"),
    ("csc[x]","ln|csc[x]-cot[x]|"),
    ("sec[x]","ln|sec[x]+tan[x]|"),
    ("sec^2[x]","tan[x]"),
    ("csc^2[x]","-cot[x]"),
    ("sec[x]tan[x]","sec[x]"),
    ("csc[x]cot[x]","-csc[x]")
    # ("x")
]
integar_ret_formula01 = [
    ("1/(a^2+x^2)","(1/a)arctan[x/a]"),
    ("-1/(a^2+x^2)","(1/a)arccot[x/a]"),
    ("1/√(1-x^2)","arcsin[x]"),
    ("-1/√(1-x^2)","arccos[x]")
]

'''
和差化积系列
'''
sum_mil = [
    ("sin[a]cos[b]","(1/2)(sin[a+b]+sin[a-b])"),
    ("sin[a]sin[b]","-(1/2)(cos[a+b]-cos[a-b])"),
    ("cos[a]cos[b]","(1/2)(cos[a+b]+cos[a-b])"),
    ("cos[a]sin[b]","(1/2)(sin(a+b]-sin[a-b])")
]
all = [integar_ret_formula01,integar_ret_formula11]