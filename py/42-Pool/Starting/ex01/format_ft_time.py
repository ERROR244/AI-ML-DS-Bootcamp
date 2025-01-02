import time
from datetime import date

t = time.time()

print(f'Seconds since January 1, 1970: {format(t, ",.4f")} or {"{:.2e}".format(t)} in scientific notation\n{date.today().strftime("%b %d %Y")}')