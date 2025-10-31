# Anchor Ders Sitesi
## Python-DJango 
Bu proje django ile bir eğitim sitesi veya tasarım,admin ve içerik yüklenme projesidir.

## Amaç
```
Projede amaç django ile olası bir eğitim sitesi yapımını saplamaktır.
Ve proje tamamen bitmemiş haldedir. Lütfen bu uyarıları ele alarak inceleyiniz !
```
[![image](https://www.linkpicture.com/q/anchor_1.png)](https://www.linkpicture.com/view.php?img=LPic60d1d02e26eee949621512)

## İnstallation
Aşağıdaki linki clone yaparak bilgisayarınızda kodları inceleyebilir,çalıştırabilirsiniz.
```
https://github.com/mekroket/Anchor.git
```

### Ortam Değişkenleri (Environment Variables)
Güvenlik için, hassas bilgiler ortam değişkenlerinde saklanır. Başlamak için:

1. `.env.example` dosyasını `.env` olarak kopyalayın:
```bash
cp .env.example .env
```

2. `.env` dosyasını düzenleyerek kendi SECRET_KEY'inizi ekleyin:
```bash
# Yeni bir secret key oluşturmak için:
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

3. Oluşan anahtarı `.env` dosyasına ekleyin:
```
SECRET_KEY=your-generated-secret-key-here
```
## Usage
Proje içerisinde çok fazla eklenti olduğu için bilgisayarınıza gerekli modülleri yüklemeniz gerekmekte.

```
pip install ckeditor4
pip install django-crispy-forms
-----------------------------------
python manage.py runserver
````


## License

[MIT](https://choosealicense.com/licenses/mit/)
