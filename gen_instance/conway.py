import itertools
from itertools import combinations
from itertools import product

def remove_duplicates(lst):
    unique_elements = set()
    result = []
    for sublist in lst:
        sublist = [x for x in sublist if x not in unique_elements]
        unique_elements.update(sublist)
        if sublist:
            result.append(sublist)
    return result

def generate_combinations(lst):
    result = set()
    for items in product(*lst):
        if len(set(items)) == len(items):
            result.add(tuple(sorted(items)))
    return list(result)

def conway(n, edge_dict, tri_dict, count_dict, cnf, var_count, fixed = False):
    #at least vs vertices are connected to at least t triangles
    clause_count = 0
    cnf_file = open(cnf, 'a+')
    vertices_lst = list(range(1, n+1))
    all_tri = list(itertools.combinations(vertices_lst, 3))
    t = max(count_dict.values())
    extra_var_dict_master = {}

    for triangle in list(itertools.combinations(vertices_lst, 3)):
        # the following encoding are applied in every possible triangle in the graph
        # given a triangle, if encode the equivalence relation
        v_1 = triangle[0]
        v_2 = triangle[1]
        v_3 = triangle[2]
        vertices = [v_1, v_2, v_3]
        vertices.sort()
        edge_1 = (vertices[0], vertices[1])
        edge_2 = (vertices[1], vertices[2])
        edge_3 = (vertices[0], vertices[2])
        cnf_file.write('{} {} 0\n'.format(str(edge_dict[edge_1]), str(-tri_dict[triangle])))
        cnf_file.write('{} {} 0\n'.format(str(edge_dict[edge_2]), str(-tri_dict[triangle])))
        cnf_file.write('{} {} 0\n'.format(str(edge_dict[edge_3]), str(-tri_dict[triangle])))
        cnf_file.write('{} {} {} {} 0\n'.format(str(-edge_dict[edge_1]), str(-edge_dict[edge_2]), str(-edge_dict[edge_3]), str(tri_dict[triangle])))
        clause_count += 4

    for v in range(1, n+1):
        v_tri_lst = [tri for tri in all_tri if v in tri] #triangles containing v
        #want to include that at least t of the vars are True
        extra_var_dict = {}
        for i in range(0, len(v_tri_lst)+1): #0 to n
            for j in range(0, t+1): #0 to t
                extra_var_dict[(i,j)] = var_count + 1
                var_count += 1
        for j in range(1, t+1): # s0,j will be false for 1 ≤ j ≤ t
            clause = "-" + str(extra_var_dict[(0,j)])
            cnf_file.write(clause + " 0\n")
            clause_count += 1
        for i in range(0, len(v_tri_lst)+1): # si,0 will be true for 0 ≤ i ≤ n
            clause = str(extra_var_dict[(i,0)])
            cnf_file.write(clause + " 0\n")
            clause_count += 1
        for i in range(1, len(v_tri_lst)+1):
            for j in range(1, t+1):
                clause_1 = "-" + str(extra_var_dict[(i-1,j)]) + " " + str(extra_var_dict[(i,j)])
                clause_2 = "-" + str(tri_dict[v_tri_lst[i-1]]) + " " + "-" + str(extra_var_dict[(i-1,j-1)]) + " " + str(extra_var_dict[(i,j)])
                clause_3 = "-" + str(extra_var_dict[(i,j)]) + " " + str(extra_var_dict[(i-1,j)]) + " " + str(tri_dict[v_tri_lst[i-1]])
                clause_4 = "-" + str(extra_var_dict[(i,j)]) + " " + str(extra_var_dict[(i-1,j)]) + " " + str(extra_var_dict[(i-1,j-1)])
                cnf_file.write(clause_1 + " 0\n")
                cnf_file.write(clause_2 + " 0\n")
                cnf_file.write(clause_3 + " 0\n")
                cnf_file.write(clause_4 + " 0\n")
                clause_count += 4
        extra_var_dict_master[v] = extra_var_dict
    for vs in count_dict:
        t = count_dict[vs]
        print (t)
        ind = []
        ind_dict = {}
        for v in range(1, n+1):
            extra_var_dict = extra_var_dict_master[v]
            ind.append(extra_var_dict[(len(v_tri_lst),t)])
            ind_dict[extra_var_dict[(len(v_tri_lst),t)]] = v
        combinations_lst = list(combinations(ind, int(len(ind))-int(vs)+1))
        # Print the combinations
        for combination in combinations_lst:
            constraint_1 = ' '.join(str(value) for value in combination)
            cnf_file.write(constraint_1 + " 0\n")
            clause_count += 1
    if fixed:
        clause = ""
        for tri in all_tri:
            ind_var = var_count + 1
            v1, v2, v3 = tri[0], tri[1], tri[2]
            v1_ind = next(key for key, value in ind_dict.items() if value == v1)
            v2_ind = next(key for key, value in ind_dict.items() if value == v2)
            v3_ind = next(key for key, value in ind_dict.items() if value == v3)
            #ind_var <-> tri and ind_1 and ind_2 and ind_3
            clause_1 = str(ind_var) + " -" + str(tri_dict[tri]) + " -" + str(v1_ind) + " -" + str(v2_ind) + " -" + str(v3_ind)
            clause_2 = "-" + str(ind_var) + " " + str(tri_dict[tri])
            clause_3 = "-" + str(ind_var) + " " + str(v1_ind)
            clause_4 = "-" + str(ind_var) + " " + str(v2_ind)
            clause_5 = "-" + str(ind_var) + " " + str(v3_ind)
            cnf_file.write(clause_1 + " 0\n")
            cnf_file.write(clause_2 + " 0\n")
            cnf_file.write(clause_3 + " 0\n")
            cnf_file.write(clause_4 + " 0\n")
            cnf_file.write(clause_5 + " 0\n")
            clause = clause + str(ind_var) + " "
            clause_count += 5
            var_count += 1
        cnf_file.write(clause + "0")
        clause_count += 1
    
    return var_count, clause_count