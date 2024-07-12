
# README

## Introduction
This script fetches the current exchange rates for USD and EUR from Taiwan's financial data, analyzes the rates using OpenAI's GPT-4 model, and sends the results to a specified LINE user or group. This prediction is part of the AIFIAN exchange rate activity utilizing the ChatGPT API.

## 介紹
這個腳本從台灣的金融數據中獲取當前的美元和歐元匯率，使用OpenAI的GPT-4模型分析匯率，並將結果發送到指定的LINE用戶或群組。此預測是利用ChatGPT API進行的AIFIAN匯率活動的一部分。

## Requirements
- Python 3.x
- `requests` library
- `pandas` library
- `openai` library

## 安裝要求
- Python 3.x
- `requests`庫
- `pandas`庫
- `openai`庫

## Installation
Install the required Python libraries using pip:
```sh
pip install requests pandas openai
```

## 安裝
使用pip安裝所需的Python庫：
```sh
pip install requests pandas openai
```

## Usage
1. Replace the placeholders in the script with your actual API keys and user IDs:
   - `your_openai_api_key`: Your OpenAI API key.
   - `YOUR_CHANNEL_ACCESS_TOKEN`: Your LINE Channel Access Token.
   - `YOUR_USER_ID`: Your LINE user ID or group ID.

2. Run the script:
```sh
python your_script.py
```

## 使用方法
1. 將腳本中替換為您的實際API密鑰和用戶ID：
   - `your_openai_api_key`: 您的OpenAI API密鑰。
   - `YOUR_CHANNEL_ACCESS_TOKEN`: 您的LINE Channel訪問令牌。
   - `YOUR_USER_ID`: 您的LINE用戶ID或群組ID。

2. 運行腳本：
```sh
python your_script.py
```

## Scheduling on Windows
To schedule the script to run automatically every Thursday at 4 PM on a Windows machine, follow these steps:

1. Open Task Scheduler.
2. Click on "Create Basic Task...".
3. Name your task and provide a description.
4. Select "Weekly" and click "Next".
5. Set the start date and time to a Thursday at 4 PM and select "Repeat every: 1 week".
6. Select "Start a program" and click "Next".
7. Browse for `rate.py` and in the "Add arguments" field, add the path to your script.
8. Review your settings and click "Finish".

## 在 Windows 上排程
要在Windows機器上每週四下午4點自動運行腳本，請按照以下步驟操作：

1. 打開任務排程器。
2. 點擊“創建基本任務...”。 
3. 命名您的任務並提供描述。
4. 選擇“每週”並點擊“下一步”。
5. 將開始日期和時間設置為星期四下午4點，並選擇“每週重複：1週”。
6. 選擇“啟動程序”並點擊“下一步”。
7. 瀏覽`rate.py`，並在“添加參數”字段中添加腳本的路徑。
8. 查看設置並點擊“完成”。

## Example Output
The script will print the combined exchange rate data and the analysis results, and send these results to the specified LINE user or group.

## 示例輸出
腳本將打印組合的匯率數據和分析結果，並將這些結果發送到指定的LINE用戶或群組。

## Troubleshooting
- Ensure that all API keys and user IDs are correctly set.
- Check the console output for any error messages and verify the response status and body.

## 故障排除
- 確保所有的API密鑰和用戶ID設置正確。
- 檢查控制台輸出是否有錯誤消息，並驗證響應狀態和內容。

## License
This project is licensed under the MIT License.

## 許可證
此項目根據MIT許可證授權。

---
