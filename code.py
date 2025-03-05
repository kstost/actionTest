import os
from datetime import datetime
api_key = os.getenv("API_KEY")

# data 폴더가 없으면 생성
os.makedirs("data", exist_ok=True)

# 현재 타임스탬프 (초 단위)
timestamp = int(datetime.now().timestamp())
filename = f"data/{timestamp}.txt"

# 파일 생성 및 내용 기록
with open(filename, "w") as file:
    file.write(f"File created at {timestamp}\n{api_key}")

print(f"File {filename} created.")
