import subprocess
import json

def run_cli(cmd: list):
    print('#' * 80)
    print(' '.join(cmd))
    print('#' * 80)
    result, _ = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()
    result = result.decode('utf-8')
    result = json.loads(result)
    return result