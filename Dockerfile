# 1. Python-ning rasmiy engil obrazidan foydalanamiz
FROM python:3.11-slim

# 2. Server ichidagi ishchi papkani belgilaymiz
WORKDIR /app

# 3. Python terminalga xatolarni darhol chiqarishi uchun sozlamalar
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 4. Kerakli paketlarni o'rnatish uchun requirements.txt ni nusxalaymiz
COPY requirements.txt /app/

# 5. Kutubxonalarni o'rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# 6. Loyihaning qolgan barcha kodlarini konteyner ichiga ko'chiramiz
COPY .. /app/

# 7. Django statik fayllarini yig'amiz
RUN python manage.py collectstatic --noinput

# 8. Konteyner ishga tushganda loyihani qaysi portda yurgizishni belgilaymiz
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]