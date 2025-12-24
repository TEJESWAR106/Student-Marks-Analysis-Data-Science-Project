import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("marks.csv")
subjects = ["Math", "Science", "English"]  

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df["Total"] / len(subjects)

top_index = df["Total"].idxmax()
top_student = df.loc[top_index, "Student"]
top_total = df.loc[top_index, "Total"]
top_average = df.loc[top_index, "Average"]

print("Top Scorer:", top_student)
print("Top Scorer Total Marks:", top_total)
print("Top Scorer Average Marks:", top_average)

class_average = df["Average"].mean()
print("Class Average Marks:", class_average)

plt.figure(figsize=(10, 6))
plt.bar(df["Student"], df["Total"], color="skyblue")

plt.title("Total Marks per Student")
plt.xlabel("Student")
plt.ylabel("Total Marks")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("marks_graph.png")
print("Graph saved as marks_graph.png")

plt.show()
