import requests
import json

# 1) Construct the query for entries containing RNA
query_payload = {
    "query": {
        
        "type": "terminal",
        "service": "text",
        "parameters": {
            "value": "RNA"
        }
    },
    "return_type": "entry"
}

search_url = "https://search.rcsb.org/rcsbsearch/v2/query?json="

# 2) Perform the query
response = requests.get(search_url + json.dumps(query_payload))
if response.status_code != 200:
    raise Exception(f"Search request failed with status {response.status_code}")

search_results = response.json()
pdb_ids = [item["identifier"] for item in search_results["result_set"]]

print(f"Found {len(pdb_ids)} PDB entries containing 'RNA'.")

# 3) Write the PDB IDs to a text file
output_filename = "rna_pdb_ids.txt"
with open(output_filename, "w") as f:
    for pid in pdb_ids:
        f.write(pid + "\n")

print(f"PDB IDs saved to '{output_filename}'")