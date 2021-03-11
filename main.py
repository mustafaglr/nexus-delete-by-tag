import pandas as pd
import os

df = pd.read_csv('id.txt', delimiter = ",")

df["number"] = df.version
df["branch"] = df.version

NEXUS_URL=""
USERNAME=""
PASSWORD=""

k = 0
for ver in df.version:
    if ver.__contains__("-"):
        df.number[k] = ver.split("-")[1]
        df.branch[k] = ver.split("-")[0]
    else:
        df.number[k] = ver
        df.branch[k] = ver
    k+=1

df.drop(df[df.number.str.contains("[A-Za-z]|\.")].index,inplace=True)
df.number = pd.to_numeric(df.number)
sorted = df.sort_values(by=['app','branch','number'])

counted = sorted.groupby(['app','branch']).size()
grouped = sorted.groupby(['app','branch'])


def deleteByID(index):
    os.system("curl -X DELETE 'http://"+NEXUS_URL+"/service/rest/v1/components/"+index+"' -u "+USERNAME+":"+PASSWORD+" -H 'accept: application/json'")

imageCount = 0
i = 0
for (group_name, df_group) in grouped:

    if counted[i] > 5:
        imageCount = counted[i]
        for row_index, row in df_group.iterrows():
            imageCount = imageCount - 1
            if imageCount == 4:
                break
            print(row_index, "--",row["app"], "--",row["version"])
            deleteByID(row["id"])

    i = i +1
