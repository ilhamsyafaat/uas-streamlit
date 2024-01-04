import numpy as np
import math

# Fungsi-fungsi perhitungan MOORA
# (masukkan fungsi normalization, weighted_normalization, dan optimize_value ke sini)
def normalization(matrix):
    # Transpose Decision Matrix
    matrix = matrix.transpose()
    row_values = []
    norm_matrix = []
    
    for i in range(matrix.shape[0]): # Looping per baris (kriteria)
        # Menghitung sum tiap x_{ij}^2
        sum_row = sum([pow(x,2) for x in matrix[i]])
        
        for j in range(matrix[i].shape[0]): # Looping per kolom (alternatif)
            # membangi nilai asli x_{ij} dengan hasil akar
            r_value = matrix[i][j] / math.sqrt(sum_row)
            
            # Masukkan hasil normalisasi ke list tiap baris
            row_values.append(r_value)
        
        #Masukkan hasil normalisasi per baris ke matrix normalisasi
        norm_matrix.append(row_values)
        
        #Kosongkan list normalisasi perbaris
        row_values = []
            
    # Ubah dalam bentuk numpy array
    norm_matrix = np.asarray(norm_matrix)
    
    # Return dalam bentuk transporse agar kembali ke format awal
    return norm_matrix.transpose()


# Fungsi untuk kalkulasi matrix terbobot. Paramter yang diperlukan adalah nilai ternormalisasi dan bobot
# Untuk mempermudah perhitungan, lakukan operasi transpose pada matrix ternormalisasi.
# Ingat! Kriteria adalah baris, alternatif adalah kolom setelah proses transpose
def weighted_normalization(n_matrix, c_weights):
    # Buat salinan nilai ternormalisasi dan transpose
    norm_weighted = n_matrix.transpose()
    
    for i in range(c_weights.shape[0]): # Looping tiap kriteria
        # Kalkulasi normalisasi terbobot
        norm_weighted[i] = [r * c_weights[i] for r in norm_weighted[i]]
    
    # Ubah ke bentuk numpy array
    norm_weighted = np.asarray(norm_weighted)
    
    # Return ke dalam format matrix semula
    return norm_weighted.transpose()


# Implementasi Menghitung Nilai Optimasi
def optimize_value(w_matrix, label):
    y_values = []
    
    for i in range(w_matrix.shape[0]):
        max_val = []
        min_val = []
        
        for j in range(w_matrix[i].shape[0]):
            # Hitung benefit
            if label[j] == 1:
                max_val.append(w_matrix[i][j])
            # Hitung cost
            else:
                min_val.append(w_matrix[i][j])
        
        y = sum(max_val) - sum(min_val)
        y_values.append(y)
    
    return np.asarray(y_values)