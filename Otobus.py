"""
Ela Hümeyra Hacıçavuşoğlu 2020717050 A grubu
"""

class Otobus:
    """Otobus bilet satis takip sinifi"""
    plaka:str=""
    nerden:str=""
    nereye:str=""
    koltuk_sayisi:int=0
    _dolu_koltuk_sayisi:int=0


    def __init__(self,plaka,nerden,nereye,koltuk_sayisi) -> None:
        """Constructor method

        Args:
            plaka otobüs plakası
            nerden güzargah başlangıç noktası
            nereye güzargah bitiş noktası
            koltuk sayısı otobüste yer alan koltuk sayısı
        """
        self.plaka=plaka
        self.nerden=nerden
        self.nereye=nereye
        self.koltuk_sayisi=koltuk_sayisi
    
    def bilet_sat(self):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        if self._dolu_koltuk_sayisi<self.koltuk_sayisi:
            self._dolu_koltuk_sayisi += 1

    def bilet_iade(self):
        """Otobusteki dolu koltuk sayisini 1 azaltir"""
        if self._dolu_koltuk_sayisi>0:
            self._dolu_koltuk_sayisi -= 1

    def durum_yaz(self):
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""
        print("{},{},{},{},{}".format(self.nerden,self.nereye,self.plaka,self.koltuk_sayisi,self._dolu_koltuk_sayisi))
