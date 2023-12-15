import csv
dict1={'Name':'sl','Age':21,'Course':'MCA'}
file1=input("Enter file name:")
csvfile=open(file1,'w',newline="")
csvwrite=csv.DictWriter(csvfile,fieldnames=dict1.keys())
csvwrite.writeheader()
csvwrite.writerow(dict1)
csvfile.close()
csvfile=open(file1,'r')
csvread=csv.reader(csvfile)
for i in csvread:
    print(i)
csvfile.close()
