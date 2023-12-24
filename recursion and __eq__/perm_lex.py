# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in):
    perm_list = []
    if len(str_in) == 1:
        return list(str_in)
    else:
        for i in range(len(str_in)):
            simpler_str = str_in[:i] + str_in[i+1:]
            small_permutation = perm_gen_lex(simpler_str)
            for j in range(len(small_permutation)):
                val = str_in[i] + small_permutation[j]
                perm_list.append(val)
        return perm_list
