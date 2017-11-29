# integar_formula = [

integar_ret_formula11 = [
    ("sin[x]","cos[x]"),
    ("cos[x]","-sin[x]"),
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
all = [integar_ret_formula01,integar_ret_formula11]