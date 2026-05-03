# Veri klasörü

## Veri seti

ULB / Kaggle üzerinde yayınlanan **Credit Card Fraud Detection** veri seti kullanılır. Özellikler PCA ile dönüştürülmüş sayısal sütunlardır (`Time`, `Amount`, `V1`–`V28`); hedef sütun genelde `Class` (0: meşru, 1: dolandırıcılık).

- Kaggle: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud  
- Orijinal makale ve bağlam için Kaggle sayfasındaki açıklamalara bakın.

## Yerel kurulum

1. `creditcard.csv` dosyasını indirin.
2. Bu klasöre kopyalayın: `data/creditcard.csv`  
   Kodda varsayılan yol: `src/fraud_detection/paths.py` içindeki `DEFAULT_DATA_PATH`.

## Gizlilik ve boyut

- Veri seti gerçek işlemlerden türetilmiş ancak **kimlik doğrudan içermez**; yine de kurum politikalarına göre saklama ve paylaşım kurallarına uyun.
- Dosya boyutu yüzlerce MB olabilir; Git’e eklemeyin (`.gitignore` zaten `data/*.csv` dışlar).
