# Kredi kartı dolandırıcılığı tespiti

European cardholder işlemlerine dayalı, aşırı dengesiz sınıflı bir ikili sınıflandırma problemi. Bu repoda **ham veri dosyası tutulmaz**; veriyi yerelde `data/` altına indirirsiniz (aşağıdaki talimatlar).

## Klasör yapısı

| Yol | Açıklama |
|-----|----------|
| `data/` | Yerel veri (`creditcard.csv`); `.gitignore` ile CSV dışlanır |
| `notebooks/` | Jupyter not defterleri (EDA, model denemeleri) |
| `src/fraud_detection/` | Tekrar kullanılan yardımcı kod (yollar, ileride yükleme ve model) |
| `reports/` | İleride dışa aktarılan figürler (PNG/PDF git dışı; klasör `.gitkeep` ile takip edilir) |
| `artifacts/` | İleride model veya ara çıktılar (git dışı) |

## Ortam kurulumu

```powershell
cd "c:\Users\Dgkn0\cursorprojects\Credit_Card_Fraud _Detection"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Not defterlerinden `fraud_detection` paketini kullanmak için proje kökünde:

```powershell
$env:PYTHONPATH = "src"
jupyter lab
```

İleride `pyproject.toml` ile düzenlenebilir kurulum eklenebilir.

## Yol haritası (milestones)

- **M0 (şu an)**: İskelet, bağımlılıklar, veri talimatları, EDA not defteri iskeleti
- **M1**: Keşifsel veri analizi (EDA) tamamlama
- **M2**: Ön işleme ve `src` modüllerinin genişletilmesi
- **M3**: Baseline model ve metrikler (ROC-AUC, precision-recall, confusion matrix)
- **M4**: Sınıf dengesizliği stratejileri (ör. SMOTE, sınıf ağırlıkları)

## Önerilen commit sırası

1. `chore: initial project skeleton`
2. `docs: add README and data instructions`
3. `feat: add EDA notebook scaffold`
