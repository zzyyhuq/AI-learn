import numpy as np




def get_dot(vec_a , vec_b):
    if len(vec_a)!=len(vec_b):
        raise ValueError("2个向量必须维度数量相同")

    dot_sum = 0
    for a,b in zip(vec_a , vec_b):
        dot_sum+=a*b

    return dot_sum

def get_norm(vec):
    sum_squares=0
    for v in vec:
        sum_squares+=v**2

    return np.sqrt(sum_squares)

def cosine_similarity(vec_a,vec_b):
    result = get_dot(vec_a,vec_b)/(get_norm(vec_a)*get_norm(vec_b))
    return result

if __name__ == '__main__':
    vec_a = [0.5,0.5]
    vec_b = [0.7,0.7]
    vec_c = [0.5,0.7]
    vec_d = [-0.5,-0.5]

    print("ab:",cosine_similarity(vec_a,vec_b))
    print("ac:",cosine_similarity(vec_a,vec_c))
    print("ad:",cosine_similarity(vec_a,vec_d))

