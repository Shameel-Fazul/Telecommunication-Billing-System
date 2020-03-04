# Customer Billing System #

def BillingSystem(CustomerName,PackageType,TotalGBUsed):
 StandardCustomer=1500
 StandardQuota=25
 PremiumCustomer=2500
 PremiumQuota=50

 # Standard Customer Statement
 
 if (PackageType=="Standard") or (PackageType=="standard"):
    if (TotalGBUsed > StandardQuota):
        ExcessGB=TotalGBUsed-StandardQuota
        ExcessCharge=ExcessGB * 250

        TotalCharge=StandardCustomer+ExcessCharge

        print("→ Customer Name                         : " + CustomerName)
        print("→ Package Type                          : " + PackageType)
        print("→ Standard Package Charge               : " + str(StandardCustomer))
        print("→ Excess Charge for excess "+str(ExcessGB)+" GB used    : " + str(ExcessCharge))
        print("→ Total Charge                          : " + str(TotalCharge))
        print("_____________________________________________________________________")
        print("                      ~ NEXT CUSTOMER ~                              ")
        print("=====================================================================")

    else:
        print("→ Customer Name                         : " + CustomerName)
        print("→ Package Type                          : " + PackageType)
        print("→ Standard Package Charge               : " + str(StandardCustomer))
        print("→ Total GB Used                         : " + str(TotalGBUsed))
        print("→ Excess Charge                         : 0")
        print("→ Total Charge                          : " + str(StandardCustomer))
        print("_____________________________________________________________________")
        print("                      ~ NEXT CUSTOMER ~                              ")
        print("=====================================================================")

 # Premium Customer Statement

 elif (PackageType=="Premium") or (PackageType=="premium"):
    if (TotalGBUsed > PremiumQuota):
        ExcessGB=TotalGBUsed-PremiumQuota
        ExcessCharge=ExcessGB * 250

        TotalCharge=PremiumCustomer+ExcessCharge

        print("→ Customer Name                         : " + CustomerName)
        print("→ Package Type                          : " + PackageType)
        print("→ Premium Package Charge                : " + str(PremiumCustomer))
        print("→ Excess Charge for excess "+str(ExcessGB)+" GB used   : " + str(ExcessCharge))
        print("→ Total Charge                          : " + str(TotalCharge))
        print("_____________________________________________________________________")
        print("                      ~ NEXT CUSTOMER ~                              ")
        print("=====================================================================")

    else:
        print("→ Customer Name                         : " + CustomerName)
        print("→ Package Type                          : " + PackageType)
        print("→ Premium Package Charge                : " + str(PremiumCustomer))
        print("→ Total GB Used                         : " + str(TotalGBUsed))
        print("→ Excess Charge                         : 0")
        print("→ Total Charge                          : " + str(PremiumCustomer))
        print("_____________________________________________________________________")
        print("                      ~ NEXT CUSTOMER ~                              ")
        print("=====================================================================")

x=0
while(x < 1):
   CName=input("[!] Enter Customer Name : ")
   PType=input("[!] Customer Package Type : ")
   TotGB=int(input("[!] Total GB used by Customer : "))
   print("---------------------------------------------------------------------")
   print("                      [ "+CName+"'s BILL ]                             ")
   print("---------------------------------------------------------------------")
   BillingSystem(CName,PType,TotGB)





          



    


