import streamlit as st
import os

st.set_page_config(page_title="Guess the Price - Real Estate", layout="centered")

st.title("🏠 Guess the Price - Real Estate Challenge")

# 🏡 House Features Section
st.header("🏡 House Features")
st.markdown("""
- **Room Count**: 3 bedrooms, 2 bathrooms  
- **Living Area**: 1,480 sqft (~137 m²)  
- **Year Built**: 2003 (Renovated in 2009)  
- **Neighborhood**: Northridge Heights, Ames, Iowa  
- **Garage**: 2-car garage (620 sqft)  
- **Deck / Outdoor**: 252 sqft deck + 73 sqft patio  
""")

# 📸 Images with safe loading (optional but recommended)
st.header("🏘️ Neighborhood and Location")

image_files = {
    "konum.webp": "📍 Ames, Iowa - General Region",
    "ev_genel.webp": "🏠 House Exterior",
    "mutfak.webp": "🍽️ Kitchen",
    "odalar.webp": "🛏️ Rooms",
    "garaj.webp": "🚗 Garage",
    "dış.webp": "🌳 Backyard / Garden",
    "plan.webp": "📐 Floor Plan"
}

for filename, caption in image_files.items():
    if os.path.exists(filename):
        st.image(filename, caption=caption, use_container_width=True)
    else:
        st.warning(f"⚠️ Missing file: {filename}")

# 💸 User Input for Price Guess
st.subheader("💸 Enter Your Price Guess")
user_price = st.number_input("Your guess (in USD):", min_value=0, step=1000)

# 🎯 Real Price (kept hidden in game logic)
real_price = 214000

if st.button("🎯 Make a Guess"):
    diff = abs(user_price - real_price)

    if diff <= 5000:
        st.success("🏆 *Incredible!* You guessed almost spot on!\nYou must have a sixth sense for real estate deals 🧠💰")
        st.image("https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif", caption="👏 Amazing guess!")
        
    elif user_price < real_price:
        st.warning("📉 *Too Low!* You just undersold a gem!\nThis house is more valuable than that 💎")
        st.image("https://media.giphy.com/media/xT5LMzikV2WcZRzCBK/giphy.gif", caption="Oops... it's more expensive!")

    else:
        st.warning("📈 *Too High!* Easy there, billionaire! 💸\nTurns out this one's a better deal than you thought 😉")
        st.image("https://media.giphy.com/media/3o7abldj0b3rxrZUxW/giphy.gif", caption="That guess was way over!")

