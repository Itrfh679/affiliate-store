import os
import requests
import json
from datetime import datetime

TELEGRAM_BOT_TOKEN = "8959389105:AAGza59y2PmqfDrybiZnYJjcAvyIhKLU3w0"
TELEGRAM_CHAT_ID   = "5706939133"

def send_telegram_alert(product_name, platform, order_value, commission_rate, total_commission_so_far):
    """
    Sends an instant sales & commission alert to the user's Telegram.
    """
    commission_earned = round((order_value * commission_rate) / 100, 2)
    new_total = round(total_commission_so_far + commission_earned, 2)
    store_emoji = "🛒" if platform.lower() == "flipkart" else "👗"

    message = f"""
🎉 <b>NAYI SALE TRACK HUI!</b> 🎉
━━━━━━━━━━━━━━━━━━━━
{store_emoji} <b>Platform:</b> {platform.upper()}
👕 <b>Product:</b> {product_name}
💰 <b>Order Value:</b> ₹{order_value:,.2f}
💵 <b>Commission Rate:</b> {commission_rate}%
✨ <b>Is Order Ka Commission:</b> ₹{commission_earned:,.2f}
━━━━━━━━━━━━━━━━━━━━
📈 <b>Total Accumulated Commission:</b> ₹{new_total:,.2f}
⏰ <b>Time:</b> {datetime.now().strftime('%d %b %Y, %I:%M %p')}
━━━━━━━━━━━━━━━━━━━━
🚀 <i>Keep sharing your store: itrfh679.github.io/affiliate-store/</i>
"""

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message.strip(),
        "parse_mode": "HTML"
    }

    try:
        res = requests.post(url, json=payload, timeout=10)
        return res.json().get("ok", False)
    except Exception as e:
        print(f"Error sending telegram alert: {e}")
        return False

if __name__ == "__main__":
    print("Affiliate Telegram Notifier Ready!")
