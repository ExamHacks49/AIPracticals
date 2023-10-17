import math
tree = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]
root, pruned = 0, 0
def alpha_beta_search(branch, depth, alpha, beta):
    global tree, root, pruned
    i = 0
    for child in branch:
        if type(child) == list:
            (nalpha, nbeta) = alpha_beta_search(child, depth+1, alpha, beta)
            if depth % 2 == 0:
                alpha = nbeta if nbeta > alpha else alpha
            else:
                beta = nalpha if nalpha < beta else beta
            branch[i] = alpha if depth % 2 == 0 else beta
            i += 1
        else:
            if depth % 2 == 0 and alpha < child:
                alpha = child
            if depth % 2 != 0 and beta > child:
                beta = child
            if alpha >= beta:
                pruned += 1
                break
    if depth == root:
        tree = alpha if root == 0 else beta
    return (alpha, beta)

(alpha, beta) = alpha_beta_search(tree, root, -math.inf, math.inf)
print ("(alpha, beta): ", alpha, beta)
print ("Result: ", tree)
print ("Times pruned: ", pruned)