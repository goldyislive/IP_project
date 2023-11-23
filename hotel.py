import pandas as pd

# data given below for making dataframe

d = {
"Name": pd.Series(['jack','rose','raj','adam']),
"Age": pd.Series([20,24,19,40]),
"room-size": pd.Series(['small','midium','small','large']),
"No-of-days": pd.Series([5,3,6,9]),
"Cost": pd.Series([1500,2100,1800,9000])
}
hotel=pd.DataFrame(d)
print(hotel)

#dataframe making done

op = input("operations to perform: \n 1. Adding rows \n 2. Deleting rows \n 3. Updating rows\n")

# ADDING ROW
if op == "1":
    name=input("enter your Name: ")
    age=input("enter your Age: ")
    print("Available room sizes:\n 1. small (₹300/day)\n 2. medium (₹700/day)\n 3. large (₹1000/day)")
    rm=input("enter your room-size: ")
    days=int(input("enter how many days you want to stay: "))

    if rm == "1":
        rmc=300
        rm = "small"
    if rm == "2":
        rmc=700
        rm = "meduim"
    if rm == "3":
        rmc=1000
        rm = "large"
    cost=days*rmc
    hotel.loc[len(hotel.index)]=[name,age,rm,days,cost]
    print("new row added 👍")
    print(hotel)
# DELETING ROW
if op == "2":
    dele=int(input("which row you want to delete 🛑 : "))
    hotel = hotel.drop(hotel.index[dele],axis=0)
    print(hotel)
# UPDATING ROWS
if op == "3":
    rr=int(input("enter at which row value should be updated: "))
    cc=input("enter at which column value should be updated: ")
    vv=input("enter the value should be updated: ")
    hotel.at[rr,cc]=vv
    print(hotel)