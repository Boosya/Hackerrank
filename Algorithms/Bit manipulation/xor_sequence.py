def calc_head(L, seq_beg):
    sum_dict = {1: seq_beg-1, 2: seq_beg-1, 3: (L+1)^(L+2)}
    return sum_dict[seq_beg - L]

def calc_tail(R, prev_div_4):
    sum_dict = {1: 1, 2: prev_div_4+ 2, 3: prev_div_4+ 2}
    for _ in range(R, prev_div_4):
        pass
    return sum_dict[R - prev_div_4]


def calculate_xor_quick(beg_i, end_i):
    answer = 0
    prev_div_4 = end_i // 4 * 4
    nb_seq = (prev_div_4 - beg_i+1) // 4
    seq_beg = prev_div_4 - 4* nb_seq+1
    answer = answer ^ calc_xor_seq( prev_div_4 - 4* nb_seq+1, nb_seq)
    if end_i != prev_div_4:
        answer  = answer^calc_tail(end_i, prev_div_4)
    if beg_i != seq_beg:
        answer = answer ^ calc_head(beg_i, seq_beg)

    return answer

def calc_xor_seq(beg_i, nb_seq):
    answer = 0
    shift = 1
    for _ in range(2*nb_seq):
        answer = answer^(beg_i+shift)
        shift += 2
    return answer

def generate_A(end_i):
    A = [0]*(end_i+1)
    A[0] = 0
    for i in range(end_i+1):
        A[i] = A[i-1]^i
    return A

def calculate_xor(beg_i, end_i, A):
    answer = 0
    for i in range(beg_i, end_i+1):
        answer = answer^A[i]
    return answer

A = generate_A(20)
print(A)
L = 2
R = 8
print(calculate_xor_quick(L,R))
print(calculate_xor(L,R,A))
# print(calc_sum(2,8))
