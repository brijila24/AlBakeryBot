import streamlit as st
from menu_loader import load_menu
from llm_utils import send_message_tollm,start_session


#UI
st.title("Home Bakery AI Assistant")
st.markdown("Homemade cakes| Serving Dubaai and Sharjah since 2011|Payment on Delivery")

#to load menu 
cake_menu = load_menu()

# menu_text=""
# for name, price in cake_menu.items():
#     menu_text = menu_text + f"-{name}: AED {price}\n\n"
# st.markdown(menu_text)

if "messages" not in st.session_state:
    start_session()
    welcome_message=(
        "Hi there !Welcome to Brij's Home Bakery\n\n"
        "Here is our menu:\n\n"
        +cake_menu
        +"\n Would you like to place an order or have any questions about our cakes? 🍰"
    )
    st.session_state.messages = [
        {"role": "Assistant", "content": welcome_message}
    ]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
user_input = st.chat_input("Enter your message here...")
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append(
        {"role": "user",
          "content": user_input})
    llm_response = send_message_tollm(user_input)
    with st.chat_message("assistant"):
        st.markdown(llm_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": llm_response}
    )
    # # Here you can add your code to generate a response from the AI model
    # # For demonstration, we'll just echo the user's input
    # ai_response = f"AI Response to: {user_input}"
    # st.session_state.messages.append({"role": "assistant", "content": ai_response})

