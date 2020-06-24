finalPer = []
a = "You have received Tk 3000.00 from 01742724997. Ref 3000. Fee Tk 0.00. Balance TK 3,021.00. TrxID 7CH6U761AM at 17/03/2020 12:41."
b = a.split(". ")
print(b)

recivedMoney = ((b[0].split("You have received Tk "))[1].split(" from 01742724997"))[0]

ref = (b[1].split("Ref"))[1]

newBalance = (b[3].split("Balance TK"))[1]

TrxID = ((b[4].split("TrxID"))[1]).split("at 17/03/2020 12:41.")[0]

date = ((((b[4].split("TrxID"))[1]).split(TrxID)[1]).split("at "))[1]

finalPer = recivedMoney, ref, newBalance, TrxID, date

print(finalPer)