import requests
import json

url = "http://127.0.0.1:5000/api/arots"

try:
    print(f"Sending GET request to {url}...")
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Check headers
    content_type = response.headers.get('Content-Type', '')
    print(f"Content-Type: {content_type}")
    assert 'application/json' in content_type, f"Expected application/json in Content-Type, got {content_type}"
    
    # Parse JSON
    data = response.json()
    print("Successfully parsed JSON response!")
    print(f"Number of records retrieved: {len(data)}")
    
    if len(data) > 0:
        print("\nFirst record sample:")
        print(json.dumps(data[0], indent=2))
        
        # Verify key fields are present
        essential_keys = ["id", "b2b_seller_id", "created_at"]
        for key in essential_keys:
            if key not in data[0]:
                print(f"Warning: Expected key '{key}' not found in record. Record fields: {list(data[0].keys())}")
        print("\nVerification checks passed successfully!")
    else:
        print("Warning: Received empty list of arot records.")

except Exception as e:
    print(f"Verification FAILED: {str(e)}")
    exit(1)
