import requests
import pandas as pd
from openai import OpenAI
from datetime import datetime

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="your_openai_api_key")  # Replace with your OpenAI API key

def fetch_exchange_rate(currency, date):
    url = "https://api.finmindtrade.com/api/v3/data"
    params = {
        "dataset": "TaiwanExchangeRate",
        "data_id": currency,
        "date": date,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return pd.DataFrame(data['data'])

def analyze_rates(rates):
    prompt = (
        "I will provide you with the cash buying exchange rates for USD and EUR every Thursday. "
        "Please predict the cash buying exchange rates for USD and EUR on Friday based on monetary "
        "policies or international policies, etc.:\n"
    )
    for _, row in rates.iterrows():
        prompt += f"The cash buying exchange rate for {row['currency']} is {row['cash_buy']}.\n"
    
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a financial expert."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message['content']

def send_line_message(message, token, user_id):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    payload = {
        'to': user_id,  # Replace with your user ID or group ID
        'messages': [
            {
                'type': 'text',
                'text': message
            }
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    return response

# Get the current date
date = datetime.now().strftime("%Y-%m-%d")

# Fetch exchange rates
usd_data = fetch_exchange_rate("USD", date)
usd_data['currency'] = 'USD'

eur_data = fetch_exchange_rate("EUR", date)
eur_data['currency'] = 'EUR'

# Combine data
combined_data = pd.concat([usd_data, eur_data])

# Analyze and predict exchange rates
combined_analysis = analyze_rates(combined_data)

# Convert DataFrame to string
combined_data_str = combined_data[['date', 'currency', 'cash_buy']].to_string(index=False)

# Send messages to LINE
line_token = 'YOUR_CHANNEL_ACCESS_TOKEN'  # Replace with your Channel Access Token
user_id = 'YOUR_USER_ID'  # Replace with your user ID or group ID
send_line_message(combined_data_str, line_token, user_id)
send_line_message(combined_analysis, line_token, user_id)
