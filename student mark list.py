##student Mark list
T=int(input("Enter the mark tamil"))
E=int(input("Enter the mark english"))
M=int(input("Enter the mark maths"))
S=int(input("Enter the mark science"))
SS=int(input("Enter the mark socialscience"))
print("Tamil=",T,"\nEnglish=",E,"\nMaths=",M,"\nScience=",S,"\nsocialscience=",SS)
total=T+E+M+S+SS
per=(total/500)*100
print("Total=",total)
print("Percentage=",per)
