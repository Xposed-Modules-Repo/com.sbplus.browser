import sys
sys.stdout.reconfigure(encoding="utf-8")
# 检查 SUMMARY 的真实字节是否为有效UTF-8中文
raw = open("SUMMARY","rb").read()
print("字节:", raw[:80])
s = raw.decode("utf-8", errors="replace")
print("解码:", s[:120])
# 检测是否含 mojibake(乱码)模式: 常见是中文被GBK编码后按Latin1读
import re
bad = re.findall(r'[\ufffd]', s)
print("替换符数:", len(bad))
