import ast
import json
from pathlib import Path

log_file = Path(r"c:\Users\Pc\Desktop\Shubham\My work\options_risk_framework\log.jsonl")

if log_file.exists():
    with open(log_file, "r") as f:
        lines = f.readlines()
    
    with open(log_file, "w") as f:
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                # ast.literal_eval is safe for Python literals like dicts with single quotes
                data = ast.literal_eval(line)
                f.write(json.dumps(data) + "\n")
            except (ValueError, SyntaxError):
                # Skip invalid lines
                print(f"Skipping malformed line: {line[:50]}...")
                continue
    print("log.jsonl has been converted to valid JSONLines.")
else:
    print("log.jsonl not found.")
