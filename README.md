# Flask Gallery
Website gallery sederhana dengan fitur upload dan delete gambar dengan menggunakan framework flask.

## Requirements
Flask==2.3.2

## Instalasi dengan Docker
- Clone repository
- Masuk ke directory project
- Build docker image

	```docker build -t <nama-image> .```

- Jalankan docker container dengan image yang sudah dibuat

	```docker run --name <nama-container> -d -p 5000:5000 <nama-image>```

## Instalasi dengan Python Virtual Enviroment
- Clone repository
- Masuk ke directory project
- Buat python virtual env baru

	```python3.9 -m venv venv```

- Jalankan virtual env

	```source venv/bin/activate```

- Install semua requirements pada virtual enviroment

	```python3.9 -m pip install -r requirements.txt```

- Masuk folder app

	```cd app```

- Jalankan aplikasi dengan perintah

	```flask --app app.py run --host=0.0.0.0```