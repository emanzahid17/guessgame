import streamlit as st
import random

# Set the title of the app
st.title("User Guessing Game")

# Generate a random number between 1 and 100, if not already generated
if 'guess_num' not in st.session_state:
    st.session_state.guess_num = random.randint(1, 100)
if 'success' not in st.session_state:
    st.session_state.success = False

# Input box for the user's guess
entered_num = st.number_input("Enter a number between 1 and 100:", min_value=1, max_value=100, step=1)

# Button to submit the guess
if st.button("Submit Guess"):
    if entered_num > st.session_state.guess_num:
        st.write("Too high! Try again.")
    elif entered_num < st.session_state.guess_num:
        st.write("Too low! Try again.")
    else:
        st.success("Congratulations! You guessed the correct number.")
        st.session_state.success = True

if st.session_state.success:
        # Optionally, reset the game
        if st.button("Play Again"):
            # Generate a new random number
            st.session_state.guess_num = random.randint(1, 100)
            st.session_state.success = False
            # Clear the input
            st.experimental_rerun()

