import streamlit as st
import os

st.set_page_config(page_title="Guess the Price - Real Estate", layout="centered")

st.title("🏠 Guess the Price - Real Estate Challenge")

# 🏡 House Features Section
st.header("🏡 House Features")
st.markdown("""
- **Room Count**: 3 bedrooms, 2 bathrooms  
- **Living Area**: 137 m²  
- **Year Built**: 2003 (Renovated in 2009)  
- **Neighborhood**: Northridge Heights, Ames, Iowa  
- **Garage**: 2-car garage (57 m²)  
- **Deck / Outdoor**: 24 m² deck + 7 m² patio  
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
        st.image("https://media.tenor.com/lW9bOeVpCs0AAAAC/that-is-the-best-answer-weve-had-simon-cowell.gif", caption="👏 Perfect answer!")
        
    elif user_price < real_price:
        st.warning("📉 *Too Low!* You just undersold a gem!\nThis house is more valuable than that 💎")
        st.image("https://media.tenor.com/YOtJ0DMyc6oAAAAC/office-the-insulting.gif", caption="😬 That was a bit insulting...")

    else:
        st.warning("📈 *Too High!* Whoa! That’s a sky-high guess! 💸\nAt that price, the house might still be on sale when you’re retired 😅")
        st.image("https://media.tenor.com/UlD6LXPckBMAAAAC/very-high-gill-engvid.gif", caption="⏳ Hope you're patient...")

