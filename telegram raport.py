import subprocess
import sys
import os
import webbrowser
import socket
import random
import requests
import time
from datetime import datetime

def install_required_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

essential_packages_collection = [
    "requests",
    "fake_useragent",
    "termcolor"
]

for required_package_module in essential_packages_collection:
    try:
        __import__(required_package_module)
    except ImportError:
        print(f"Gerekli kütüphane {required_package_module} sistemde bulunamadı, yükleme işlemi başlatılıyor...")
        install_required_package(required_package_module)

import random
from fake_useragent import UserAgent
from termcolor import colored

webbrowser.open('https://t.me/+bb6qhd2UaxxiMjBk')

print(colored('━' * 80, 'cyan'))
print(colored('🎯 TELEGRAM ADVANCED REPORT SYSTEM', 'red', attrs=['bold']))
print(colored('━' * 80, 'cyan'))

current_device_hostname = socket.gethostname()
current_device_ip_address = socket.gethostbyname(current_device_hostname)
current_timestamp_datetime = datetime.now()

print(colored(f"✅ Sistem Başarıyla Başlatıldı | Cihaz: {current_device_hostname}", 'green'))
print(colored(f"⏰ Oturum Zamanı: {current_timestamp_datetime.strftime('%Y-%m-%d %H:%M:%S')}", 'yellow'))
print(colored(f"🌐 Ağ IP Adresi: {current_device_ip_address}", 'blue'))
print(colored('━' * 80, 'cyan'))
print(colored('📢 Resmi Telegram Kanalı: https://t.me/+bb6qhd2UaxxiMjBk', 'magenta'))
print(colored('👤 Geliştirici & Yapımcı: @ZytrenixPY', 'cyan'))
print(colored('━' * 80, 'cyan'))

telegram_support_endpoint_url = 'https://telegram.org/support'
user_agent_generator_instance = UserAgent()
total_successful_reports_counter = 0

def send_telegram_abuse_complaint_report(complaint_message_text, contact_phone_number):
    http_request_headers_configuration = {
        'User-Agent': user_agent_generator_instance.random
    }
    complaint_form_data_payload = {
        'text': complaint_message_text,
        'contact': contact_phone_number
    }
    proxy_server_configuration_list = [
        {'http': '43.167.189.202:6006'},
        {'http': '43.167.174.235:6006'},
        {'http': '43.133.12.69:6006'},
        {'http': '43.167.175.2:6006'},
        {'http': '43.167.184.140:6006'},
        {'http': '43.167.206.86:6006'},
        {'http': '43.167.248.236:6006'},
        {'http': '43.167.244.88:6006'},
        {'http': '43.167.196.155:6006'},
        {'http': '43.133.21.32:6006'},
        {'http': '43.167.236.57:6006'},
        {'http': '43.167.247.186:6006'},
        {'http': '43.167.254.69:6006'},
        {'http': '43.167.225.66:6006'},
        {'http': '43.167.254.87:6006'},
        {'http': '160.20.55.235:8080'},
        {'http': '43.167.213.128:6006'},
        {'http': '43.167.235.158:6006'},
        {'http': '43.167.241.146:6006'},
        {'http': '65.109.37.51:8080'},
        {'http': '43.167.185.75:6006'},
        {'http': '43.167.237.219:6006'},
        {'http': '43.167.191.67:6006'},
        {'http': '43.133.12.238:6006'},
        {'http': '43.167.216.216:6006'},
        {'http': '43.167.170.160:6006'},
        {'http': '43.133.8.63:6006'},
        {'http': '43.167.233.124:6006'},
        {'http': '43.167.223.107:6006'},
        {'http': '8.212.177.126:8080'},
        {'http': '43.167.166.248:6006'},
        {'http': '43.133.21.170:6006'},
        {'http': '43.167.212.194:6006'},
        {'http': '43.167.223.67:6006'},
        {'http': '43.167.223.182:6006'},
        {'http': '43.167.168.246:6006'},
        {'http': '43.133.28.61:6006'},
        {'http': '43.167.203.183:6006'},
        {'http': '43.167.214.170:6006'},
        {'http': '43.167.177.101:6006'},
        {'http': '43.167.190.148:6006'},
        {'http': '43.167.236.131:6006'},
        {'http': '43.167.184.4:6006'},
        {'http': '175.99.220.171:80'},
        {'http': '43.133.28.234:6006'},
        {'http': '43.133.5.182:6006'},
        {'http': '43.167.168.253:6006'},
        {'http': '43.167.247.251:6006'},
        {'http': '43.167.225.7:6006'},
        {'http': '43.133.7.95:6006'},
        {'http': '43.133.28.200:6006'},
        {'http': '43.167.173.222:6006'},
        {'http': '43.167.189.221:6006'},
        {'http': '43.167.232.211:6006'},
        {'http': '43.167.220.149:6006'},
        {'http': '43.167.189.181:6006'},
        {'http': '43.167.197.209:6006'},
        {'http': '46.161.6.165:8080'},
        {'http': '43.167.241.42:6006'},
        {'http': '43.167.175.158:6006'},
        {'http': '43.167.156.53:6006'},
        {'http': '43.133.6.137:6006'},
        {'http': '43.167.195.77:6006'},
        {'http': '43.167.252.237:6006'},
        {'http': '43.133.22.80:6006'},
        {'http': '43.167.220.230:6006'},
        {'http': '43.167.224.55:6006'},
        {'http': '43.167.159.226:6006'},
        {'http': '43.167.202.142:6006'},
        {'http': '154.3.236.202:3128'},
        {'http': '43.167.252.12:6006'},
        {'http': '43.167.215.182:6006'},
        {'http': '43.167.194.148:6006'},
        {'http': '43.167.168.70:6006'},
        {'http': '43.133.29.125:6006'},
        {'http': '43.167.241.181:6006'},
        {'http': '43.167.158.91:6006'},
        {'http': '43.167.176.168:6006'},
        {'http': '43.167.248.252:6006'}
    ]
    
    randomly_selected_proxy_configuration = random.choice(proxy_server_configuration_list)

    try:
        http_post_response_object = requests.post(
            telegram_support_endpoint_url, 
            data=complaint_form_data_payload, 
            headers=http_request_headers_configuration, 
            proxies=randomly_selected_proxy_configuration,
            timeout=15
        )
        if http_post_response_object.status_code == 200:
            global total_successful_reports_counter
            total_successful_reports_counter += 1
            print(colored(f"\n✅ Şikayet raporu başarıyla Telegram destek ekibine iletildi", 'green'))
            print(colored(f"📊 Toplam gönderilen rapor sayısı: {total_successful_reports_counter}", 'cyan'))
            print(colored(f"⏰ İşlem zamanı: {datetime.now().strftime('%H:%M:%S')}", 'yellow'))
            print(colored("━" * 80, 'blue'))
        else:
            print(colored(f"\n❌ Şikayet gönderilirken HTTP hatası oluştu | Durum Kodu: {http_post_response_object.status_code}", 'red'))
    except requests.exceptions.Timeout:
        print(colored("\n⚠️ Bağlantı zaman aşımına uğradı, lütfen tekrar deneyin", 'yellow'))
    except requests.exceptions.ProxyError:
        print(colored("\n⚠️ Proxy sunucu bağlantı hatası tespit edildi", 'yellow'))
    except Exception as general_exception_error:
        print(colored(f"\n❌ Beklenmeyen bir hata oluştu: {general_exception_error}", 'red'))

target_username_to_report = input(colored('\n🎯 Şikayet etmek istediğiniz hedef kullanıcı adını girin (örnek: @username) ▶ ', 'green'))
target_phone_number_account = input(colored('📱 Hedef kullanının telefon numarasını girin (örnek: +905551234567) ▶ ', 'magenta'))

complaint_message_templates_collection = [
    f"Dear Telegram Support Team, I am writing to formally report the user {target_username_to_report} (account identifier: {target_phone_number_account}). This individual is engaging in serious violations including deanonymization of Telegram users, privacy invasion, and swatting activities, which directly contravene Telegram's Terms of Service and community guidelines. I respectfully request immediate investigation and appropriate action against this account to protect the safety and privacy of the Telegram community.",
    f"To Telegram Support: I need to report dangerous behavior by user {target_username_to_report} (phone: {target_phone_number_account}). This account is actively involved in doxing, swatting, and harassment of other users, creating serious safety concerns. These actions are clear violations of Telegram's policies and pose real-world risks. Please investigate and take necessary enforcement actions.",
    f"Telegram Support, urgent report: User {target_username_to_report} (contact: {target_phone_number_account}) is conducting malicious activities including user deanonymization and coordinating swatting attacks. This represents severe violations of platform rules and threatens user safety. I request prompt review and account suspension to prevent further harm.",
    f"Hello Telegram Team, I'm reporting {target_username_to_report} (account {target_phone_number_account}) for engaging in prohibited activities such as revealing personal information of users without consent, organizing harassment campaigns, and swatting. These serious ToS violations require immediate attention and enforcement action."
]

contact_phone_numbers_rotation_pool = [
    '+79967285422', '+79269736273', '+79963668355', '+79661214909', 
    '+79254106650', '+22666228126', '+79269069196', '+79315894431', 
    '+79621570718', '+79152847395', '+79037428651', '+79256849372',
    '+79184736251', '+79625183947', '+79341826574', '+79768524139'
]

randomly_selected_complaint_message = random.choice(complaint_message_templates_collection)
randomly_selected_contact_number = random.choice(contact_phone_numbers_rotation_pool)

print(colored("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", 'cyan'))
print(colored("🚀 Şikayet gönderme işlemi başlatılıyor...", 'yellow'))
print(colored("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", 'cyan'))

send_telegram_abuse_complaint_report(randomly_selected_complaint_message, randomly_selected_contact_number)

print(colored(f"\n⏳ Sistem güvenliği için 6 saniye bekleniyor...", 'yellow'))
time.sleep(6)

print(colored("\n✅ İşlem başarıyla tamamlandı!", 'green'))
print(colored("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", 'cyan'))
print(colored("📢 Daha fazla araç için: https://t.me/+bb6qhd2UaxxiMjBk", 'magenta'))
print(colored("👤 yapımcı iletişim: @ZytrenixPY", 'blue'))
print(colored("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", 'cyan'))