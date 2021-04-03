import csv
with open('st.csv', 'w')as f:
    w = csv.writer(f,
                  delimiter= ',')
    w.writerow(['one',
                'two',
                'tree'])
    w.writerow(['foo',
                'five',
                'sex'])
    
    