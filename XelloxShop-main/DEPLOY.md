# 🚀 Deploy Xellox Shop lên Railway

## Bước 1 — Chuẩn bị

1. Đăng ký tài khoản tại [railway.com](https://railway.com)
2. Cài Railway CLI (tuỳ chọn):
   ```bash
   npm install -g @railway/cli
   railway login
   ```

---

## Bước 2 — Tạo project trên Railway

### Cách A: Qua GitHub (khuyên dùng)
1. Push code lên GitHub repository
2. Vào Railway → **New Project** → **Deploy from GitHub repo**
3. Chọn repository → Railway tự động build và deploy

### Cách B: Qua CLI
```bash
cd xellox
railway init
railway up
```

---

## Bước 3 — Cấu hình Variables (BẮT BUỘC)

Vào **Railway project** → **Variables** → thêm các biến sau:

| Biến | Giá trị | Bắt buộc |
|------|---------|----------|
| `SECRET_KEY` | Chuỗi random ≥32 ký tự | ✅ |
| `SMTP_USER` | Gmail của bạn | ✅ |
| `SMTP_PASS` | Gmail App Password | ✅ |
| `SHOP_NAME` | Tên shop | ✅ |
| `CLOUDINARY_URL` | URL từ Cloudinary | ⭐ Khuyên dùng |
| `MB_USERNAME` | Tài khoản MBBank | ❌ Tuỳ chọn |
| `MB_PASSWORD` | Mật khẩu MBBank | ❌ Tuỳ chọn |

> **Tạo Gmail App Password:**  
> Vào [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords) → chọn "Mail" → copy mật khẩu 16 ký tự

---

## Bước 4 — Thêm Volume (lưu database & uploads)

> ⚠️ Railway filesystem **reset khi redeploy** — cần Volume để giữ dữ liệu!

1. Vào project → **Add Service** → **Volume**
2. Mount path: `/data`
3. Thêm 2 Variables:
   ```
   DATA_DIR=/data
   UPLOAD_DIR=/data/uploads
   ```

**Hoặc** dùng [Cloudinary](https://cloudinary.com) để lưu file (miễn phí 25GB):
- Đăng ký → Dashboard → copy `CLOUDINARY_URL`
- Thêm vào Railway Variables

---

## Bước 5 — Kiểm tra

Sau khi deploy, Railway cấp domain dạng `xxx.railway.app`.

Kiểm tra app đang chạy:
```
https://your-app.railway.app/api/stats
```

---

## ⚠️ Lưu ý quan trọng

- **Xoá** `SMTP_PASS` và `SECRET_KEY` khỏi code trước khi push GitHub
- Không commit file `.env` (đã có trong `.gitignore`)
- File `database.json` nếu push lên GitHub sẽ là data khởi tạo — Railway sẽ copy vào Volume lần đầu
