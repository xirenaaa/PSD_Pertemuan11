class Node:

    def __init__(self, nilai):
        self.nilai = nilai
        self.kiri = None
        self.kanan = None

class BinarySearchTree:
    """
    Kelas Binary Search Tree untuk menyimpan dan mengelola data dalam struktur pohon biner.
    Aturan BST: nilai di kiri selalu lebih kecil dari node induk, 
    nilai di kanan selalu lebih besar dari node induk.
    """
    def __init__(self):
        """Membuat BST kosong"""
        self.akar = None
    
    def tambah(self, nilai):
        """
        Menambahkan nilai baru ke dalam BST.
        Jika BST kosong, nilai menjadi akar.
        Jika tidak, nilai ditambahkan sesuai aturan BST.
        
        :param nilai: Nilai yang akan ditambahkan ke BST
        """
        if self.akar is None:
            self.akar = Node(nilai)
            return
        
        self._tambah_rekursif(self.akar, nilai)
    
    def _tambah_rekursif(self, node_saat_ini, nilai):
        """
        Fungsi bantuan rekursif untuk menambahkan nilai ke BST.
        
        :param node_saat_ini: Node saat ini yang sedang diperiksa
        :param nilai: Nilai yang akan ditambahkan
        """
        if nilai == node_saat_ini.nilai:
            return
        
        if nilai < node_saat_ini.nilai:
            if node_saat_ini.kiri is None:
                node_saat_ini.kiri = Node(nilai)
            else:
                self._tambah_rekursif(node_saat_ini.kiri, nilai)

        else:
            if node_saat_ini.kanan is None:
                node_saat_ini.kanan = Node(nilai)
            else:
                self._tambah_rekursif(node_saat_ini.kanan, nilai)
    
    def cari(self, nilai):
        """
        Mencari nilai tertentu dalam BST.
        
        :param nilai: Nilai yang dicari
        :return: Node yang berisi nilai jika ditemukan, None jika tidak ditemukan
        """
        return self._cari_rekursif(self.akar, nilai)
    
    def _cari_rekursif(self, node_saat_ini, nilai):
        """
        Fungsi bantuan rekursif untuk mencari nilai dalam BST.
        
        :param node_saat_ini: Node saat ini yang sedang diperiksa
        :param nilai: Nilai yang dicari
        :return: Node yang berisi nilai jika ditemukan, None jika tidak ditemukan
        """
        if node_saat_ini is None or node_saat_ini.nilai == nilai:
            return node_saat_ini
        
        if nilai < node_saat_ini.nilai:
            return self._cari_rekursif(node_saat_ini.kiri, nilai)
        
        return self._cari_rekursif(node_saat_ini.kanan, nilai)
    
    def cari_minimum(self):
        """
        Menemukan nilai terkecil dalam BST.
        Dalam BST, nilai terkecil selalu berada di subtree kiri terdalam.
        
        :return: Nilai terkecil dalam BST, None jika BST kosong
        """
        if self.akar is None:
            return None
        
        node_saat_ini = self.akar
        while node_saat_ini.kiri:
            node_saat_ini = node_saat_ini.kiri
        
        return node_saat_ini.nilai
    
    def cari_maksimum(self):
        """
        Menemukan nilai terbesar dalam BST.
        Dalam BST, nilai terbesar selalu berada di subtree kanan terdalam.
        
        :return: Nilai terbesar dalam BST, None jika BST kosong
        """
        if self.akar is None:
            return None
        
        node_saat_ini = self.akar
        while node_saat_ini.kanan:
            node_saat_ini = node_saat_ini.kanan
        
        return node_saat_ini.nilai
    
    def traversal_inorder(self):
        """
        Melakukan traversal inorder (Kiri-Akar-Kanan).
        Traversal inorder pada BST akan menghasilkan nilai terurut dari kecil ke besar.
        
        :return: List berisi hasil traversal inorder
        """
        hasil = []
        self._inorder_rekursif(self.akar, hasil)
        return hasil
    
    def _inorder_rekursif(self, node_saat_ini, hasil):
        """
        Fungsi bantuan rekursif untuk traversal inorder.
        
        :param node_saat_ini: Node saat ini yang sedang ditraversal
        :param hasil: List untuk menyimpan hasil traversal
        """
        if node_saat_ini:
            self._inorder_rekursif(node_saat_ini.kiri, hasil)
            hasil.append(node_saat_ini.nilai)
            self._inorder_rekursif(node_saat_ini.kanan, hasil)
    
    def traversal_preorder(self):
        """
        Melakukan traversal preorder (Akar-Kiri-Kanan).
        
        :return: List berisi hasil traversal preorder
        """
        hasil = []
        self._preorder_rekursif(self.akar, hasil)
        return hasil
    
    def _preorder_rekursif(self, node_saat_ini, hasil):
        """
        Fungsi bantuan rekursif untuk traversal preorder.
        
        :param node_saat_ini: Node saat ini yang sedang ditraversal
        :param hasil: List untuk menyimpan hasil traversal
        """
        if node_saat_ini:
            hasil.append(node_saat_ini.nilai)
            self._preorder_rekursif(node_saat_ini.kiri, hasil)
            self._preorder_rekursif(node_saat_ini.kanan, hasil)
    
    def traversal_postorder(self):
        """
        Melakukan traversal postorder (Kiri-Kanan-Akar).
        
        :return: List berisi hasil traversal postorder
        """
        hasil = []
        self._postorder_rekursif(self.akar, hasil)
        return hasil
    
    def _postorder_rekursif(self, node_saat_ini, hasil):
        """
        Fungsi bantuan rekursif untuk traversal postorder.
        
        :param node_saat_ini: Node saat ini yang sedang ditraversal
        :param hasil: List untuk menyimpan hasil traversal
        """
        if node_saat_ini:

            self._postorder_rekursif(node_saat_ini.kiri, hasil)
            self._postorder_rekursif(node_saat_ini.kanan, hasil)
            hasil.append(node_saat_ini.nilai)

if __name__ == "__main__":
    pohon_bst = BinarySearchTree()
    
    nilai_nilai = [50, 30, 70, 20, 40, 60, 80, 100]
    print("Memasukkan nilai:", nilai_nilai)
    
    for nilai in nilai_nilai:
        pohon_bst.tambah(nilai)
    
    
    # Mencari nilai
    nilai_cari_1 = 40
    nilai_cari_2 = 90
    print(f"Mencari nilai {nilai_cari_1}:", "Ditemukan" if pohon_bst.cari(nilai_cari_1) else "Tidak ditemukan")
    print(f"Mencari nilai {nilai_cari_2}:", "Ditemukan" if pohon_bst.cari(nilai_cari_2) else "Tidak ditemukan")
    
    # Menampilkan nilai terkecil dan terbesar
    print("Nilai terkecil:", pohon_bst.cari_minimum())
    print("Nilai terbesar:", pohon_bst.cari_maksimum())
    
    # Menampilkan hasil traversal
    print("\nHasil traversal:")
    print("Inorder traversal  :", pohon_bst.traversal_inorder(), "- (Menghasilkan data terurut)")
    print("Preorder traversal :", pohon_bst.traversal_preorder())
    print("Postorder traversal:", pohon_bst.traversal_postorder())