import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# Generate data
index = pd.date_range('1/1/2000', periods=8)
data = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["测试1","测试2","测试3"])

# Get Chinese font
font = fm.FontProperties(fname="/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc")

# ================ Pandas DataFrame way ================
ax = data.plot()
# Set legend with Chinese font properties
ax.legend(prop=font)
# Show plot
plt.show()


# ================ Matplotlib way ================
fig, ax = plt.subplot()

ax.line()

