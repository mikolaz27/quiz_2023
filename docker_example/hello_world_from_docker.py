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

# docker run --rm -it -d -p 8010:8000 -v D:\Hillel\quiz_2023\src\:/quizez/src --name quiz_cont  quiz_image
# CMD ["python", "src/manage.py", "runserver", "0:8000"]

# docker build  -t quiz_image .
