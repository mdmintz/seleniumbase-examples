import gc
import glob
import os
import tempfile
from seleniumbase import sb_cdp

tmp = tempfile.gettempdir()
print(tmp)


def uc_count():
    return len(glob.glob(os.path.join(tmp, "uc_*")))


for i in range(1, 6):
    sb = sb_cdp.Chrome("about:blank")
    sb.quit()
    gc.collect()
    print(f"after run {i}: uc_* temp dirs = {uc_count()}")
