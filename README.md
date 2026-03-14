# BONZ STORE - Fixed Registration OTP

## ✅ SMTP Fixed - pass_set: True

**Local Setup:**
```
# 1. Gmail App Password: Account → Security → App passwords → Generate
# 2. Copy .env.example → .env → paste your SMTP_PASS
cp .env.example .env
```

**PowerShell Test (Windows):**
```powershell
Invoke-RestMethod -Uri "http://localhost:8002/api/test-smtp" -Method POST -ContentType "application/json" -Body '{"to_email":"test@gmail.com"}'
```

**Expected:**
```
[SMTP] pass_set: True
[SMTP] ✅ Email sent successfully
```

## 🚀 Quick Start
```bash
pip install -r requirements.txt
python app.py
```
Visit: http://localhost:8002/register

## Deploy Railway
```
Railway → New Project → Deploy → Variables → SMTP_USER + SMTP_PASS
```

**Registration now sends REAL OTP emails!** 🎉

