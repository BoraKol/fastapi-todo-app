## 🗒️ FastAPI Todo App 
FastAPI Todo App , JSON şemalarında todo listesini dict(sözlük) olarak tutarak , temel CRUD işlemlerini web server aracılığıyla gerçekleştirmenizi sağlar.

## 🚀 Özellikler

- ✅ Yeni görev ekleme  
- 📄 Tüm görevleri listeleme  
- 🔍 ID'ye göre görev görüntüleme  
- ✏️ Görev güncelleme  
- ❌ Görev silme  

## 🛠️ Kullanılan Teknolojiler
* FastAPI
* Python 3.1.x
* Pydantic

## ⚙️ Kurulum ve Çalıştırma
Terminalde gerekli paketlerin kurulumu :
pip install fastapi uvicorn

Uygulamayı web serverda çalıştırmak için : 
uvicorn todo_app(.py dosyanızın ismi):app --reload
