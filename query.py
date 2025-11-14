import os
import requests

dune_api_key = os.getenv("DEFI_JOSH_DUNE_QUERY_API_KEY")

if not dune_api_key:
    raise ValueError("API key not found in environment variables")

query_ids = [6151943, 6152176, 6152608, 6154760, 6155052, 6154197, 6152448, 6153828, 6153694, 6182546, 6183240, 6183386, 6183420, 6183986]

headers = {"X-DUNE-API-KEY": dune_api_key}

for query_id in query_ids:
    url = f"https://api.dune.com/api/v1/query/{query_id}/execute"
    response = requests.post(url, headers=headers)
    print(f"Query {query_id}: {response.status_code} - {response.text}")
