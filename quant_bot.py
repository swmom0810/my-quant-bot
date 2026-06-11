name: AI Quant Bot Auto Run

on:
  schedule:
    - cron: '0 23 * * *'
  workflow_dispatch:

jobs:
  run-bot:
    runs-on: ubuntu-latest

    steps:
    - name: 1. 내 코드 가져오기
      uses: actions/checkout@v3

    - name: 2. 파이썬 설치하기
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: 3. 필요한 인공지능 라이브러리 설치
      run: |
        pip install yfinance numpy pandas scikit-learn tensorflow transformers requests torch matplotlib

    - name: 4. 내 퀀트 봇 실행하기!
      env:
        TELEGRAM_TOKEN: ${{ secrets.TELEGRAM_TOKEN }}
      run: python quant_bot.py
