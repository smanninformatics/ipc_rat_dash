# convert_to_utf8.py
src = "app/app.py"
# Read with the likely Windows encoding (cp1252 never fails on 0xE7),
# then rewrite as UTF-8 without a BOM.
with open(src, encoding="cp1252") as f:
    text = f.read()
with open(src, "w", encoding="utf-8", newline="\n") as f:
    f.write(text)
print("Re-saved as UTF-8.")