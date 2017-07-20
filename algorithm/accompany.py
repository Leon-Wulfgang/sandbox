
find_anagrams(words) -> grouping of anagrams

>> find_anagrams(["cat", "act", "dog"])
[["cat", "act"], ["dog"]]

caat  act
acta


# dict[word] = [char_sorted]
# dict[word] = []


def get_sorted_chars(word):
    return sorted(word)


def construct(words): # ["cat", "act", "dog", "tacc"]
    dict_words = {}
    # dict = {
    #     cat: act
    #     act: act
    #     dog: dgo
    #    tacc: acct
    # }
    #
    for word in words: # cat
        dict_words[word] = get_sorted_chars(word)
    return dict_words


def produce_final_anagrams_array(dict_words_sorted):
    dict_char_sets_to_words = {}
    # dict_char_sets_to_words = {
    #     act: [cat, act]
    #     dgo: [dog]
    #    acct: [tacc]
    # }
    for word, sorted_chars in dict_words_sorted.items(): # cat, act
        if sorted_chars  not in dict_char_sets_to_words:
            dict_char_sets_to_words[sorted_chars] = [word]
        else:
            dict_char_sets_to_words[sorted_chars].append(word)
    result = []
    for key ,item in dict_char_sets_to_words.items():
        result += item
    return result
    # [[cat, act], [dog], [tacc]]

inp = ["cat", "act", "dog", "tacc"]

dict_words = construct(inp)
print produce_final_anagrams_array(dict_words)

inp = [binfile1, binfile2, binfile3]
dict_char_count[a] :1
dict_char_count[file_]

# =========

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
1
4 2
7 5 3
8 6
9

[[1, 2],
 [3, 4],
 [5, 6]]
1
3 2
5 4
6


# pointer => sub[0]
# feature scan upper right dig, and go until outofbounds

def get_current_line(inp, i, j): # 1,0     [2,2]
    list_d = [inp[i ,j]] # [1] [4, 2] [7, ]
    out_bound = false
    while not out_bound:
        i += 1
        j -= 1
        try  :# 1, -1  [2, -1]
            list_d.append(inp[i ,j])
        except:
            out_bound = True
    return list_d


inp =   [[1, 2, 3],
         [4, 5, 6],
         [7, 8, (9)]]


# start from left top most
pointer_base_i, pointer_base_j = 0, 0
for i range(0, len(inp ) +len(inp[0] ) -1):
    print get_current_line(inp, pointer_base_i, pointer_base_j)
    if pointer_base_i == len(inp): # 3, 3 [3,1] [3,2]
        pointer_base_j += 1
    else:
        pointer_base_i += 1





