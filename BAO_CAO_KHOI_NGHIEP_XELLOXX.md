1. TỔNG QUAN DỰ ÁN

Tên dự án: Xelloxx Shop

Loại hình: Chợ trực tuyến (Marketplace) chuyên bán các sản phẩm kỹ thuật số như Bot, API, Source Code và các công cụ tự động.

Ngày phát triển: 2024
Dữ liệu cơ sở dữ liệu: từ 02/2026 (dữ liệu thử nghiệm).

Công nghệ sử dụng:

Backend: Flask (Python)

Cơ sở dữ liệu: JSON

Thanh toán: API MB Bank

Xác thực Email: SMTP Gmail (OTP)

Triển khai: Railway

URL Demo:

Local: http://localhost:8002

Production: Railway (cấu hình trong railway.toml)

Triển khai hệ thống:

Railway

Procfile + Gunicorn

Nixpacks tự động build

Người sáng lập / lập trình: xellox
(Số dư hiện tại: 960.000 xu)

Sứ mệnh

Cung cấp các bot và source code chất lượng cao cho cộng đồng developer và marketer tại Việt Nam với giá rẻ (khoảng 8.000 – 15.000 xu / sản phẩm), hỗ trợ thanh toán ví điện tử tự động.

2. SẢN PHẨM & DỊCH VỤ
Danh mục sản phẩm (6 loại)

Bot Zalo

Bot Facebook

Bot Discord

API

Source Code

Tool

Các sản phẩm hiện tại (database.json – 3 sản phẩm)
ID	Tên sản phẩm	Giá	Khuyến mãi	Danh mục	Lượt xem	Đánh giá
2f5b...	Quản lý nhóm Zalo	10.000 xu	Không	Bot Zalo	16	5★ (1)
b995...	Bot Facebook Auto Like/Comment	15.000 → 12.000 xu	Giảm 20%	Bot Facebook	45	4.8★ (12)
7aef...	Discord Auto Bump	8.000 xu	Không	Bot Discord	23	4.5★ (7)
Hình thức giao file

File được cung cấp qua:

MediaFire

Google Drive

Sau khi mua, hệ thống tự tạo:

License key dạng: BONZ-XXXX

Token tải file có thời hạn: 1 giờ (TTL = 1h)

3. TỔNG QUAN CHỨC NĂNG WEBSITE
3.1 Các trang chính của website (templates)
index.html
Trang chủ gồm:
- Banner giới thiệu
- Đếm ngược flash sale
- Danh sách sản phẩm
- Bộ lọc và tìm kiếm
- Thống kê thời gian thực
- Carousel đánh giá người dùng

register.html
- Đăng ký tài khoản
- Xác thực OTP qua email

login.html
- Đăng nhập bằng username/password
- Mật khẩu được mã hóa SHA256

profile.html
- Chỉnh sửa thông tin
- Đổi avatar
- Đổi mật khẩu
- Xem số dư
- Xem mã giới thiệu

orders.html
- Lịch sử mua hàng
- Link tải file (token có hạn 1 giờ)

cart.html
- Giỏ hàng (hỗ trợ nhiều sản phẩm)

checkout.html
- Áp dụng mã giảm giá
- Tính tổng tiền
- Mua hàng nhanh

topup.html
- Tạo mã nạp tiền
- Hiển thị thông tin chuyển khoản MB Bank
- Lịch sử nạp

notifications.html
- Thông báo hệ thống
- Thông báo thành công/thất bại
- Thông báo nạp tiền

referral.html
- Chia sẻ link giới thiệu
- Theo dõi thu nhập từ giới thiệu

product.html
- Trang chi tiết sản phẩm
- Nút mua
- Danh sách đánh giá

admin.html
- Dashboard quản trị
- CRUD toàn bộ dữ liệu
- Test MB Bank

invoice.html
- Hóa đơn chuẩn PDF
- Có thể chỉnh thông tin shop

Các trang khác:
error.html
base.html (giao diện dark mode responsive)
3.2 API Backend chính (app.py)
API dành cho người dùng

(Yêu cầu đăng nhập)

GET /api/me
Lấy thông tin người dùng:
- Số dư
- Thông báo chưa đọc
- Hồ sơ cá nhân

GET /api/products
Danh sách sản phẩm + tìm kiếm + lọc

GET /api/cart
Danh sách sản phẩm trong giỏ hàng

POST /api/cart/add
Thêm vào giỏ

POST /api/cart/remove
Xóa khỏi giỏ

POST /api/cart/clear
Xóa toàn bộ giỏ

POST /api/checkout
Thanh toán:
- Trừ xu
- Tạo license
- Xóa giỏ

GET /api/my-orders
Lịch sử đơn hàng + token tải file

POST /api/topup/create
Tạo mã nạp tiền (tối thiểu 10k)

GET /api/topup/history
Lịch sử nạp

GET /api/topup/status
Trạng thái nạp tiền

POST /api/reviews
Thêm / sửa / xóa đánh giá

GET /api/notifications
Danh sách thông báo

GET /api/referral/info
Thông tin giới thiệu
- Link
- Thu nhập
- Số người đã giới thiệu
API dành cho Admin
POST /api/admin/products
Thêm / sửa / xóa sản phẩm

POST /api/admin/users/{id}/balance
Điều chỉnh số dư người dùng

POST /api/admin/topup-requests/{id}/approve
Duyệt nạp tiền

POST /api/admin/topup-requests/{id}/reject
Từ chối nạp tiền

POST /api/admin/mb-settings
Cấu hình tài khoản MB Bank

POST /api/admin/upload/image
Upload ảnh (tối đa 10MB)

POST /api/admin/upload/file
Upload file (tối đa 200MB)

POST /api/admin/notify
Gửi thông báo cho toàn bộ user

GET /api/admin/stats
Thống kê hệ thống
API công khai
/api/stats
Thống kê:
- số sản phẩm
- số người dùng
- số đơn hàng

/api/categories
Danh sách danh mục

/api/products/best-sellers
Sản phẩm bán chạy

/api/coupon/check
Kiểm tra mã giảm giá
3.3 Logic Backend chính
Rate Limiting

Giới hạn request:

decorator(key_prefix, max_calls, window)

Ví dụ: OTP chỉ gửi 3 lần / 5 phút

Cơ sở dữ liệu

Sử dụng JSON:

load_db()
save_db()

Lưu dữ liệu dạng atomic.

OTP Email

OTP 6 chữ số

Lưu trong _otp_store

Sử dụng threading.Lock() để tránh race condition.

Thanh toán MB Bank

Thread daemon kiểm tra giao dịch mỗi 15 giây

Dùng thư viện mbbank-lib

Chức năng:

getBalance()
transactions()
License Key

Sau khi mua:

BONZ-XXXXX

Lưu trong bảng license_keys.

Bảo mật

Token tải file: HMAC

TTL: 1 giờ

Hash mật khẩu: SHA256

Upload

Cho phép:

ALLOWED_IMAGES
ALLOWED_FILES

Upload bằng:

secure_filename

Lưu:

Local

Cloudinary (tùy chọn)

Thông báo
push_notification()

Giới hạn tối đa 200 thông báo / user

Hệ thống giới thiệu

Phần thưởng:

Đăng ký: +10.000 xu
Nạp tiền: +5%
4. THỐNG KÊ HỆ THỐNG
Sản phẩm (3)

Quản lý nhóm Zalo
Giá: 10k xu
Lượt xem: 16

Bot Facebook Auto
Giá: 15k → 12k
Lượt xem: 45
Đánh giá: 4.8★

Discord Bump
Giá: 8k xu
Lượt xem: 23

Người dùng (4)
xellox
- Số dư: 960k xu
- 4 đơn hàng
- SĐT: 0967427517

Raichin
xellox1 (mã giới thiệu 10k)
xellox2
Đơn hàng

Tổng: 5 đơn (~50k xu)

Ví dụ:

99b4df9a
xellox mua Bot Zalo (10k)

3f3adf72
raichontui mua Bot Zalo (10k)
Nạp tiền

Tổng: 3 giao dịch

2 pending: 500k
1 completed: 10k
Đánh giá
1 review
5 sao
Nội dung: "siuuu"
MB Bank
Tài khoản: 0967427517
Tên: HO NHAT TRUONG

Đã xử lý: 11 giao dịch

API Thống kê
/api/stats
products = 3
users = 4
orders = 5
5. MÔ HÌNH KINH DOANH
Quy đổi tiền
1 xu = 1 VND

Giá trung bình sản phẩm:

11.000 xu
Ví dụ đơn hàng

Bot FB giảm giá 20%

15.000 → 12.000 xu
Doanh thu thực: 9.600 xu
Nguồn doanh thu

Bán sản phẩm trực tiếp (70%)

Hệ thống giới thiệu (20%)

Phí nạp tiền tương lai (5%)

Dự đoán tài chính năm 1
1.000 người dùng
50 đơn / ngày
ARPU = 50.000 xu

Doanh thu:

1.5 triệu VND / tháng
18 triệu VND / năm

Lợi nhuận: ~95%

Chi phí vận hành

Hosting: Railway (gói miễn phí)
Thanh toán: MB Bank (miễn phí)
Email: Gmail (miễn phí)

6. PHÂN TÍCH SWOT
Điểm mạnh

MVP hoàn chỉnh

Thanh toán MB tự động

Chi phí vận hành gần như 0

Điểm yếu

Chỉ có 3 sản phẩm

Database JSON khó mở rộng

Cơ hội

Thị trường bot Việt Nam đang phát triển

Affiliate marketing

Rủi ro

Cạnh tranh từ ToolVN

Gian lận thanh toán

LỘ TRÌNH PHÁT TRIỂN
Quý 1

50 sản phẩm

Quảng cáo Facebook

100.000 người dùng

Quý 2

Tích hợp MoMo / VNPay

Phát triển ứng dụng Android

Quý 3

100.000 người dùng

Doanh thu 100 triệu / tháng

Quý 4

Chuẩn bị gọi vốn / IPO

Gọi vốn
500 triệu VND

Dùng cho:

Marketing

Phát triển sản phẩm

Mục tiêu:

10x lợi nhuận năm 2

Nguồn: Phân tích từ code (app.py, templates, database.json)

Chạy demo:

python app.py