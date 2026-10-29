import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="7510 Ads Platform", docs_url=None, redoc_url=None)

@app.get("/health")
def health():
    return {"status": "ok", "service": "7510-ads-platform"}

@app.get("/", response_class=HTMLResponse)
def home():
    return """<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#111827"><title>7510 Ads Platform</title><style>body{margin:0;background:#111827;color:#f9fafb;font:16px system-ui}main{max-width:520px;margin:auto;padding:28px 20px}.brand{color:#facc15;font-weight:800}section{background:#1f2937;border-radius:18px;padding:22px;margin-top:24px}small{color:#9ca3af}h1{line-height:1.15}span{display:inline-block;background:#374151;padding:10px 14px;border-radius:12px;margin:5px}</style></head><body><main><p class="brand">● В ДЕСЯТКУ 7510</p><h1>Рекламный центр</h1><small>Мобильная панель · техническая версия</small><section><h2>Подготовка платформы</h2><p>Сервис доступен. Функции управления рекламой пока не включены.</p><span>Кампании</span><span>Площадки</span><span>Расписание</span><span>Отчёты</span></section><p><small>Не вводите пароли и платёжные данные. Авторизация ещё не настроена.</small></p></main></body></html>"""
