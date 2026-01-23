import yfinance as yf
from datetime import datetime
import pytz
import os



symbols = {
    "Nippon Silver BeES": "SILVERBEES.NS",
    "Nippon Gold BeES": "GOLDBEES.NS"
}

IST = pytz.timezone("Asia/Kolkata")
now = datetime.now(IST)

lines = []
lines.append(f"Run Time IST: {now.strftime('%Y-%m-%d %H:%M')}\n")

def pct_change(prev, current):
    return ((current - prev) / prev) * 100


for name, ticker in symbols.items():

    stock = yf.Ticker(ticker)
    info = stock.info

    current_price = info.get("regularMarketPrice")
    prev_close = info.get("previousClose")

    if prev_close is None:
        hist = stock.history(period="7d")
        prev_close = hist.iloc[-2]["Close"]

    change = pct_change(prev_close, current_price)

    lines.append(name)
    lines.append(f"Previous Close : ₹{prev_close:.2f}")
    lines.append(f"Current Price  : ₹{current_price:.2f}")

    if change < 0:
        lines.append(f"Dip  : {change:.2f}%")
    else:
        lines.append(f"Gain : {change:.2f}%")

    lines.append("")

# ---- SAVE TO FILE ----
with open("result.txt", "w") as f:
    f.write("\n".join(lines))

print("\n".join(lines))


#----- save output in file -----#
os.makedirs("output", exist_ok=True)

with open("output/result.txt", "w") as f:
    f.write("\n".join(lines))
