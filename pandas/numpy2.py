import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.arange(12).reshape(3,4),
    columns=['A','B','C','D']
)

df.drop("A",axis=1,inplace=True)
df.drop(index=1,axis=0,inplace=True) # 或者直接写1
print(df)