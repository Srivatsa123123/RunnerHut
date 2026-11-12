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
  urls_to_check = [
      'https://httpbin.org/status/200',
      'https://httpbin.org/status/404',
      'https://example.com'
  ]
  
  print("Starting RunnerHut Continuous Monitor...")
  
  # The infinite loop that keeps the container alive
  while True:
    for target in urls_to_check:
      result = check_website(target)
      print(f"[{result['status']}] {target} - {result.get('http_code')} ({result.get('latency_ms', 0)}ms)", flush=True)
    
    print("Sleeping for 30 seconds...\n", flush=True)
    time.sleep(30)