import random
#untuk file dipisah dengan antar kolom didalam txt dipisah dengan koma

#panjang bit per-rule = 3+4+4+3+1 = 15 bit
#suhu = 3, waktu = 4, kondisi = 4, kelembapan = 3, terbang/tidak = 1

#encode data untung perbandingan per-individu
def encode_data(N,data_latih = []):#encode data ke biner; N = banyak baris data
    encoded = []
    encoding = []
    i = 0
    while (i < N):
        j = 0
        while (j < 5):# 5 kolom
            if (data_latih[i][j] == 'rendah'):
                encoding.append(1)
                encoding.append(0)
                encoding.append(0)
            elif (data_latih[i][j] == 'normal'):
                encoding.append(0)
                encoding.append(1)
                encoding.append(0)
            elif (data_latih[i][j] == 'tinggi'):
                encoding.append(0)
                encoding.append(0)
                encoding.append(1)

            elif (data_latih[i][j] == 'pagi'):
                encoding.append(1)
                encoding.append(0)
                encoding.append(0)
                encoding.append(0)
            elif (data_latih[i][j] == 'siang'):
                encoding.append(0)
                encoding.append(1)
                encoding.append(0)
                encoding.append(0)
            elif (data_latih[i][j] == 'sore'):
                encoding.append(0)
                encoding.append(0)
                encoding.append(1)
                encoding.append(0)
            elif (data_latih[i][j] == 'malam'):
                encoding.append(0)
                encoding.append(0)
                encoding.append(0)
                encoding.append(1)

            elif (data_latih[i][j] == 'cerah'):
                encoding.append(1)
                encoding.append(0)
                encoding.append(0)
                encoding.append(0)
            elif (data_latih[i][j] == 'berawan'):
                encoding.append(0)
                encoding.append(1)
                encoding.append(0)
                encoding.append(0)
            elif (data_latih[i][j] == 'rintik'):
                encoding.append(0)
                encoding.append(0)
                encoding.append(1)
                encoding.append(0)
            elif (data_latih[i][j] == 'hujan'):
                encoding.append(0)
                encoding.append(0)
                encoding.append(0)
                encoding.append(1)

            elif (data_latih[i][j] == 'rendah'):
                encoding.append(1)
                encoding.append(0)
                encoding.append(0)
            elif (data_latih[i][j] == 'normal'):
                encoding.append(0)
                encoding.append(1)
                encoding.append(0)
            elif (data_latih[i][j] == 'tinggi'):
                encoding.append(0)
                encoding.append(0)
                encoding.append(1)

            elif (data_latih[i][j] == 'ya\n' or data_latih[i][j] == 'ya'):
                encoding.append(1)
            elif (data_latih[i][j] == 'tidak\n' or data_latih[i][j] == 'tidak'):
                encoding.append(0)

            j = j+1
        encoded.append(encoding)
        encoding=[]
        i= i + 1
    return encoded

def encode_datauji(N,data_uji = []):
    encoded = []
    encoding = []
    i = 0
    while (i < N):
        j = 0
        while (j < 4): #4 kolom
            if (data_uji[i][j] == 'rendah'):
                encoding.append(1)
                encoding.append(0)
                encoding.append(0)
            elif (data_uji[i][j] == 'normal'):
                encoding.append(0)
                encoding.append(1)
                encoding.append(0)
            elif (data_uji[i][j] == 'tinggi'):
                encoding.append(0)
                encoding.append(0)
                encoding.append(1)

            elif (data_uji[i][j] == 'pagi'):
                encoding.append(1)
                encoding.append(0)
                encoding.append(0)
                encoding.append(0)
            elif (data_uji[i][j] == 'siang'):
                encoding.append(0)
                encoding.append(1)
                encoding.append(0)
                encoding.append(0)
            elif (data_uji[i][j] == 'sore'):
                encoding.append(0)
                encoding.append(0)
                encoding.append(1)
                encoding.append(0)
            elif (data_uji[i][j] == 'malam'):
                encoding.append(0)
                encoding.append(0)
                encoding.append(0)
                encoding.append(1)

            elif (data_uji[i][j] == 'cerah'):
                encoding.append(1)
                encoding.append(0)
                encoding.append(0)
                encoding.append(0)
            elif (data_uji[i][j] == 'berawan'):
                encoding.append(0)
                encoding.append(1)
                encoding.append(0)
                encoding.append(0)
            elif (data_uji[i][j] == 'rintik'):
                encoding.append(0)
                encoding.append(0)
                encoding.append(1)
                encoding.append(0)
            elif (data_uji[i][j] == 'hujan'):
                encoding.append(0)
                encoding.append(0)
                encoding.append(0)
                encoding.append(1)

            elif (data_uji[i][j] == 'rendah\n'):
                encoding.append(1)
                encoding.append(0)
                encoding.append(0)
            elif (data_uji[i][j] == 'normal\n'):
                encoding.append(0)
                encoding.append(1)
                encoding.append(0)
            elif (data_uji[i][j] == 'tinggi\n'):
                encoding.append(0)
                encoding.append(0)
                encoding.append(1)

            j = j + 1
        encoded.append(encoding)
        encoding = []
        i = i + 1
    return encoded

def pop_awal(jum_pop): #panjang per-rule 15 bit, max 4 rule, max bit = 60 bit;
    pop_kolom = []
    pop_baris = []
    i = 0
    while (i < jum_pop):
        j = 0
        rand_rule = random.randint(1,4) #random banyak rule per-individu, max rule = 4
        if (rand_rule == 1):
            while(j<15): #random 15 bit
                pop_kolom.append(random.randint(0,1))
                j = j+1
        elif (rand_rule == 2):
            while(j<30):#random 30 bit
                pop_kolom.append(random.randint(0,1))
                j = j+1
        elif (rand_rule == 3):
            while(j<45):#random 45 bit
                pop_kolom.append(random.randint(0,1))
                j = j+1
        elif (rand_rule == 4):
            while(j<60):#random 60 bit
                pop_kolom.append(random.randint(0,1))
                j = j+1

        pop_baris.append(pop_kolom)
        pop_kolom = []
        i = i+1

    return pop_baris


def hitungRule(krom = []):#menghitung banyak rule didalam kromosom
    count = 0
    while (count < len(krom)):
        count = count+1;

    if (count == 15):
        return 1
    elif (count == 30):
        return 2
    elif (count == 45):
        return 3
    elif (count == 60):
        return 4

def hitung_1(krom = []): #hitung jumlah true per-kolom data latih dan uji
    hasil = 0
    i = 0
    while (i < len(krom)):
        if (krom[i] == 1):
            hasil = hasil + 1
        i = i + 1;
    return hasil

def convert_biner(krom_random = [], krom_dataLatih = []):#hasil konversi AND per-rule dan per-data pada data latih
    hasil_konversi = []
    i = 0
    while (i < 15):
        if (krom_random[i] == 0 and krom_dataLatih[i] == 0):
            hasil_konversi.append(0)
        elif (krom_random[i] == 1 and krom_dataLatih[i] == 1):
            hasil_konversi.append(1)
        elif(krom_random[i] == 1 and krom_dataLatih[i] == 0):
            hasil_konversi.append(0)
        elif (krom_random[i] == 0 and krom_dataLatih[i] == 1):
            hasil_konversi.append(0)
        i = i + 1

    cek = 0
    i = 0
    while (i < len(hasil_konversi)):
        if(hasil_konversi[i] == 1):
            cek = cek + 1
        i = i + 1

    if (cek == 4 and krom_random[14] == 0 and krom_dataLatih[14] == 0):
        hasil_konversi[14] = 1

    return hasil_konversi


def convert_biner_uji(krom_terbaik = [], krom_dataUji = []):#hasil konversi AND per-rule dan per-data pada data uji
    hasil_konversi = []
    i = 0
    while (i < 14):
        if (krom_terbaik[i] == 0 and krom_dataUji[i] == 0):
            hasil_konversi.append(0)
        elif (krom_terbaik[i] == 1 and krom_dataUji[i] == 1):
            hasil_konversi.append(1)
        elif(krom_terbaik[i] == 1 and krom_dataUji[i] == 0):
            hasil_konversi.append(0)
        elif (krom_terbaik[i] == 0 and krom_dataUji[i] == 1):
            hasil_konversi.append(0)
        i = i + 1
    return hasil_konversi



def hitung_error(data_valid = []): #menghitung jumlah data yg error
    count_error = 0
    i = 0
    while (i < 80):
        if(data_valid[i] == 0):
            count_error = count_error + 1
        i = i + 1
    return count_error

def valid_test(kromosom_random = [], kromosom_dataLatih = []):#test kromosom untuk menunjukkan ada berapa data yg error di data dan ada berapa data yg tidak
    isidatalatih = kromosom_dataLatih.copy()
    krom_random = kromosom_random.copy()
    validitas = [] #banyaknya data yg valid atau true
    banyak_rule = hitungRule(krom_random)

    if (banyak_rule == 1):
        j = 0
        while (j < 80): #banyak data 80 baris
            #print(j)
            converted = convert_biner(krom_random,isidatalatih[j]) #convert hasil AND
            jumlah_true = hitung_1(converted)
            if (jumlah_true == 5):
                validitas.append(1)
            else:
                validitas.append(0)
            j = j + 1
    elif (banyak_rule == 2):
        j = 0
        while (j < 80):
            #print(j)
            point = 0 #untuk slice array
            point2 = 15 #untuk slice array
            k = 0
            while (k < 2):#banyak rule 2
                krom_random2 = krom_random[point:point2]
                converted = convert_biner(krom_random2,isidatalatih[j])
                jumlah_true = hitung_1(converted)
                if (jumlah_true == 5):
                    validitas.append(1)
                    k = k + 2 #jika salah satu rule valid maka hentikan iterasi
                elif (jumlah_true < 5 and k == 1): #jika rule terakhir tetap tidak ada yg valid maka data error
                    validitas.append(0)
                else:
                    point = point + 15
                    point2 = point2 + 15
                k = k + 1
            j = j + 1
    elif (banyak_rule == 3):#banyak rule 3
        j = 0
        while (j < 80):
            #print(j)
            point = 0
            point2 = 15
            k = 0
            while (k < 3):
                krom_random2 = krom_random[point:point2]
                converted = convert_biner(krom_random2,isidatalatih[j])
                jumlah_true = hitung_1(converted)
                if (jumlah_true == 5):
                    validitas.append(1)
                    k = k + 3 #jika salah satu rule valid maka hentikan iterasi
                elif (jumlah_true < 5 and k == 2):#jika rule terakhir tetap tidak ada yg valid maka data error
                    validitas.append(0)
                else:
                    point = point + 15
                    point2 = point2 + 15
                k = k + 1
            j = j + 1

    elif (banyak_rule == 4):  # banyak rule 4
        j = 0
        while (j < 80):
            point = 0
            point2 = 15
            k = 0
            while (k < 4):
                krom_random2 = krom_random[point:point2]
                converted = convert_biner(krom_random2, isidatalatih[j])
                jumlah_true = hitung_1(converted)
                if (jumlah_true == 5):
                    validitas.append(1)
                    k = k + 4  # jika salah satu rule valid maka hentikan iterasi
                elif (jumlah_true < 5 and k == 3):  # jika rule terakhir tetap tidak ada yg valid maka data error
                    validitas.append(0)
                else:
                    point = point + 15
                    point2 = point2 + 15
                k = k + 1
            j = j + 1
    return validitas
#------------------------------------------------------------

def valid_test_uji(k_terbaik = [], kromosom_dataUji = []):#test kromosom untuk menunjukkan ada berapa data yg error di data dan ada berapa data yg tidak
    isidatauji = kromosom_dataUji.copy()
    krom_terbaik = k_terbaik.copy()
    validitas = [] #banyaknya data yg valid atau true
    banyak_rule = hitungRule(krom_terbaik)

    if (banyak_rule == 1):
        j = 0
        while (j < 20): #banyak data 20 baris
            #print(j)
            converted = convert_biner_uji(krom_terbaik,isidatauji[j]) #convert hasil AND
            jumlah_true = hitung_1(converted)
            if (jumlah_true == 4):
                validitas.append(krom_terbaik[14])
            else:
                validitas.append(0)
            j = j + 1
    elif (banyak_rule == 2):
        j = 0
        while (j < 20):
            #print(j)
            point = 0 #untuk slice array
            point2 = 15 #untuk slice array
            k = 0
            while (k < 2):#banyak rule 2
                krom_random2 = krom_terbaik[point:point2]
                converted = convert_biner_uji(krom_random2,isidatauji[j])
                jumlah_true = hitung_1(converted)
                if (jumlah_true == 4):
                    validitas.append(krom_random2[14])
                    k = k + 2 #jika salah satu rule valid maka hentikan iterasi
                elif (jumlah_true < 4 and k == 1): #jika rule terakhir tetap tidak ada yg valid maka data error
                    validitas.append(0)
                else:
                    point = point + 15
                    point2 = point2 + 15
                k = k + 1
            j = j + 1
    elif (banyak_rule == 3):#banyak rule 3
        j = 0
        while (j < 20):
            #print(j)
            point = 0
            point2 = 15
            k = 0
            while (k < 3):
                krom_random2 = krom_terbaik[point:point2]
                converted = convert_biner_uji(krom_random2,isidatauji[j])
                jumlah_true = hitung_1(converted)
                if (jumlah_true == 4):
                    validitas.append(krom_random2[14])
                    k = k + 3 #jika salah satu rule valid maka hentikan iterasi
                elif (jumlah_true < 4 and k == 2):#jika rule terakhir tetap tidak ada yg valid maka data error
                    validitas.append(0)
                else:
                    point = point + 15
                    point2 = point2 + 15
                k = k + 1
            j = j + 1

    elif (banyak_rule == 4):  # banyak rule 4
        j = 0
        while (j < 20):
            point = 0
            point2 = 15
            k = 0
            while (k < 4):
                krom_random2 = krom_terbaik[point:point2]
                converted = convert_biner_uji(krom_random2, isidatauji[j])
                jumlah_true = hitung_1(converted)
                if (jumlah_true == 4):
                    validitas.append(krom_random2[14])
                    k = k + 4  # jika salah satu rule valid maka hentikan iterasi
                elif (jumlah_true < 4 and k == 3):  # jika rule terakhir tetap tidak ada yg valid maka data error
                    validitas.append(0)
                else:
                    point = point + 15
                    point2 = point2 + 15
                k = k + 1
            j = j + 1
    return validitas


def fitness(populasi = [], krom_dataLatih = []): #menghitung fitness per-individu didalam satu generasi
    #fungsi fitness yg digunakan (ndata-error)/ndata, ndata = 80
    isidatalatih = krom_dataLatih.copy()

    arr_fitness = []

    i = 0
    while (i < len(populasi)):
        validtest = valid_test(populasi[i],isidatalatih) #test validitas per-kromosom di data latih
        error = hitung_error(validtest) # jumlah error di data latih
        arr_fitness.append((80-error)/80) #hitung fitness

        i = i + 1
    return arr_fitness

def select_parent(populasi = [], fit = []): #cari parent 1 dan parent 2 dengan roulette wheel
    proporsi = []
    parent= []


    total_fitness = sum(fit) #total fitness

    i = 0
    while (i < len(populasi)): #hitung proporsi per-kromosom
        proporsi.append(fit[i]/total_fitness+0.01) # +0.01 mengurangi chance pembagian dengan 0
        i = i + 1


    j = 0
    while (j < 2):#select 2 parent
        random_double = round(random.uniform(0,1),3)
        current_prop = 0 #jumlah proporsi saat ini
        k = 0
        while (current_prop < random_double):
            current_prop += proporsi[k-1]
            k = k + 1
        parent.append(populasi[k-1])
        j = j + 1

    while (parent[0] == parent[1]): #menghindari isi parent yang sama
        random_double = round(random.uniform(0, 1), 3)
        current_prop = 0  # jumlah proporsi saat ini
        k = 0
        while (current_prop < random_double):
            current_prop += proporsi[k-1]
            k = k + 1
        parent[1] = populasi[k-1]

    return parent


def crossover(prob_cross,arr_parent = []):#dua point crossover, prob crossover random di main
    #sementara titik potongnya sama
    #parent 1: titik 1 dan titik 2 random, parent 2: titik 1 sama, titik 2 = gap(hasil nilai mod)

    child_1 = arr_parent[0]
    child_2 = arr_parent[1]
    child = []

    random_nilai = random.uniform(0,1)


    if(random_nilai < prob_cross):
        titik_1 = random.randint(1,14) #titik potong 1 untuk p1 dan p2
        titik_2 = random.randint(1,14) #titik potong 2 untuk p1

        arr_c1 = child_1[titik_1:titik_2]
        arr_c2 = child_2[titik_1:titik_2]

        child_1[titik_1:titik_2] =  arr_c2
        child_2[titik_1:titik_2] = arr_c1

        child = [child_1,child_2]
        return child

    else:
        return arr_parent


def mutasi(prob_mutasi, child = []):#metode mutasi yg digunakan yaitu metode bit flip mutation
    mutated = [] #kedua child akan dimutasi

    m_child1 = child[0]
    m_child2 = child[1]

    rule_child1 = hitungRule(m_child1)
    rule_child2 = hitungRule(m_child2)

    random_mutasi = random.uniform(0,1)

    if (random_mutasi < prob_mutasi):
        #proses child 1
        if (rule_child1 == 1): #jika isi kromosom 1 rule
            point = random.randint(0,14)
            if (m_child1[point] == 0):
                m_child1[point] = 1
            else:
                m_child1[point] = 0
        elif (rule_child1 == 2):  # jika isi kromosom 2 rule
            point = random.randint(0, 29)
            if (m_child1[point] == 0):
                m_child1[point] = 1
            else:
                m_child1[point] = 0
        elif (rule_child1 == 3):  # jika isi kromosom 3 rule
            point = random.randint(0, 44)
            if (m_child1[point] == 0):
                m_child1[point] = 1
            else:
                m_child1[point] = 0
        elif (rule_child1 == 4):  # jika isi kromosom 4 rule
            point = random.randint(0, 59)
            if (m_child1[point] == 0):
                m_child1[point] = 1
            else:
                m_child1[point] = 0

        #proses child2
        if (rule_child2 == 1): #jika isi kromosom 1 rule
            point = random.randint(0,14)
            if (m_child2[point] == 0):
                m_child2[point] = 1
            else:
                m_child2[point] = 0
        elif (rule_child2 == 2):  # jika isi kromosom 2 rule
            point = random.randint(0, 29)
            if (m_child2[point] == 0):
                m_child2[point] = 1
            else:
                m_child2[point] = 0
        elif (rule_child2 == 3):  # jika isi kromosom 3 rule
            point = random.randint(0, 44)
            if (m_child2[point] == 0):
                m_child2[point] = 1
            else:
                m_child2[point] = 0
        elif (rule_child2 == 4):  # jika isi kromosom 4 rule
            point = random.randint(0, 59)
            if (m_child2[point] == 0):
                m_child2[point] = 1
            else:
                m_child2[point] = 0
    mutated = [m_child1,m_child2]
    return mutated

def fit_rendah(fit = []):#mencari dua fitness terendah di dalam populasi
    fit2 = fit.copy()
    arr_point = []
    curr_fit = fit2[0]
    point = 0
    i = 0
    while (i < len(fit2)):
        if (fit2[i] < curr_fit):
            curr_fit = fit2[i]
            point = i
        i = i + 1
    arr_point.append(point)#point 1
    fit2[point] = 80

    point2 = 0
    i = 0
    curr_fit = fit2[0]
    while (i < len(fit2)):
        if (fit2[i] < curr_fit):
            curr_fit = fit2[i]
            point2 = i
        i = i + 1
    arr_point.append(point2)#point 2

    return arr_point


def general_replacement(populasi = [], offspring = [],fit = []):
    new_pop = populasi.copy() #copy populasi
    off1 = offspring[0] #offspring 1
    off2 = offspring[1] #offspring 2

    fitness_rendah = fit_rendah(fit)
    point1 = fitness_rendah[0] #terendah ke 1
    point2 = fitness_rendah[1] #terendah ke 2

    new_pop[point1] = off1 #tukar individu ke-point1 dengan offspring 1
    new_pop[point2] = off2 #tukar individu ke-point2 dengan offspring 2

    return new_pop


def fitness_terbaik(fit = []):
    info = [] #menyimpan info fitness terbaik dan individunya
    curr_fit = 0
    point = 0
    i = 0
    while (i < len(fit)):
        if (fit[i] > curr_fit):
            curr_fit = fit[i]
            point = i
        i = i + 1
    info.append(point)
    info.append(curr_fit)
    return info

def convert_text(label = []): #convert label 1 0 ke text
    arr_text = []
    i = 0
    while (i < len(label)):
        if (label[i] == 1):
            arr_text.append("ya")
        else:
            arr_text.append("tidak")
        i = i + 1
    return arr_text


if __name__ == "__main__":
    #banyak generasi nentuin sendiri
    #prob crossover dan mutasi ditentuin sendiri

    #untuk file dipisah dengan antar kolom didalam txt dipisah dengan koma

    data_latih = []
    data_L = open('data_latih.txt', 'r')  # read data latih
    isi_data_latih = [line.split(',') for line in data_L.readlines()]

    data_uji = []
    data_U = open('data_uji.txt', 'r')  # read data uji
    isi_data_uji = [line.split(',') for line in data_U.readlines()]

    print(isi_data_latih)
    #print(isi_data_uji)

    prob_crossover = 1 #probabilitas crossover
    prob_mutasi = 1 #probabilitas mutasi

    encoded_datalatih = encode_data(80,isi_data_latih) #encode data latih menjadi biner

    banyak_generasi = 200 #inisiasi generasi
    banyak_populasi = 80 #inisiasi populasi per-generasi

    populasi= pop_awal(banyak_populasi) #populasi random awal, dengan panjang individu berbeda
    print(".......................Mohon Tunggu dengan Sabar :)....................................")

    i = 0
    while (i < banyak_generasi):
        list_fitness = fitness(populasi, encoded_datalatih)  # list fitness semua individu
        parent = select_parent(populasi,list_fitness)
        child = crossover(prob_crossover,parent)
        offspring = mutasi(prob_mutasi,child)
        populasi = general_replacement(populasi,offspring,list_fitness)
        print("Generasi ke",i+1)
        print("Kalau error run ulang")
        i = i + 1

    best_fit = fitness_terbaik(list_fitness)
    point = best_fit[0]
    print("Individu terbaik generasi ke ",i,": ",populasi[point])
    print("==================================================================")
    best_kromosom = populasi[point]
    print("Fitness: ",best_fit[1])
    encode_uji = encode_datauji(20,isi_data_uji) #encode data uji
    label_datauji = valid_test_uji(best_kromosom,encode_uji)
    print("Hasil prediksi: ",label_datauji)
    label = convert_text(label_datauji)

    prediksi = open("prediksi.txt","w+")
    i = 0
    while (i < 20):
        prediksi.write(label[i])
        prediksi.write("\n")
        i = i + 1
    prediksi.close()

