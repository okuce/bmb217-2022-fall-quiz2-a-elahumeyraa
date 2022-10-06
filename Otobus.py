"""
Ela Hümeyra Hacıçavuşoğlu 2020717050 A grubu
"""

class Otobus:
    """Otobus bilet satis takip sinifi"""
    plaka=""
    nerden=""
    nereye=""
    _koltuk_sayisi=0

    def __init__(self,plaka,nerden,nereye,_koltuk_sayisi):
        self.plaka=plaka
        self.nerden=nerden
        self.nereye=nereye
        self._koltuk_sayisi=_koltuk_sayisi
    
    def bilet_sat(self):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        satislar = self._koltuk_sayisi-1
        dolu_koltuk=satislar
        return dolu_koltuk

    def bilet_iade(self):
        """Otobusteki dolu koltuk sayisini 1 azaltir"""
        iadeler= self._koltuk_sayisi + 1
        bos_koltuk=iadeler
        return bos_koltuk

    def durum_yaz(self):
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""
        print("{}, {}, {}, {}, {}".format(self.nerden,self.nereye,self.plaka,self.bilet_iade(),self.bilet_sat()))
