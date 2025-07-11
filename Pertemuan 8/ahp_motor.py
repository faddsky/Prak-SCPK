import numpy as np

def calc_norm(M):
    print('\nNormalisasi Matriks')
    if M.ndim == 1:  # Check if M is a vector
        sM = np.sum(M)
        return M / sM
    else:
        sM = np.sum(M, axis=0)
        return M / sM

def ahp():
    # Step 1: Matrix Kriteria dan Eigenvector Kriteria
    print('Matriks Perbandingan Berpasangan pada Kriteria')
    # (G)   (A)    (E)    
    MPBk = np.array([
        [1/1, 1/2, 3/1],  # (G-Gaya)
        [2/1, 1/1, 4/1],  # (A-Keandalan)
        [1/3, 1/4, 1/1]   # (E-Keekonomisan)
    ])
    print(MPBk)
    
    # Normalisasi
    w_MPB = calc_norm(MPBk)
    print(w_MPB)
    
    # Hitung Eigenvector
    m, n = w_MPB.shape
    V = np.zeros(m)
    for i in range(m):
        V[i] = np.sum(w_MPB[i, :])
    
    print('\nEigenvektor')
    w_MPB = V / m
    print(w_MPB)
    
    # Step 2: Matrix Alternatif dan Eigenvectors Alternatif
    # Bandingkan Gaya:
    print('\nPerbandingan Gaya: Alternatif Kualitatif Berpasangan')
    AKB_G = np.array([
        [1/1, 1/2, 2/1, 1/3],
        [2/1, 1/1, 3/1, 1/2],
        [1/2, 1/3, 1/1, 1/4],
        [3/1, 2/1, 4/1, 1/1]
    ])
    print(AKB_G)
    
    w_G = calc_norm(AKB_G)
    print(w_G)
    
    m, n = w_G.shape
    V = np.zeros(m)
    for i in range(m):
        V[i] = np.sum(w_G[i, :])
    
    print('\nEigenvector')
    w_G = V / m
    print(w_G)
    
    # Bandingkan Keandalan:
    print('\nPerbandingan Keandalan: Alternatif Kualitatif Berpasangan')
    AKB_A = np.array([
        [1/1, 1/2, 3/1, 2/1],
        [2/1, 1/1, 4/1, 3/1],
        [1/3, 1/4, 1/1, 1/2],
        [1/2, 1/3, 2/1, 1/1]
    ])
    print(AKB_A)
    
    w_A = calc_norm(AKB_A)
    print(w_A)
    
    m, n = w_A.shape
    V = np.zeros(m)
    for i in range(m):
        V[i] = np.sum(w_A[i, :])
    
    print('\nEigenvector')
    w_A = V / m
    print(w_A)
    
    # Bandingkan Keekonomisan Bahan Bakar:
    print('\nPerbandingan Keekonomisan Bahan Bakar: Alternatif Kuantitatif')
    ym = 60  # yamaha
    hn = 80  # honda
    sz = 60  # suzuki
    kw = 80  # kawasaki
    
    ACM_Fe = np.array([ym, hn, sz, kw])
    print(ACM_Fe)
    
    w_E = calc_norm(ACM_Fe)
    print(w_E)
    
    # Step 3: Menghitung Jawaban Akhir dan Vector Keputusan
    print('Tekan Enter untuk melanjutkan')
    input()
    
    # Gabung Nilai Eigenvector menjadi Matrix
    wM = np.column_stack((w_G, w_A, w_E))
    
    # Menghitung Score Akhir
    print('Nilai akhir untuk: yamaha, honda, suzuki, kawasaki')
    MC_Scores = np.dot(wM, w_MPB)
    print(MC_Scores)
    
    # Mencari Motor Terbaik
    print('\nNilai Motor terbaik terpilih berdasarkan manfaat (kriteria)')
    Max_Motor_Score = np.max(MC_Scores)
    print(Max_Motor_Score)
    
    return Max_Motor_Score

if __name__ == "__main__":
    # Fungsi Clear Screen
    print('\033c', end='')
    
    Max_Score = ahp()