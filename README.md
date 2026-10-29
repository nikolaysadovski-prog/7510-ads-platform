# 7510 Ads Platform

Technical deployment scaffold only. This is **not** a production advertising platform. No authentication, billing, campaign delivery, Telegram integration or database yet.

Start: `uvicorn app:app --host 0.0.0.0 --port 10000`

Health check: `/health`.

Never commit tokens or credentials. Ads must be delivered only to authorized destinations.
