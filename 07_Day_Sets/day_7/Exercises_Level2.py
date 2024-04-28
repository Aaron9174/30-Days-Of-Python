########################################
#          EXERCISES - Level 2         #
#             Sets Practice            #
########################################

A = {19, 22, 24, 20, 25, 26}
print(f"Set A is:\n{A}")
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(f"Set B is:\n{B}")

a_union_b = A.union(B)
print(f"The union of A and B is:\n{a_union_b}")

a_intersection_b = A.intersection(B)
print(f"The intersection of A and B is:\n{a_intersection_b}")

is_a_subset_of_b = A.issubset(B)
print(f"Is A a subset of B? {is_a_subset_of_b}")

is_a_disjointed_with_b = A.isdisjoint(B)
print(f"Is A disjointed from B? {is_a_disjointed_with_b}")

a_union_b_union_a = A.union(B).union(B.union(A))
print(f"Join A with B and B with A into one set:\n{a_union_b_union_a}")

symmetric_difference = A.symmetric_difference(B)
print(f"The symmetric difference of A and B:\n{symmetric_difference}")
del A
del B