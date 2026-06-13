import requests
import json

endpoints = [
    {"path": "/api/arots", "name": "arots", "essential_keys": ["id", "b2b_seller_id", "created_at"]},
    {"path": "/api/products", "name": "products", "essential_keys": ["id", "name", "category_id"]},
    {"path": "/api/units", "name": "units", "essential_keys": ["id", "name", "status"]}
]

for ep in endpoints:
    url = f"http://127.0.0.1:5000{ep['path']}"
    try:
        print(f"\n==========================================")
        print(f"Testing endpoint: {url}")
        print(f"==========================================")
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
            for key in ep["essential_keys"]:
                if key not in data[0]:
                    print(f"Warning: Expected key '{key}' not found in record. Record fields: {list(data[0].keys())}")
            print(f"\nVerification checks for {ep['name']} passed successfully!")
        else:
            print(f"Warning: Received empty list of {ep['name']} records.")

    except Exception as e:
        print(f"Verification FAILED for {ep['name']}: {str(e)}")
        exit(1)

