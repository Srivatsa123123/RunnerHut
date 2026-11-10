import time
import requests

def check_website(url: str, timeout: int = 5) -> dict:
  start_time = time.time()
  try:
    response = requests.get(url, timeout=timeout)
    latency = round((time.time() - start_time) * 1000, 2)
    
    return {
        'url': url,
        'status': 'UP' if response.status_code == 200 else 'ISSUE',
        'http_code': response.status_code,
        'latency_ms': latency,
    }
  except requests.RequestException as error:
    return {'url': url, 'status': 'DOWN', 'http_code': None, 'error': str(error)}

if __name__ == '__main__':
  # We replaced the single target_url with a list of multiple URLs
  urls_to_monitor = [
      'https://httpbin.org/status/200',
      'https://httpbin.org/status/404',  # This intentionally simulates a broken link
      'https://example.com'
  ]
  
  print("Starting RunnerHut Monitor...\n")
  
  # The 'for' loop goes through the list one by one
  for target in urls_to_monitor:
    print(f'Pinging {target}...')
    result = check_website(target)
    
    print(f"  Status:    {result['status']}")
    print(f"  HTTP Code: {result.get('http_code')}")
    if 'latency_ms' in result:
      print(f"  Latency:   {result['latency_ms']} ms")
    if 'error' in result:
      print(f"  Error:     {result['error']}")
    print("-" * 40)  # Prints a visual divider between results