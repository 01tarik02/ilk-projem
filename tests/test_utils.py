import unittest
import sys
import os

# src klasörünü Python'un modül yoluna ekliyoruz ki fonksiyonumuzu bulabilsin
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils import karsilama_mesaji

class TestUtils(unittest.TestCase):
    
    def test_karsilama_mesaji(self):
        # Test verisi hazırlıyoruz
        isim = "Tarik"
        sonuc = karsilama_mesaji(isim)
        
        # Beklenen çıktı
        beklenen = "Merhaba, Tarik! Moduler mimari projesine hos geldin."
        
        # Sonucun beklenenle eşleşip eşleşmediğini test ediyoruz
        self.assertEqual(sonuc, beklenen)

if __name__ == '__main__':
    unittest.main()
    