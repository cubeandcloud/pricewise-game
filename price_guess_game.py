import streamlit as st

st.set_page_config(page_title="Guess the Price - Real Estate", layout="centered")

st.title("🏠 Guess the Price - Real Estate Challenge")

# 🏡 House Features Section (comes before images)
st.header("🏡 House Features")
st.markdown("""
- **Room Count**: 3 bedrooms, 2 bathrooms  
- **Living Area**: 1,480 sqft (~137 m²)  
- **Year Built**: 2003 (Renovated in 2009)  
- **Neighborhood**: Northridge Heights, Ames, Iowa  
- **Garage**: 2-car garage (620 sqft)  
- **Deck / Outdoor**: 252 sqft deck + 73 sqft patio  
""")

# 📸 Image Section
st.header("🏘️ Neighborhood and Location")
st.image("genel_konum.webp", caption="📍 Ames, Iowa - General Region", use_container_width=True)
st.image("ev_dis.webp", caption="🏠 House Exterior", use_container_width=True)
st.image("mutfak.webp", caption="🍽️ Kitchen", use_container_width=True)
st.image("banyo.webp", caption="🛁 Bathroom", use_container_width=True)

# 💰 User Input Area
st.subheader("💸 Enter Your Price Guess")
user_price = st.number_input("Your guess (in USD):", min_value=0, step=1000)

# 🎯 Real Price (kept hidden)
real_price = 214000

# 🚀 Result Button
if st.button("🎯 Make a Guess"):
    diff = abs(user_price - real_price)

    if diff <= 5000:
        st.success("👏 Spot on! Your estimate is almost perfect.\nYou could save buyers and sellers both time and money.")
    elif user_price < real_price:
        st.warning("⬇️ Your guess is too low. This house is actually more expensive.")
    else:
        st.warning("⬆️ Your guess is too high. This house costs less than your estimate.")
