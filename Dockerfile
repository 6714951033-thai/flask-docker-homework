# ใช้ Python image
FROM python:3.10-slim

# กำหนดโฟลเดอร์การทำงาน
WORKDIR /app

# คัดลอก requirements.txt
COPY requirements.txt .

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ด Python
COPY app.py .

# สร้างไฟล์ log.txt
RUN touch log.txt

# เปิด port 5000
EXPOSE 5000

# รัน Flask
CMD ["python", "app.py"]