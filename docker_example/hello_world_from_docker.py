import datetime
from time import sleep

import pandas as pd

while True:
    df = pd.DataFrame(
        data={
            "timestamp": [datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=7)],
            "col2": [3, 4],
        }
    )
    print(df)
    sleep(2)

# docker run --rm -it -d --name while_cont  while_image

# docker run --rm -it -d --name quiz_cont  quiz_image
