"""Собирает index.html для GitHub Pages из src/body.html."""
import pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
body = (root / "src" / "body.html").read_text(encoding="utf-8")

# head-only parts (title, meta, links, style) stay in <head>, the rest goes to <body>
split = body.index("</style>") + len("</style>")
head_part, body_part = body[:split], body[split:]
head_part = head_part.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")

head = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<meta name="theme-color" content="#0b0720">
<meta name="description" content="Три браузерные мини-игры: гонка на закате, квиз-пати и пиксельная кухня. Играйте с телефона или компьютера.">
<meta property="og:title" content="Пиксель-Парк — мини-игры в браузере">
<meta property="og:description" content="Гонка, квиз и бургерная. Открывается по ссылке на любом телефоне.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Crect width='16' height='16' rx='3' fill='%23130d2c'/%3E%3Crect x='3' y='5' width='10' height='6' fill='%23ff4f9a'/%3E%3Crect x='5' y='7' width='2' height='2' fill='%23130d2c'/%3E%3Crect x='10' y='6' width='1' height='1' fill='%23130d2c'/%3E%3Crect x='11' y='8' width='1' height='1' fill='%23130d2c'/%3E%3C/svg%3E">
"""
out = head + head_part + "\n</head>\n<body>" + body_part + "\n</body>\n</html>\n"
(root / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out))
