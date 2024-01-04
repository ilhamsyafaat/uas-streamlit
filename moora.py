import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from moora_functions import normalization, weighted_normalization, optimize_value

# Fungsi MOORA
def moora_method(decision_matrix, weights, label):
    norm_matrix = normalization(decision_matrix)
    weighted_matrix = weighted_normalization(norm_matrix, weights)
    result = optimize_value(weighted_matrix, label)
    return result

def main():
    st.set_page_config(
        page_title="Implementasi MOORA",
        page_icon="👋",
    )

    st.write("# Implementasi Metode MOORA")
    st.write("Dikembangkan oleh Muh. Ilham Syafa'at D. F")

    st.markdown(
        """
        SMA XYZ akan melakukan seleksi untuk menentukan Guru terbaik tahun ajaran 2019/2020. Beberapa kriteria yang akan digunakan dalam penilaian selesi tersebut adalah, 

        1. Memilki pretasi dalam bidang akademik maupun non-akademik. (C1)
        2. Memiliki sifat kepemimpinan baik. (C2)
        3. Tingkat kesibukan. (C3)
        4. Absensi. (C4)
        5. Mempunyai keahlian dalam bidang ekstrakulikuler. (C5)
        6. Memiliki hubungan sejawat baik. (C6)

        Sedangkan kandidat guru terbaik adalah sebagai berikut,

        1. Hamdi, S.Pd.
        2. Purwanto, S.Pd.
        3. Lutfi Subhan, S.Pd.
        4. Dewi Rosatika, S.Pd.
        5. Tati Sunarti, S.Pd.

        Pihak panitia seleksi, menentukan bobot untuk setiap kriteria adalah sebagai berikut,

        |No | Kriteria | Bobot |
        |:---:|:---:|:---:|
        | 1 | C1 | 0.290 |
        | 2 | C2 | 0.173 |
        | 3 | C3 | 0.091 |
        | 4 | C4 | 0.162 |
        | 5 | C5 | 0.080 |
        | 6 | C6 | 0.204 |

        Penilaian tiap kriteria, ditentukan oleh skala berikut,

        Untuk C1, C2, dan C5

        | Opsi Penilaian | Skala Nilai |
        |:---:|:---|
        | Ya | 1 |
        | Tidak | 0 |

        Untuk C3

        | Opsi Penilaian | Skala Nilai |
        |:---:|:---:|
        | Sangat Sibuk | 1 |
        | Sibuk | 2 |
        | Wajar | 3 |
        | Tidak Sibuk | 4 |

        Untuk C4

        | Opsi Penilaian | Skala Nilai |
        |:---:|:---:|
        | Sangat Rajin | 4 |
        | Rajin | 3 |
        | Kurang Rajin | 2 |
        | Tidak Rajin | 1 |

        Untuk C6

        | Opsi Penilaian | Skala Nilai |
        |:---:|:---:|
        | Sangat Baik | 4 |
        | Baik | 3 |
        | Kurang Baik | 2 |
        | Tidak Baik | 1 |

    """
    )

    # Input data
    st.header("Input Data")
    init_matrix = st.text_area("Masukkan Matrix Alternatif (pisahkan dengan koma dan baris dengan newline)", value="1,1,3,4,1,4\n1,1,4,3,1,3\n1,1,4,4,1,4\n1,1,3,3,0,3\n1,1,3,3,1,4")
    init_matrix = np.array([list(map(int, row.split(','))) for row in init_matrix.split('\n')])

    c_weights = st.text_area("Masukkan Bobot Kriteria (pisahkan dengan koma)", value="0.290,0.173,0.091,0.162,0.080,0.204")
    c_weights = np.array(list(map(float, c_weights.split(','))))

    label = st.text_area("Masukkan Label Kriteria (pisahkan dengan koma)", value="1,1,0,0,1,1")
    label = np.array(list(map(int, label.split(','))))

    # Button untuk menghitung hasil
    if st.button("Hitung Hasil"):
        st.header("Hasil Perhitungan MOORA")

        # Normalisasi
        norm_matrix = normalization(init_matrix)

        # Normalisasi Terbobot
        weighted_matrix = weighted_normalization(norm_matrix, c_weights)

        # Optimasi Nilai
        result_values = optimize_value(weighted_matrix, label)

        # Menampilkan hasil
        st.subheader("Matrix Ternormalisasi:")
        st.write(norm_matrix)

        st.subheader("Matrix Ternormalisasi Terbobot:")
        st.write(weighted_matrix)

        st.subheader("Hasil Optimasi (Y):")
        st.write(result_values)

        # Menampilkan visualisasi data pendukung output (grafik batang)
        visualize_data(result_values)

def visualize_data(y_values):
    fig, ax = plt.subplots(figsize=(8, 6))

    alternatives = [f'Alternatif {i + 1}' for i in range(len(y_values))]
    ax.barh(alternatives, y_values, color='skyblue')
    ax.set_xlabel('Nilai Y')
    ax.set_title('Hasil Optimasi MOORA')

    st.pyplot(fig)

if __name__ == "__main__":
    main()
