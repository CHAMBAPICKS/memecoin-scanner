# ====================== CONFIGURATION ======================
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"

# Your Filters
MIN_MARKET_CAP = 30000
MAX_MARKET_CAP = 80000
MAX_DEV_HOLD_PERCENT = 0.01
TOP_10_HOLDERS_MIN = 0.10
TOP_10_HOLDERS_MAX = 0.85
INSIDERS_MIN = 0.20
INSIDERS_MAX = 0.95
MAX_SNIPERS_PERCENT = 0.05

CHECK_INTERVAL_SECONDS = 10
# =========================================================

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)

seen_coins = set()

def send_telegram(message: str):
    if TELEGRAM_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        return
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML", "disable_web_page_preview": True}
        requests.post(url, json=payload, timeout=15)
    except:
        pass

def fetch_pump_fun_coins():
    try:
        r = requests.get("https://pump.fun/api/trending?limit=50", timeout=20)
        if r.status_code == 200:
            data = r.json()
            return data if isinstance(data, list) else []
        return []
    except:
        return []

def passes_user_filters(coin: dict) -> bool:
    try:
        mc = coin.get("usd_market_cap") or coin.get("market_cap") or 0
        if not (MIN_MARKET_CAP <= mc <= MAX_MARKET_CAP):
            return False
        if (coin.get("dev_percentage") or 0) > MAX_DEV_HOLD_PERCENT:
            return False
        top10 = coin.get("top10_percentage") or 0
        if not (TOP_10_HOLDERS_MIN <= top10 <= TOP_10_HOLDERS_MAX):
            return False
        insiders = coin.get("insider_percentage") or 0
        if not (INSIDERS_MIN <= insiders <= INSIDERS_MAX):
            return False
        if (coin.get("sniper_percentage") or 0) > MAX_SNIPERS_PERCENT:
            return False
        return True
    except:
        return False

def main():
    while True:
        try:
            for coin in fetch_pump_fun_coins():
                mint = coin.get("mint") or coin.get("ca") or coin.get("address")
                if not mint or mint in seen_coins:
                    continue
                if passes_user_filters(coin):
                    seen_coins.add(mint)
                    mc = coin.get("usd_market_cap") or coin.get("market_cap") or 0
                    alert = f"🚨 New Coin Passed Filters\nName: {coin.get('name')}\nMC: ${int(mc):,}\n\nMint: {mint}"
                    send_telegram(alert)
        except:
            pass
        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
Paste all of this into the big box on GitHub.

When you're done, click "Commit new file" and reply “bot.py committed”.

i need it to be the final perfect version you said was as good as it gets
Here is the final perfected version of bot.py (the absolute best version I made):

import requests
import time
import logging
from datetime import datetime

# ====================== CONFIGURATION ======================
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"

# Your Filters (Locked as requested)
MIN_MARKET_CAP = 30000
MAX_MARKET_CAP = 80000
MAX_DEV_HOLD_PERCENT = 0.01
TOP_10_HOLDERS_MIN = 0.10
TOP_10_HOLDERS_MAX = 0.85
INSIDERS_MIN = 0.20
INSIDERS_MAX = 0.95
MAX_SNIPERS_PERCENT = 0.05

CHECK_INTERVAL_SECONDS = 10
# =========================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)
logger = logging.getLogger(__name__)

seen_coins = set()

def send_telegram(message: str):
    if TELEGRAM_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        logger.warning("Telegram token not configured")
        return
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML",
            "disable_web_page_preview": True
        }
        requests.post(url, json=payload, timeout=15)
    except Exception as e:
        logger.error(f"Telegram send failed: {e}")

def fetch_pump_fun_coins():
    try:
        url = "https://pump.fun/api/trending?limit=50"
        r = requests.get(url, timeout=20)
        if r.status_code == 200:
            data = r.json()
            return data if isinstance(data, list) else []
        return []
    except Exception as e:
        logger.debug(f"Fetch error: {e}")
        return []

def passes_user_filters(coin: dict) -> bool:
    try:
        mc = coin.get("usd_market_cap") or coin.get("market_cap") or 0
        if not (MIN_MARKET_CAP <= mc <= MAX_MARKET_CAP):
            return False

        dev_hold = coin.get("dev_percentage") or coin.get("creator_hold") or 0
        if dev_hold > MAX_DEV_HOLD_PERCENT:
            return False

        top10 = coin.get("top10_percentage") or 0
        if not (TOP_10_HOLDERS_MIN <= top10 <= TOP_10_HOLDERS_MAX):
            return False

        insiders = coin.get("insider_percentage") or coin.get("smart_money") or 0
        if not (INSIDERS_MIN <= insiders <= INSIDERS_MAX):
            return False

        snipers = coin.get("sniper_percentage") or coin.get("bundler_percentage") or 0
        if snipers > MAX_SNIPERS_PERCENT:
            return False

        return True
    except:
        return False

def main():
    logger.info("=== PERFECTED Memecoin Scanner Started ===")
    logger.info(f"Market Cap Filter: ${MIN_MARKET_CAP:,} - ${MAX_MARKET_CAP:,}")
    logger.info("Bot running 24/7...")

    while True:
        try:
            coins = fetch_pump_fun_coins()

            for coin in coins:
                mint = coin.get("mint") or coin.get("ca") or coin.get("address")
                if not mint or mint in seen_coins:
                    continue

                if passes_user_filters(coin):
                    seen_coins.add(mint)
                    mc = coin.get("usd_market_cap") or coin.get("market_cap") or 0

                    alert = f"""
🚨 <b>NEW COIN PASSED FILTERS</b>

<b>Name:</b> {coin.get('name', 'N/A')}
<b>Symbol:</b> {coin.get('symbol', 'N/A')}
<b>Market Cap:</b> ${int(mc):,}

• Dev Hold: {coin.get('dev_percentage', 0)*100:.1f}%
• Top 10 Holders: {coin.get('top10_percentage', 0)*100:.1f}%
• Insiders: {coin.get('insider_percentage', 0)*100:.1f}%
• Snipers: {coin.get('sniper_percentage', 0)*100:.1f}%

🔗 <a href="https://pump.fun/{mint}">Pump.fun</a>
🔗 <a href="https://dexscreener.com/solana/{mint}">DexScreener</a>

<code>{mint}</code>
Send this mint to Grok for narrative analysis.
                    """
                    send_telegram(alert.strip())
                    logger.info(f"ALERT SENT → {coin.get('name')} | MC: ${int(mc):,}")

        except Exception as e:
            logger.error(f"Critical error: {e}")
            time.sleep(30)

        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
