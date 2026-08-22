import sys
sys.stdout.reconfigure(encoding="utf-8")
raw = open("SUMMARY","rb").read()
# 找第二段(中文部分)字节
s = raw.decode("utf-8", errors="replace")
print("完整内容:")
print(s)
print("---")
# 是否含 GBK 编码的中文(乱码特征: 字节>127 但UTF-8无效)
import re
high = [b for b in raw if b > 127]
print(f">127字节数: {len(high)} / {len(raw)}")
