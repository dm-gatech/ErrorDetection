import numpy as np 

def low_rank_approximation(A, c):
    '''
    A function to compute low rank approximation with rank k, where
    k is chosen based singular values of A. 
    Rule of Thumb: choose k such that top k eigenvalues is at least 
    c times as big as the sum of other eigenvalues, where c is a domain-dependent 
    constant. 
    Return u_k, s_k, v_k
    '''
    u, s, v = np.linalg.svd(A, full_matrices=False)    # Compute SVD

    # Choose a proper value for k
    # take advantage of s storeing singular values in descending orders
    k = 1
    top_k_sum = np.sum(s[:k])
    rest_sum = np.sum(s[k:])
    while(top_k_sum <= c * rest_sum):
        k += 1
        top_k_sum += s[k-1]
        rest_sum -= s[k-1]


    s_k = np.diag(s[:k]) # Take first k important eigenvalues
    u_k = u[:, :k]          # Take top k left singular vectors
    v_k = v[:k, :]          # Take top k right singular vectors
    
    return u_k, s_k, v_k;


A = np.random.randint(5, size=(100, 400000))
(u_k, s_k, v_k) = low_rank_approximation(A, 10)
print(s_k)

