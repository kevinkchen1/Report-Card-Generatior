file = open('StudentInfo.tsv', 'r')
lines = file.readlines()

grades = []
all_mid1 = []
all_mid2 = []
all_final = []
for line in lines:
    seperate = line.split()
    midterm1 = int(seperate[2])
    all_mid1.append(midterm1)
    midterm2 = int(seperate[3])
    all_mid2.append(midterm2)
    final = int(seperate[4])
    all_final.append(final)
    scores = []
    for index in range(2,5):
            score = 0
            score += int(seperate[index])
            scores.append(score)
            if(len(scores)) == 3:
                avg = sum(scores)/len(scores)
                if avg >= 90:
                    grades.append('A')
                elif avg >= 80:
                    grades.append('B')
                elif avg >= 70:
                    grades.append('C')
                elif avg >= 60:
                    grades.append('D')
                elif avg < 60:
                    grades.append('F')

mid1_avg = sum(all_mid1)/len(all_mid1)
mid2_avg = sum(all_mid2)/len(all_mid2)
final_avg = sum(all_final)/len(all_final)
count = -1
for line in lines:
    count += 1
    no_newline = line.strip()
    print(no_newline, end = ':  ') 
    print(grades[count])
print()
print(f'Averages: midterm1 {mid1_avg:.2f}, midterm2 {mid2_avg:.2f}, final {final_avg:.2f}\n')
