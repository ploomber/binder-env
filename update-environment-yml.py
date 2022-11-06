from datetime import datetime
from pathlib import Path

path = Path('environment.yml')
content = path.read_text()
lines = content.splitlines()
current = datetime.now()
lines[0] = f'# Automatically added by GitHub Actions on {current}'
path.write_text('\n'.join(lines))
