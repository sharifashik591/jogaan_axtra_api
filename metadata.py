payload = {
    "table": "information_schema.tables",
    "query": "select table_name, table_type from information_schema.tables where table_schema = database() order by table_name"
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()
    if data.get("success") and "payload" in data:
        # Extract only table names
        tables = [t["table_name"] for t in data["payload"]]
        print("All tables:")
        print(tables)
    else:
        print("API did not return expected payload:", data)
else:
    print("Request failed:", response.status_code, response.text)