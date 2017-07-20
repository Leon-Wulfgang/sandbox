# Two Gold Stars
# Question 2: Combating Link Spam

# One of the problems with our page ranking system is pages can
# collude with each other to improve their page ranks.  We consider
# A->B a reciprocal link if there is a link path from B to A of length
# equal to or below the collusion level, k.  The length of a link path
# is the number of links which are taken to travel from one page to the
# other.

# If k = 0, then a link from A to A is a reciprocal link for node A,
# since no links needs to be taken to get from A to A.

# If k=1, B->A would count as a reciprocal link  if there is a link
# A->B, which includes one link and so is of length 1. (it requires
# two parties, A and B, to collude to increase each others page rank).

# If k=2, B->A would count as a reciprocal link for node A if there is
# a path A->C->B, for some page C, (link path of length 2),
# or a direct link A-> B (link path of length 1).

# Modify the compute_ranks code to
#   - take an extra input k, which is a non-negative integer, and
#   - exclude reciprocal links of length up to and including k from
#     helping the page rank.


def is_reciprocal(graph, k, page_start, page_end):
    #print(k, page_start, page_end)

    # base case: when k is 0, we only check same level link
    if k == 0:
        # they exist on the same level
        if page_end == page_start:
            return True
        # they don't
        return False

    # base case: page_start is in page_end's link
    elif page_start in graph[page_end]:
        return True

    # recursion: --k and check each links of page_end
    # print(page_start,page_end,k)
    for page_end_link in graph[page_end]:
        # check if page_start and each page_end_link is relative
        if is_reciprocal(graph, k-1, page_start, page_end_link):
            return True
    # every link of them check, finally false
    return False


def compute_ranks(graph, k):

    # initial values
    d = 0.8 # damping factor
    numloops = 10 # do 10 loops to refine ranking
    ranks = {} # init empty ranking
    npages = len(graph) # number of pages in the graph

    # init each page's ranking with 1/n
    for page_start in graph:
        ranks[page_start] = 1.0 / npages

    # do loops of refine
    for i in range(0, numloops):
        # init empty new ranking
        newranks = {}
        # do each page in the graph
        for page_start in graph:
            # new base ranking is 1-d/n , 0.2 * 1/4 = 0.05
            newrank = (1 - d) / npages
            # do a search from start to end, for each of the pages
            for page_end in graph:
                # found page start in links of page_end
                if page_start in graph[page_end]:
                    # check if page_start and page_end are relatives to each other(link to each other in <= k steps)
                    is_rec = is_reciprocal(graph, k, page_end, page_start)
                    #print(is_rec,page_start,page_end)
                    if not is_rec:
                    #if not is_reciprocal(graph, page_end, page_start, k):
                        # set page_start's weight to be
                        #    base + d * (previous_weight/n_links_of_page_end)
                        newrank = newrank + d * (ranks[page_end]/len(graph[page_end]))
            # update page_start's weight
            newranks[page_start] = newrank
        # replace with new ranking
        #print(newranks)
        ranks = newranks
    return ranks

# For example

g = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}

print(compute_ranks(g, 0)) # the a->a link is reciprocal
#>>> {'a': 0.26676872354238684, 'c': 0.1216391112164609,
#     'b': 0.1216391112164609, 'd': 0.1476647842238683}

print(compute_ranks(g, 1)) # a->a, a->b, b->a links are reciprocal
#>>> {'a': 0.14761759762962962, 'c': 0.08936469270123457,
#     'b': 0.04999999999999999, 'd': 0.12202199703703702}

print(compute_ranks(g, 2))
#print(is_reciprocal(g,2,'d','a'))
#print(g['a'])
# a->a, a->b, b->a, a->c, c->d, d->a links are reciprocal
# (so all pages end up with the same rank)
#>>> {'a': 0.04999999999999999, 'c': 0.04999999999999999,
#     'b': 0.04999999999999999, 'd': 0.04999999999999999}

