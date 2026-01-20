import sys
print("arguments:", sys.argv)

day = int(sys.argv[1])
print(f"Running pipeline for day {day}")

import pandas as pd

df = pd.DataFrame({
    'A': range(5),
    'B': range(5, 10)
})

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")