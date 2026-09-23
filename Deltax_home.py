"""
import Deltax_DataBase
from sklearn import tree

x = []
y = []
ListData = Deltax_DataBase.ListData()
for data in ListData:
    x.append([data[1],data[2],data[3],data[4],data[7],data[8]])
    y.append(data[5])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)
"""
import Deltax_DataBase

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

# دریافت داده‌ها
ListData = Deltax_DataBase.ListData()

X = []
y = []

for data in ListData:
    # استخراج محله
    address = data[1]
    parts = address.split("،")

    if len(parts) >= 2:
        region = parts[1].strip()
    else:
        region = address

    features = data[7]

    has_elevator = int("آسانسور" in features and "آسانسور ندارد" not in features)
    has_parking = int("پارکینگ" in features and "پارکینگ ندارد" not in features)
    has_storage = int("انباری" in features and "انباری ندارد" not in features)

    X.append([
        region,         # محله
        data[2],        # متراژ
        data[3],        # سال ساخت
        data[4],        # تعداد اتاق
        has_elevator,
        has_parking,
        has_storage
    ])

    # قیمت کل
    y.append(data[6])

# ستون 0 (محله) متنی است
preprocessor = ColumnTransformer(
    transformers=[
        (
            "region",
            OneHotEncoder(handle_unknown="ignore"),
            [0]
        )
    ],
    remainder="passthrough"
)

model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ))
])

model.fit(X, y)

print("Model trained successfully")

# تست پیش‌بینی
sample = [[
"ستارخان",   # محله
    100,       # متراژ
    1405,      # سال ساخت
    2,         # اتاق
    1,         # آسانسور
    1,         # پارکینگ
    1          # انباری
]]

predicted_price = model.predict(sample)
flor_area = sample[0][1]
print(f"Predicted Price per meter: {predicted_price[0]:,.0f} Price : {flor_area*(predicted_price[0]):,.0f}")