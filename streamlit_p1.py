import streamlit as st

st.title("Grocery budget calculator")
st.header("Grocery List")

if 'grocery_list' not in st.session_state:
    st.session_state.grocery_list=[]

item=st.text_input("Add grocery item")

if st.button("add item"):
    if item:
        st.session_state.grocery_list.append(item)
        st.success(f"'{item}' added")
    else:
        st.warning("please enter u ")

st.subheader("list")
for i, grocery in enumerate(st.session_state.grocery_list):
    st.write(f"{i+1}.{grocery}")

st.header("Budget calculator")

budget=st.number_input("i have",min_value=0.0,format="%.2f")
st.subheader("prices for each grocery item")
prices=[]
for grocery in st.session_state.grocery_list:
    price = st.number_input(f"Price of {grocery}", min_value=0.0, format="%.2f", key=grocery)
    prices.append(price)

total=sum(prices)
leftamt=budget-total

st.subheader("Budget Summary")
st.write(f"Total Expenses: ${total:.2f}")
st.write(f"Remaining Budget: ${leftamt:.2f}")

if leftamt < 0:
    st.error("You have exceeded your budget!")





