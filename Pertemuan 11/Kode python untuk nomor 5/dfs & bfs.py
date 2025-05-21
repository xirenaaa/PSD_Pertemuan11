from collections import deque

class Graf:
    def __init__(self):
        self.graf_dict = {}
    
    def tambah_simpul(self, simpul):
        if simpul not in self.graf_dict:
            self.graf_dict[simpul] = []
    
    def tambah_sisi(self, simpul1, simpul2):
        self.tambah_simpul(simpul1)
        self.tambah_simpul(simpul2)
        self.graf_dict[simpul1].append(simpul2)
        self.graf_dict[simpul2].append(simpul1)
    
    def dfs_rekursif(self, simpul_awal):
        if simpul_awal not in self.graf_dict:
            return []
        
        simpul_dikunjungi = set()
        
        hasil_dfs = []
        
        def jelajah_dfs(simpul_saat_ini):
            simpul_dikunjungi.add(simpul_saat_ini)
            
            hasil_dfs.append(simpul_saat_ini)
        
            for tetangga in self.graf_dict[simpul_saat_ini]:
                if tetangga not in simpul_dikunjungi:
                    jelajah_dfs(tetangga)
        
        jelajah_dfs(simpul_awal)
        
        return hasil_dfs
    
    def dfs_iteratif(self, simpul_awal):
        if simpul_awal not in self.graf_dict:
            return []
        
        simpul_dikunjungi = set()
        
        stack = [simpul_awal]
        
        hasil_dfs = []
        
        while stack:
            simpul_saat_ini = stack.pop()
            
            if simpul_saat_ini not in simpul_dikunjungi:
                simpul_dikunjungi.add(simpul_saat_ini)
                
                hasil_dfs.append(simpul_saat_ini)
                
                for tetangga in reversed(self.graf_dict[simpul_saat_ini]):
                    if tetangga not in simpul_dikunjungi:
                        stack.append(tetangga)
        
        return hasil_dfs
    
    def bfs(self, simpul_awal):
        if simpul_awal not in self.graf_dict:
            return []
        
        simpul_dikunjungi = set()
        
        antrian = deque([simpul_awal])
        
        simpul_dikunjungi.add(simpul_awal)
        
        hasil_bfs = []
        
        while antrian:
            simpul_saat_ini = antrian.popleft()
            
            hasil_bfs.append(simpul_saat_ini)
            
            for tetangga in self.graf_dict[simpul_saat_ini]:
                if tetangga not in simpul_dikunjungi:
                    simpul_dikunjungi.add(tetangga)
                    antrian.append(tetangga)
        
        return hasil_bfs
    
    def tampilkan_graf(self):
        print("\n=== Representasi Graf (Adjacency List) ===")
        for simpul, tetangga in self.graf_dict.items():
            print(f"Simpul '{simpul}' terhubung dengan: {tetangga}")


if __name__ == "__main__":
    print("=== Program Implementasi Algoritma DFS dan BFS ===")
    graf = Graf()
    
    sisi_graf = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'F'), ('C', 'G'),
        ('E', 'H'), ('F', 'I')
    ]
    
    print("\nMenambahkan sisi-sisi berikut ke graf:")
    for index, sisi in enumerate(sisi_graf, 1):
        print(f"{index}. {sisi[0]} -- {sisi[1]}")
        graf.tambah_sisi(sisi[0], sisi[1])
    
    graf.tampilkan_graf()
    
    simpul_awal = 'A'

    print("\n=== Hasil Algoritma Pencarian Graf ===")
    
    # DFS Rekursif
    hasil_dfs_rekursif = graf.dfs_rekursif(simpul_awal)
    print(f"DFS (rekursif) mulai dari '{simpul_awal}':")
    print(f"Urutan kunjungan: {' -> '.join(hasil_dfs_rekursif)}")
    
    # DFS Iteratif
    hasil_dfs_iteratif = graf.dfs_iteratif(simpul_awal)
    print(f"\nDFS (iteratif) mulai dari '{simpul_awal}':")
    print(f"Urutan kunjungan: {' -> '.join(hasil_dfs_iteratif)}")
    
    # BFS
    hasil_bfs = graf.bfs(simpul_awal)
    print(f"\nBFS mulai dari '{simpul_awal}':")
    print(f"Urutan kunjungan: {' -> '.join(hasil_bfs)}")