import os
import sys
import time
import json
import requests
import threading
import random
from urllib.parse import urlparse

# Thiết lập timezone Việt Nam
import pytz
from datetime import datetime
tz = pytz.timezone("Asia/Ho_Chi_Minh")

AUTH_FILE = "Authorization.txt"

# Cấu hình retry và timeout
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 15
RETRY_DELAY = 2

def colored(text, color):
    colors = {
        "yellow": "\033[1;33m",
        "pink": "\033[1;35m",
        "cyan": "\033[1;36m",
        "white": "\033[1;97m",
        "green": "\033[1;32m",
        "red": "\033[1;31m",
        "blue": "\033[1;34m",
        "purple": "\033[1;35m",
        "orange": "\033[1;91m",
        "light_green": "\033[1;92m",
        "light_blue": "\033[1;94m",
        "light_cyan": "\033[1;96m",
        "light_yellow": "\033[1;93m",
        "light_red": "\033[1;91m",
        "light_purple": "\033[1;95m",
        "bold": "\033[1m",
        "underline": "\033[4m",
        "blink": "\033[5m",
        "reverse": "\033[7m",
        "reset": "\033[0m"
    }
    return colors.get(color, "") + text + colors["reset"]

def print_with_animation(text, color="white", animation_time=0.02):
    """In text với hiệu ứng animation"""
    for char in text:
        print(colored(char, color), end='', flush=True)
        time.sleep(animation_time)
    print()

def loading_animation(message="Đang tải", duration=2):
    """Hiệu ứng loading với spinner"""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(colored(f"\r{chars[i % len(chars)]} {message}...", "cyan"), end="", flush=True)
        time.sleep(0.1)
        i += 1
    print(colored(f"\r✅ {message} hoàn tất!{' '*20}", "green"))

def progress_bar(current, total, bar_length=40, prefix="Progress"):
    """Hiển thị thanh progress với gradient"""
    progress = current / total
    filled_length = int(bar_length * progress)
    
    # Tạo gradient cho thanh progress
    filled_chars = []
    for i in range(filled_length):
        if i < filled_length * 0.3:
            filled_chars.append(colored("█", "red"))
        elif i < filled_length * 0.7:
            filled_chars.append(colored("█", "yellow"))
        else:
            filled_chars.append(colored("█", "green"))
    
    empty_chars = colored("▒", "white") * (bar_length - filled_length)
    bar = ''.join(filled_chars) + empty_chars
    percent = progress * 100
    
    return f"{prefix}: |{bar}| {percent:.1f}% ({current}/{total})"

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    
    # Gradient banner với animation
    banner_lines = [
        "╔══════════════════════════════════════════════════════════════╗",
        "║                                                              ║",
        "║  ██████╗  ██████╗ ██╗     ██╗██╗  ██╗███████╗ ⚡            ║",
        "║ ██╔════╝ ██╔═══██╗██║     ██║██║ ██╔╝██╔════╝                ║",
        "║ ██║  ███╗██║   ██║██║     ██║█████╔╝ █████╗   🚀             ║",
        "║ ██║   ██║██║   ██║██║     ██║██╔═██╗ ██╔══╝                  ║",
        "║ ╚██████╔╝╚██████╔╝███████╗██║██║  ██╗███████╗ 💫            ║",
        "║  ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝╚══════╝                ║",
        "║                                                              ║",
        "║           🎯 GOLIKE TIKTOK AUTO TOOL PRO 🎯                  ║",
        "║                                                              ║",
        "╚══════════════════════════════════════════════════════════════╝",
    ]
    
    # Animation với gradient colors
    gradient_colors = ['light_cyan', 'cyan', 'light_blue', 'blue', 'purple', 'light_purple', 'pink']
    for i, line in enumerate(banner_lines):
        color = gradient_colors[i % len(gradient_colors)]
        print(colored(line, color))
        time.sleep(0.08)  # Animation delay
    
    print()
    
    # Thông tin tool với border animation
    info_box = [
        "┌─────────────────── 🔥 THÔNG TIN TOOL 🔥 ──────────────────┐",
        "│ 👨‍💻 Developer : Trần Đức Doanh (Bóng X) - Enhanced      │",
        "│ 📱 TikTok    : @doanh21105                               │",
        "│ 📞 Zalo      : 0865526740                                │",
        "│ 📧 Telegram  : https://t.me/doanhvip1                   │",
        "│ 🔄 Version   : 3.0 (Pro Enhanced)                        │",
        "│ 📅 Updated   : " + datetime.now(tz).strftime("%d/%m/%Y") + " - " + datetime.now(tz).strftime("%H:%M:%S") + "                     │",
        "│ ⭐ Features  : Auto TikTok + Smart UI + No Log           │",
        "└──────────────────────────────────────────────────────────┘"
    ]
    
    for i, line in enumerate(info_box):
        if i == 0 or i == len(info_box) - 1:
            print(colored(line, "yellow"))
        else:
            print(colored(line, "white"))
        time.sleep(0.05)
    
    print()
    
    # Status indicators
    status_indicators = [
        ("🟢", "System Ready", "green"),
        ("🟢", "Network Connected", "green"), 
        ("🟢", "UI Enhanced", "green"),
        ("🟢", "No Logging Mode", "light_green")
    ]
    
    print(colored("┌─────────── 📊 SYSTEM STATUS 📊 ───────────┐", "cyan"))
    for indicator, text, color in status_indicators:
        print(colored(f"│ {indicator} {text:<35} │", color))
        time.sleep(0.1)
    print(colored("└────────────────────────────────────────────┘", "cyan"))
    
    print()
    print(colored("⚡ NÂNG CẤP: Giao diện mới, không log, tốc độ cao!", "light_yellow"))
    print(colored("🎯 Tính năng: Auto Follow/Like TikTok thông minh", "light_green"))
    print()

def read_auth():
    if os.path.exists(AUTH_FILE):
        with open(AUTH_FILE, "r", encoding="utf8") as f:
            return f.read().strip()
    return ""

def write_auth(auth):
    with open(AUTH_FILE, "w", encoding="utf8") as f:
        f.write(auth.strip())

def validate_auth(auth):
    """Kiểm tra format của Authorization"""
    if not auth or len(auth.strip()) < 20:
        return False, "Authorization quá ngắn"
    
    auth = auth.strip()
    
    # Authorization thường bắt đầu bằng Bearer hoặc là token dài
    if not (auth.startswith('Bearer ') or len(auth) > 50):
        return False, "Format Authorization không hợp lệ"
    
    # Kiểm tra ký tự đặc biệt
    if any(char in auth for char in ['\n', '\r', '\t', ' ' * 3]):
        return False, "Authorization chứa ký tự không hợp lệ"
    
    return True, "Authorization hợp lệ"

def clear_auth():
    loading_animation("Đang xóa Authorization", 1)
    if os.path.exists(AUTH_FILE):
        os.remove(AUTH_FILE)
        print(colored("✅ Đã xóa Authorization thành công!", "green"))
    else:
        print(colored("⚠️  File Authorization không tồn tại!", "yellow"))
    
    print(colored("\n📝 Nhấn Enter để tiếp tục...", "light_cyan"))
    input()

def show_system_info():
    """Hiển thị thông tin hệ thống với giao diện đẹp"""
    print(colored("┌─────────────── 💻 THÔNG TIN HỆ THỐNG 💻 ──────────────┐", "cyan"))
    print(colored("│                                                       │", "white"))
    
    # Thông tin hệ thống
    try:
        import platform
        system_info = [
            ("🖥️  Hệ điều hành", platform.system()),
            ("🏷️  Phiên bản", platform.release()),
            ("🔧 Kiến trúc", platform.architecture()[0]),
            ("🐍 Python", platform.python_version()),
            ("⏰ Thời gian", datetime.now(tz).strftime("%H:%M:%S %d/%m/%Y")),
            ("🌍 Timezone", "Asia/Ho_Chi_Minh"),
        ]
        
        for icon_label, value in system_info:
            print(colored(f"│ {icon_label:<15}: {value:<30} │", "white"))
            
    except:
        print(colored("│ ❌ Không thể lấy thông tin hệ thống               │", "red"))
    
    print(colored("│                                                       │", "white"))
    print(colored("└───────────────────────────────────────────────────────┘", "cyan"))
    print()

def show_features():
    """Hiển thị tính năng với giao diện đẹp"""
    print(colored("┌─────────────── 🚀 TÍNH NĂNG PRO 🚀 ──────────────┐", "light_green"))
    print(colored("│                                                   │", "white"))
    
    features = [
        ("🎯", "Auto Follow TikTok thông minh"),
        ("❤️", "Auto Like TikTok tự động"),
        ("🔄", "Retry mechanism thông minh"),
        ("⚡", "Giao diện nhanh, không lag"),
        ("🎨", "UI/UX đẹp mắt, dễ sử dụng"),
        ("🚫", "Không tạo log file rườm rà"),
        ("🛡️", "Xử lý lỗi thông minh"),
        ("📊", "Thống kê real-time"),
        ("🎭", "Animation và hiệu ứng"),
        ("🔧", "Cấu hình linh hoạt")
    ]
    
    for icon, desc in features:
        print(colored(f"│ {icon} {desc:<45} │", "white"))
        time.sleep(0.1)
    
    print(colored("│                                                   │", "white"))
    print(colored("└───────────────────────────────────────────────────┘", "light_green"))
    
    print(colored("\n📝 Nhấn Enter để tiếp tục...", "light_cyan"))
    input()

def menu():
    banner()
    
    # Hiển thị thông tin hệ thống với animation
    show_system_info()
    
    # Menu chính với thiết kế Pro
    menu_items = [
        ("1️⃣", "Bắt đầu Tool TikTok Auto", "🚀", "light_green"),
        ("2️⃣", "Xóa Authorization hiện tại", "🗑️", "red"),
        ("3️⃣", "Thông tin hệ thống", "💻", "blue"),
        ("4️⃣", "Tính năng của tool", "🔥", "cyan"),
        ("0️⃣", "Thoát tool", "👋", "purple")
    ]
    
    print(colored("┌─────────────────── 🎮 MENU CHÍNH 🎮 ───────────────────┐", "yellow"))
    print(colored("│                                                         │", "white"))
    
    for number, desc, icon, color in menu_items:
        print(colored(f"│  {number} {icon} {desc:<40} │", color))
        time.sleep(0.1)
    
    print(colored("│                                                         │", "white"))
    print(colored("└─────────────────────────────────────────────────────────┘", "yellow"))
    print()

def safe_request(method, url, headers=None, data=None, timeout=DEFAULT_TIMEOUT, max_retries=MAX_RETRIES):
    """Thực hiện request với retry mechanism"""
    for attempt in range(max_retries):
        try:
            if method.upper() == 'GET':
                response = requests.get(url, headers=headers, timeout=timeout)
            elif method.upper() == 'POST':
                # Sử dụng json thay vì data cho POST request
                if data and isinstance(data, str):
                    try:
                        data = json.loads(data)
                    except:
                        pass
                response = requests.post(url, json=data, headers=headers, timeout=timeout)
            else:
                raise ValueError(f"Unsupported method: {method}")
            
            if response.status_code == 200:
                try:
                    return response.json()
                except json.JSONDecodeError:
                    return {"status": response.status_code, "data": response.text}
            elif response.status_code == 403:
                # Chỉ hiển thị thông báo cho người dùng, không log
                if attempt == 0:
                    print(colored("⚠️  Authorization có thể không hợp lệ (HTTP 403)", "yellow"))
            
        except requests.exceptions.Timeout:
            if attempt == 0:
                print(colored(f"⏰ Timeout kết nối - thử lại...", "yellow"))
        except requests.exceptions.ConnectionError:
            if attempt == 0:
                print(colored(f"🌐 Lỗi kết nối mạng - thử lại...", "yellow"))
        except Exception as e:
            if attempt == 0:
                print(colored(f"❌ Lỗi request: {str(e)[:50]}...", "red"))
        
        if attempt < max_retries - 1:
            delay = RETRY_DELAY * (attempt + 1) + random.uniform(0.5, 1.5)
            time.sleep(delay)
    
    return {}
def build_headers(auth):
    return {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'gateway.golike.net',
        'Origin': 'https://app.golike.net',
        'Referer': 'https://app.golike.net/',
        'Sec-Ch-Ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'T': 'VFZSak1FMTZZM3BOZWtFd1RtYzlQUT09',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
        "Authorization": auth
    }

def get_tiktok_accounts(headers):
    try:
        print(colored("🔍 Đang lấy danh sách tài khoản TikTok...", "cyan"))
        result = safe_request('GET', 'https://gateway.golike.net/api/tiktok-account', headers=headers)
        if result and result.get("status") == 200:
            print(colored(f"✅ Lấy thành công {len(result.get('data', []))} tài khoản!", "green"))
        return result
    except Exception as e:
        print(colored(f"❌ Lỗi lấy danh sách TikTok: {e}", "red"))
        return {}

def get_jobs(account_id, headers):
    try:
        url = f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={account_id}&data=null'
        result = safe_request('GET', url, headers=headers)
        return result
    except Exception as e:
        print(colored(f"❌ Lỗi lấy job: {e}", "red"))
        return {}

def complete_job(ads_id, account_id, headers):
    try:
        url = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
        data = {
            "ads_id": ads_id,
            "account_id": account_id,
            "async": True,
            "data": None
        }
        result = safe_request('POST', url, headers=headers, data=data)
        return result
    except Exception as e:
        print(colored(f"❌ Lỗi hoàn thành job: {e}", "red"))
        return {}

def report_job(ads_id, object_id, account_id, job_type, headers):
    """Báo cáo job với retry mechanism"""
    try:
        data1 = {
            "description": "Báo cáo hoàn thành thất bại",
            "users_advertising_id": ads_id,
            "type": "ads",
            "provider": "tiktok",
            "fb_id": account_id,
            "error_type": 6
        }
        safe_request('POST', 'https://gateway.golike.net/api/report/send', 
                    headers=headers, data=data1, timeout=8)

        data2 = {
            "ads_id": ads_id,
            "object_id": object_id,
            "account_id": account_id,
            "type": job_type
        }
        safe_request('POST', 'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs', 
                    headers=headers, data=data2, timeout=8)
        
    except Exception:
        pass  # Không hiển thị lỗi report để giữ giao diện sạch

def show_accounts(accounts):
    loading_animation("Đang tải danh sách tài khoản", 1)
    
    print(colored("┌─────────────── 📱 DANH SÁCH TÀI KHOẢN 📱 ──────────────┐", "cyan"))
    print(colored("│                                                        │", "white"))
    
    data = accounts.get("data", [])
    if not isinstance(data, list) or not data:
        print(colored("│ ❌ Không có tài khoản TikTok nào!                     │", "red"))
        print(colored("│ 💡 Vui lòng thêm tài khoản TikTok vào GoLike         │", "yellow"))
        print(colored("│                                                        │", "white"))
        print(colored("└────────────────────────────────────────────────────────┘", "cyan"))
        return
    
    # Header với style đẹp
    print(colored("│ STT │ 📱 Username        │ 🔋 Trạng thái     │ 💰 Xu │", "white"))
    print(colored("├─────┼─────────────────────┼────────────────────┼────────┤", "cyan"))
    
    for idx, acc in enumerate(data, 1):
        username = acc.get('unique_username', 'N/A')[:15]
        status_icon = "🟢" if acc.get('status') == 1 else "🔴"
        status_text = "Hoạt động" if acc.get('status') == 1 else "Không hoạt động"
        xu_count = acc.get('coin', 0)
        
        status_color = "green" if acc.get('status') == 1 else "red"
        
        print(colored(f"│ {idx:3} │ {username:<19} │ {status_icon} {status_text:<13} │ {xu_count:6} │", status_color))
        time.sleep(0.05)  # Animation delay
    
    print(colored("│                                                        │", "white"))
    print(colored("└────────────────────────────────────────────────────────┘", "cyan"))
    print()

def input_int(prompt, color="green", minval=1, maxval=None):
    """Input số nguyên với validation tốt hơn"""
    while True:
        try:
            value = input(colored(prompt, color)).strip()
            
            if not value.isdigit():
                print(colored("❌ Vui lòng nhập số nguyên dương!", "red"))
                continue
                
            num_value = int(value)
            
            if num_value < minval:
                print(colored(f"❌ Giá trị phải >= {minval}!", "red"))
                continue
                
            if maxval and num_value > maxval:
                print(colored(f"❌ Giá trị phải <= {maxval}!", "red"))
                continue
                
            return num_value
            
        except KeyboardInterrupt:
            print(colored("\n🛑 Đã hủy thao tác!", "yellow"))
            sys.exit()
        except Exception as e:
            print(colored(f"❌ Lỗi input: {e}", "red"))

def validate_url(url):
    """Kiểm tra URL hợp lệ"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def open_link_smart(link):
    """Mở link thông minh với nhiều phương thức"""
    if not validate_url(link):
        return False
    
    methods = [
        ("termux-open-url", f"termux-open-url {link}"),
        ("xdg-open", f"xdg-open {link}"),
        ("$BROWSER", f"$BROWSER {link}"),
    ]
    
    for method_name, command in methods:
        try:
            code = os.system(command + " 2>/dev/null")
            if code == 0:
                return True
        except Exception:
            continue
    
    # Nếu không mở được tự động, hiển thị link cho người dùng
    print(colored(f"🔗 Link: {link[:50]}...", "light_blue"))
    return False

def main():
    # Menu chính
    while True:
        menu()
        try:
            choose = input(colored("🎯 Nhập lựa chọn của bạn: ", "light_cyan")).strip()
            
            if choose == "0":
                loading_animation("Đang thoát tool", 2)
                print_with_animation("👋 Cảm ơn bạn đã sử dụng GoLike TikTok Auto Tool Pro!", "light_green")
                sys.exit()
                
            elif choose == "1":
                break
                
            elif choose == "2":
                clear_auth()
                continue
                
            elif choose == "3":
                show_system_info()
                input(colored("📝 Nhấn Enter để tiếp tục...", "light_cyan"))
                continue
                
            elif choose == "4":
                show_features()
                continue
                
            else:
                print(colored("❌ Lựa chọn không hợp lệ! Vui lòng chọn 0-4", "red"))
                time.sleep(1.5)
                
        except KeyboardInterrupt:
            print(colored("\n🛑 Tool đã được thoát!", "yellow"))
            sys.exit()

    # Xử lý Authorization với giao diện đẹp
    auth = read_auth()
    while not auth:
        print(colored("┌─────────── 🔑 NHẬP AUTHORIZATION 🔑 ──────────┐", "yellow"))
        print(colored("│                                               │", "white"))
        print(colored("│ 📋 Hướng dẫn lấy Authorization:               │", "light_blue"))
        print(colored("│ 1. Vào app.golike.net trên trình duyệt       │", "white"))
        print(colored("│ 2. Bấm F12 → Network → Refresh trang         │", "white"))
        print(colored("│ 3. Tìm request có chữ 'Authorization'        │", "white"))
        print(colored("│ 4. Copy giá trị Authorization (Bearer...)    │", "white"))
        print(colored("│                                               │", "white"))
        print(colored("└───────────────────────────────────────────────┘", "yellow"))
        print()
        
        auth = input(colored("🔑 Nhập Authorization: ", "light_green")).strip()
        if auth:
            # Validate Authorization với animation
            print(colored("🔍 Đang kiểm tra format Authorization...", "cyan"))
            time.sleep(0.5)
            
            is_valid, message = validate_auth(auth)
            if not is_valid:
                print(colored(f"❌ {message}", "red"))
                print(colored("💡 Vui lòng kiểm tra lại Authorization", "yellow"))
                time.sleep(1)
                continue
                
            write_auth(auth)
            print(colored("✅ Authorization đã được lưu!", "green"))
        else:
            print(colored("❌ Authorization không được để trống!", "red"))
            time.sleep(1)
    
    headers = build_headers(auth)
    
    # Animation đăng nhập với hiệu ứng đẹp
    loading_animation("Đang kiểm tra Authorization", 2)
    
    # Lấy danh sách tài khoản
    accounts = get_tiktok_accounts(headers)
    if not accounts or accounts.get("status") != 200 or not accounts.get("data"):
        print(colored("❌ Authorization không hợp lệ hoặc không có tài khoản TikTok!", "red"))
        print(colored("🔄 Vui lòng kiểm tra lại Authorization", "yellow"))
        clear_auth()
        return main()
    
    print(colored("✅ Đăng nhập thành công!", "green"))
    time.sleep(1)
    
    # Hiển thị và chọn tài khoản
    show_accounts(accounts)
    
    while True:
        idacc = input(colored("🎯 Nhập Username TikTok: ", "light_blue")).strip()
        acc_obj = next((a for a in accounts.get("data", []) if a.get("unique_username") == idacc), None)
        if acc_obj:
            account_id = acc_obj.get("id")
            print(colored(f"✅ Đã chọn tài khoản: {idacc}", "green"))
            time.sleep(0.5)
            break
        print(colored("❌ Username không tồn tại! Vui lòng kiểm tra lại", "red"))
    
    # Cấu hình tool với giao diện Pro
    print(colored("\n┌─────────── ⚙️  CẤU HÌNH TOOL PRO ⚙️  ───────────┐", "yellow"))
    print(colored("│                                                 │", "white"))
    
    delay = input_int("⏰ Thời gian chờ mỗi job (giây): ", "light_cyan", 5, 300)
    
    while True:
        lannhan = input(colored("🔄 Thử nhận tiền lần 2 nếu lần 1 thất bại? (y/n): ", "light_cyan")).strip().lower()
        if lannhan in {"y", "n"}:
            break
        print(colored("❌ Vui lòng nhập 'y' hoặc 'n'!", "red"))
    
    doiacc = input_int("🔄 Số job thất bại để đổi tài khoản (1 = không đổi): ", "light_cyan", 1, 50)
    
    # Chọn loại job với giao diện đẹp
    print(colored("│                                                 │", "white"))
    print(colored("│ 📋 CHỌN LOẠI NHIỆM VỤ:                          │", "light_yellow"))
    
    job_options = [
        ("1️⃣", "Chỉ Follow", "💕"),
        ("2️⃣", "Chỉ Like", "❤️"),
        ("3️⃣", "Cả Follow và Like", "🔥")
    ]
    
    for number, desc, icon in job_options:
        print(colored(f"│ {number} {icon} {desc:<35} │", "white"))
    
    print(colored("│                                                 │", "white"))
    print(colored("└─────────────────────────────────────────────────┘", "yellow"))
    
    while True:
        chedo = input(colored("🎯 Chọn loại nhiệm vụ: ", "light_green")).strip()
        if chedo in {"1", "2", "3"}:
            break
        print(colored("❌ Vui lòng chọn 1, 2 hoặc 3!", "red"))
    
    lam = ["follow"] if chedo == "1" else ["like"] if chedo == "2" else ["follow", "like"]
    job_types_str = " & ".join(lam).title()
    
    # Hiển thị cấu hình cuối cùng với animation
    loading_animation("Đang khởi tạo cấu hình", 2)
    
    print(colored(f"\n🚀 KHỞI ĐỘNG TOOL VỚI CẤU HÌNH:", "light_green"))
    config_items = [
        ("📱", "Tài khoản", idacc),
        ("🎯", "Loại job", job_types_str),
        ("⏰", "Thời gian chờ", f"{delay}s"),
        ("🔄", "Retry", "Có" if lannhan == "y" else "Không"),
        ("🔄", "Đổi acc sau", f"{doiacc} job thất bại")
    ]
    
    for icon, label, value in config_items:
        print(colored(f"   {icon} {label}: {value}", "white"))
        time.sleep(0.2)
    
    print()
    
    # Vòng lặp chính với giao diện Pro
    dem = tong = checkdoiacc = success_streak = 0
    prev_job = None
    
    # Header bảng thống kê với gradient
    print(colored("┌──────────── 📊 TRẠNG THÁI HOẠT ĐỘNG REAL-TIME 📊 ────────────┐", "cyan"))
    print(colored("│ STT │   Thời gian   │ Trạng thái  │ Loại  │  Xu  │ Tổng │ Streak │", "white"))
    print(colored("├─────┼───────────────┼─────────────┼────────┼──────┼──────┼────────┤", "cyan"))
    
    try:
        while True:
            # Kiểm tra điều kiện đổi tài khoản với animation
            if checkdoiacc >= doiacc and doiacc > 1:
                print(colored(f"\n⚠️  Thất bại {checkdoiacc} job liên tiếp - Cần đổi tài khoản!", "light_yellow"))
                show_accounts(accounts)
                
                while True:
                    idacc = input(colored("🔄 Nhập Username TikTok mới: ", "light_blue")).strip()
                    acc_obj = next((a for a in accounts.get("data", []) if a.get("unique_username") == idacc), None)
                    if acc_obj:
                        account_id = acc_obj.get("id")
                        checkdoiacc = 0
                        print(colored(f"✅ Đã đổi sang tài khoản: {idacc}", "green"))
                        break
                    print(colored("❌ Username không tồn tại!", "red"))
            
            # Tìm job với animation
            status_msg = "🔍 Đang tìm nhiệm vụ"
            print(colored(f"\r{status_msg}{'.' * (dem % 4):<4}", "light_purple"), end="", flush=True)
            
            nhanjob = get_jobs(account_id, headers)
            if not nhanjob or not nhanjob.get("data"):
                print(colored(f"\r⏳ Không có job - Chờ 10s {'⏰' * ((dem % 3) + 1):<10}", "yellow"), end="", flush=True)
                time.sleep(10)
                continue
            
            # Kiểm tra job trùng
            current_job_data = nhanjob.get("data", {})
            if (prev_job and 
                prev_job.get("data", {}).get("link") == current_job_data.get("link") and 
                prev_job.get("data", {}).get("type") == current_job_data.get("type")):
                print(colored(f"\r🔄 Job trùng - Bỏ qua {'🔄' * ((dem % 2) + 1):<15}", "orange"), end="", flush=True)
                report_job(current_job_data.get("id"), current_job_data.get("object_id"), 
                          account_id, current_job_data.get("type"), headers)
                time.sleep(2)
                continue
            
            prev_job = nhanjob
            
            if nhanjob.get("status") == 200:
                data = nhanjob["data"]
                ads_id = data.get("id")
                link = data.get("link")
                object_id = data.get("object_id")
                job_type = data.get("type", "unknown")
                
                # Kiểm tra link hợp lệ
                if not link or not validate_url(link):
                    print(colored(f"\r❌ Job không hợp lệ - Bỏ qua{' '*20}", "red"), end="", flush=True)
                    report_job(ads_id, object_id, account_id, job_type, headers)
                    checkdoiacc += 1
                    time.sleep(2)
                    continue
                
                # Kiểm tra loại job
                if job_type not in lam:
                    print(colored(f"\r⏭️  Bỏ qua job {job_type}{' '*20}", "yellow"), end="", flush=True)
                    report_job(ads_id, object_id, account_id, job_type, headers)
                    time.sleep(1)
                    continue
                
                # Mở link với hiệu ứng
                print(colored(f"\r🌐 Mở {job_type} {'🚀' * ((dem % 3) + 1):<10}", "light_cyan"), end="", flush=True)
                open_link_smart(link)
                
                # Countdown với progress bar gradient
                for t in range(delay, -1, -1):
                    progress = progress_bar(delay - t, delay, 25, f"⏰ Chờ {t:2}s")
                    print(colored(f"\r{progress}", "light_blue"), end="", flush=True)
                    time.sleep(1)
                
                # Nhận tiền với animation
                success = False
                max_attempts = 2 if lannhan == "y" else 1
                
                for attempt in range(max_attempts):
                    if attempt > 0:
                        print(colored(f"\r🔄 Lần thử {attempt + 1} {'💫' * (attempt + 1):<10}", "pink"), end="", flush=True)
                        time.sleep(1)
                    
                    nhantien = complete_job(ads_id, account_id, headers)
                    
                    if nhantien.get("status") == 200:
                        success = True
                        dem += 1
                        tien = nhantien["data"].get("prices", 0)
                        tong += tien
                        success_streak += 1
                        now = datetime.now(tz).strftime("%H:%M:%S")
                        
                        # Reset counter thất bại
                        checkdoiacc = 0
                        
                        # Hiển thị kết quả với màu gradient
                        status_text = "✅ Thành công"
                        status_color = "light_green"
                        
                        print(colored(f"\r│{dem:4} │ {now} │ {status_text:<11} │ {job_type:<6} │ +{tien:<3} │ {tong:<4} │ {success_streak:<6} │", status_color))
                        break
                
                if not success:
                    checkdoiacc += 1
                    success_streak = 0
                    now = datetime.now(tz).strftime("%H:%M:%S")
                    
                    # Báo cáo job thất bại
                    report_job(ads_id, object_id, account_id, job_type, headers)
                    
                    status_text = "❌ Thất bại"
                    print(colored(f"\r│{dem:4} │ {now} │ {status_text:<11} │ {job_type:<6} │  0   │ {tong:<4} │ {checkdoiacc:<6} │", "red"))
            
            else:
                print(colored(f"\r⚠️  API Error - Chờ 10s {'⚡' * ((dem % 4) + 1):<15}", "orange"), end="", flush=True)
                time.sleep(10)
                
    except KeyboardInterrupt:
        print(colored(f"\n\n🛑 Tool đã được dừng bởi người dùng!", "yellow"))
        print(colored("┌─────────────── 📊 THỐNG KÊ CUỐI CÙNG 📊 ──────────────┐", "cyan"))
        print(colored(f"│ 🎯 Hoàn thành: {dem:<8} job                         │", "white"))
        print(colored(f"│ 💰 Tổng xu:    {tong:<8} xu                          │", "white"))
        print(colored(f"│ 🔥 Streak max: {success_streak:<8} job liên tiếp      │", "white"))
        print(colored("└──────────────────────────────────────────────────────┘", "cyan"))
        
    except Exception as e:
        print(colored(f"\n❌ Lỗi nghiêm trọng: {e}", "red"))
        print(colored("🔄 Tool sẽ khởi động lại sau 5 giây...", "yellow"))
        time.sleep(5)
        return main()

if __name__ == "__main__":
    main()