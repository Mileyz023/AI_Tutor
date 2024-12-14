import pandas as pd
import matplotlib.pyplot as plt

file_path = 'experiment result.csv'
data = pd.read_csv(file_path)

def clean_numeric_data(df, columns):
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

competence_masculine = ["Q4_1", "Q5_1", "Q6_1", "Q7_1", "Q11_1"]
competence_feminine = ["Q4_2", "Q5_2", "Q6_2", "Q7_2", "Q11_2"]
informativeness_masculine = ["Q8_1", "Q9_1", "Q10_1"]
informativeness_feminine = ["Q8_2", "Q9_2", "Q10_2"]
voice_AI = ["Q2"]

data_cleaned = clean_numeric_data(data, competence_masculine + competence_feminine + informativeness_masculine + informativeness_feminine + voice_AI)

# male_data = data_cleaned[data_cleaned["Q1"] == "Male"]
# female_data = data_cleaned[data_cleaned["Q1"] == "Female"]
male_data = data_cleaned[data_cleaned["Q2"] == 1]
female_data = data_cleaned[data_cleaned["Q2"] == 2]

male_competence_masculine_avg = male_data[competence_masculine].mean()
female_competence_masculine_avg = female_data[competence_masculine].mean()

male_competence_feminine_avg = male_data[competence_feminine].mean()
female_competence_feminine_avg = female_data[competence_feminine].mean()

male_informativeness_masculine_avg = male_data[informativeness_masculine].mean()
female_informativeness_masculine_avg = female_data[informativeness_masculine].mean()

male_informativeness_feminine_avg = male_data[informativeness_feminine].mean()
female_informativeness_feminine_avg = female_data[informativeness_feminine].mean()

competence_labels = ["Content", "Accuracy", "Format", "Knowledgeable", "Improved Score"]
informativeness_labels = ["Chose Facts", "Ease of Learning", "Helped Understanding"]

x = range(len(competence_labels))
plt.figure(figsize=(10, 6))
plt.bar(x, male_competence_masculine_avg, width=0.4, label="Male Voice", alpha=0.7, color='blue')
plt.bar([p + 0.4 for p in x], female_competence_masculine_avg, width=0.4, label="Female Voice", alpha=0.7, color='orange')
plt.xticks([p + 0.2 for p in x], competence_labels, rotation=20)
plt.title("Competence Ratings for Masculine Topics")
plt.ylabel("Competence Rating")
plt.ylim(0, 10)
plt.legend()
plt.tight_layout()
plt.show()

# Competence (Feminine)
x = range(len(competence_labels))
plt.figure(figsize=(10, 6))
plt.bar(x, male_competence_feminine_avg, width=0.4, label="Male Voice", alpha=0.7, color='blue')
plt.bar([p + 0.4 for p in x], female_competence_feminine_avg, width=0.4, label="Female Voice", alpha=0.7, color='orange')
plt.xticks([p + 0.2 for p in x], competence_labels, rotation=20)
plt.title("Competence Ratings for Feminine Topics")
plt.ylabel("Competence Rating")
plt.ylim(0, 10)
plt.legend()
plt.tight_layout()
plt.show()

# Informativeness (Masculine)
x = range(len(informativeness_labels))
plt.figure(figsize=(10, 6))
plt.bar(x, male_informativeness_masculine_avg, width=0.4, label="Male Voice", alpha=0.7, color='blue')
plt.bar([p + 0.4 for p in x], female_informativeness_masculine_avg, width=0.4, label="Female Voice", alpha=0.7, color='orange')
plt.xticks([p + 0.2 for p in x], informativeness_labels, rotation=20)
plt.title("Informativeness Ratings for Masculine Topics")
plt.ylabel("Informativeness Rating")
plt.ylim(0, 10)
plt.legend()
plt.tight_layout()
plt.show()

# Informativeness (Feminine)
x = range(len(informativeness_labels))
plt.figure(figsize=(10, 6))
plt.bar(x, male_informativeness_feminine_avg, width=0.4, label="Male Voice", alpha=0.7, color='blue')
plt.bar([p + 0.4 for p in x], female_informativeness_feminine_avg, width=0.4, label="Female Voice", alpha=0.7, color='orange')
plt.xticks([p + 0.2 for p in x], informativeness_labels, rotation=20)
plt.title("Informativeness Ratings for Feminine Topics")
plt.ylabel("Informativeness Rating")
plt.ylim(0, 10)
plt.legend()
plt.tight_layout()
plt.show()