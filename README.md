# 🎯 GoLike TikTok Auto Tool Pro

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.0-orange.svg)](https://github.com/doanht4655/Goli4848848484)

> **Công cụ tự động hóa Follow/Like TikTok cho GoLike với giao diện Pro và hiệu suất cao**

## ✨ Tính Năng Nổi Bật

### 🚀 **Tính Năng Chính**
- 🎯 **Auto Follow TikTok** - Tự động follow người dùng TikTok
- ❤️ **Auto Like TikTok** - Tự động like video TikTok  
- 🔄 **Retry Mechanism** - Thử lại thông minh khi gặp lỗi
- 🛡️ **Error Handling** - Xử lý lỗi tự động và thông minh
- 📊 **Real-time Stats** - Thống kê hoạt động theo thời gian thực

### 🎨 **Giao Diện Pro**
- ⚡ **UI/UX Modern** - Giao diện đẹp mắt, dễ sử dụng
- 🌈 **Gradient Colors** - Hiệu ứng màu sắc gradient
- 🎭 **Animations** - Hiệu ứng animation mượt mà
- 📱 **Responsive Design** - Tương thích mọi terminal
- 🚫 **No Logging** - Không tạo file log rườm rà

### ⚙️ **Tối Ưu Hiệu Suất**
- 🔧 **Smart Configuration** - Cấu hình thông minh
- 🔄 **Auto Account Switch** - Tự động đổi tài khoản khi cần
- ⏰ **Flexible Timing** - Thời gian chờ linh hoạt
- 🎯 **Job Type Selection** - Chọn loại nhiệm vụ tùy ý

## 📋 Yêu Cầu Hệ Thống

- **Python 3.7+**
- **Termux** (Android) hoặc **Linux/Windows**
- **Kết nối Internet ổn định**
- **Tài khoản GoLike** đã đăng ký

## 🔧 Cài Đặt

### 1. Clone Repository
```bash
git clone https://github.com/doanht4655/Goli4848848484.git
cd Goli4848848484
```

### 2. Cài Đặt Dependencies
```bash
pip install requests pytz
```

### 3. Chạy Tool
```bash
python golikevipdoanh.py
```

## 📖 Hướng Dẫn Sử Dụng

### 🔑 **Lấy Authorization Token**

1. Truy cập [app.golike.net](https://app.golike.net)
2. Đăng nhập tài khoản
3. Mở **Developer Tools** (F12)
4. Vào tab **Network**
5. Refresh trang (F5)
6. Tìm request có chứa **Authorization**
7. Copy giá trị **Authorization** (bắt đầu bằng `Bearer`)

### 🎮 **Sử Dụng Tool**

1. **Khởi động tool:**
   ```bash
   python golikevipdoanh.py
   ```

2. **Chọn menu:**
   - `1` - Bắt đầu Tool TikTok Auto
   - `2` - Xóa Authorization hiện tại
   - `3` - Thông tin hệ thống
   - `4` - Tính năng của tool
   - `0` - Thoát tool

3. **Nhập Authorization** khi được yêu cầu

4. **Chọn tài khoản TikTok** từ danh sách

5. **Cấu hình tool:**
   - Thời gian chờ mỗi job (5-300 giây)
   - Retry khi thất bại (y/n)
   - Số job thất bại để đổi tài khoản
   - Loại nhiệm vụ (Follow/Like/Cả hai)

6. **Theo dõi hoạt động** trên bảng thống kê real-time

## 🎯 Cấu Hình Tùy Chỉnh

### ⏰ **Thời Gian Chờ**
- **Tối thiểu:** 5 giây
- **Tối đa:** 300 giây (5 phút)
- **Khuyến nghị:** 15-30 giây

### 🔄 **Retry Settings**
- **Số lần thử:** Tối đa 3 lần
- **Timeout:** 15 giây
- **Delay:** 2-5 giây giữa các lần thử

### 📊 **Job Types**
- **Follow Only** - Chỉ làm nhiệm vụ Follow
- **Like Only** - Chỉ làm nhiệm vụ Like
- **Both** - Làm cả Follow và Like

## 📊 Thống Kê & Theo Dõi

Tool hiển thị bảng thống kê real-time với các thông tin:

| Cột | Mô Tả |
|-----|-------|
| **STT** | Số thứ tự job |
| **Thời gian** | Thời gian hoàn thành |
| **Trạng thái** | Thành công/Thất bại |
| **Loại** | Follow/Like |
| **Xu** | Số xu nhận được |
| **Tổng** | Tổng xu tích lũy |
| **Streak** | Số job thành công liên tiếp |

## 🛡️ Bảo Mật & An Toàn

- ✅ **Không lưu trữ dữ liệu nhạy cảm**
- ✅ **Không tạo file log**
- ✅ **Authorization được mã hóa cục bộ**
- ✅ **Tuân thủ rate limit của API**
- ✅ **Xử lý lỗi an toàn**

## 🔧 Khắc Phục Sự Cố

### ❌ **Lỗi Authorization (HTTP 403)**
- Kiểm tra lại Authorization token
- Đảm bảo token còn hiệu lực
- Thử đăng nhập lại GoLike

### 🌐 **Lỗi Kết Nối**
- Kiểm tra kết nối Internet
- Thử chờ một lúc rồi chạy lại
- Kiểm tra tường lửa/proxy

### ⏰ **Timeout Errors**
- Tăng thời gian timeout
- Kiểm tra tốc độ mạng
- Thử vào giờ ít traffic

## 🎨 Screenshots

### 🖥️ **Banner & Menu**
```
╔══════════════════════════════════════════════════════════════╗
║           🎯 GOLIKE TIKTOK AUTO TOOL PRO 🎯                  ║
╚══════════════════════════════════════════════════════════════╝

┌─────────────────── 🎮 MENU CHÍNH 🎮 ───────────────────┐
│  1️⃣ 🚀 Bắt đầu Tool TikTok Auto                        │
│  2️⃣ 🗑️ Xóa Authorization hiện tại                     │
│  3️⃣ 💻 Thông tin hệ thống                              │
│  4️⃣ 🔥 Tính năng của tool                              │
│  0️⃣ 👋 Thoát tool                                      │
└─────────────────────────────────────────────────────────┘
```

### 📊 **Bảng Thống Kê**
```
┌──────────── 📊 TRẠNG THÁI HOẠT ĐỘNG REAL-TIME 📊 ────────────┐
│ STT │   Thời gian   │ Trạng thái  │ Loại  │  Xu  │ Tổng │ Streak │
├─────┼───────────────┼─────────────┼────────┼──────┼──────┼────────┤
│   1 │ 14:32:15     │ ✅ Thành công │ follow │ +15  │  15  │   1    │
│   2 │ 14:32:45     │ ✅ Thành công │ like   │ +10  │  25  │   2    │
└─────────────────────────────────────────────────────────────────┘
```

## 👨‍💻 Thông Tin Developer

- **👤 Developer:** Trần Đức Doanh (Bóng X)
- **📱 TikTok:** [@doanh21105](https://tiktok.com/@doanh21105)
- **📞 Zalo:** 0865526740
- **📧 Telegram:** [https://t.me/doanhvip1](https://t.me/doanhvip1)
- **🔄 Version:** 3.0 (Pro Enhanced)
- **📅 Updated:** 03/08/2025

## 📄 License

Dự án này được phân phối dưới giấy phép [MIT License](LICENSE).

## 🤝 Đóng Góp

Chúng tôi hoan nghênh mọi đóng góp! Vui lòng:

1. Fork dự án
2. Tạo feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

## ⭐ Support

Nếu tool hữu ích, hãy cho chúng tôi một ⭐ trên GitHub!

## 📞 Liên Hệ Hỗ Trợ

- 🐛 **Bug Reports:** [Issues](https://github.com/doanht4655/Goli4848848484/issues)
- 💡 **Feature Requests:** [Issues](https://github.com/doanht4655/Goli4848848484/issues)
- 📧 **Direct Contact:** [Telegram](https://t.me/doanhvip1)

---

<div align="center">

**🎯 Made with ❤️ by Trần Đức Doanh (Bóng X)**

[![GitHub followers](https://img.shields.io/github/followers/doanht4655?style=social)](https://github.com/doanht4655)
[![GitHub stars](https://img.shields.io/github/stars/doanht4655/Goli4848848484?style=social)](https://github.com/doanht4655/Goli4848848484)

</div>
