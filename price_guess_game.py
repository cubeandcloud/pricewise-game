import streamlit as st

st.set_page_config(page_title="Guess the Price - Real Estate", layout="centered")

st.title("🏠 Guess the Price - Real Estate Challenge")

# 🏡 House Features
st.header("🏡 House Features")
st.markdown("""
- **Room Count**: 3 bedrooms, 2 bathrooms  
- **Living Area**: 1,480 sqft (~137 m²)  
- **Year Built**: 2003 (Renovated in 2009)  
- **Neighborhood**: Northridge Heights, Ames, Iowa  
- **Garage**: 2-car garage (620 sqft)  
- **Deck / Outdoor**: 252 sqft deck + 73 sqft patio  
""")

# 📸 Images
st.header("📸 Visual Tour")

st.image("house_images/genel_konum.webp", caption="📍 Ames, Iowa - General Region", use_column_width=True)
st.image("house_images/dış.webp", caption="🏠 Exterior View", use_column_width=True)
st.image("house_images/mutfak.webp", caption="🍽️ Kitchen", use_column_width=True)
st.image("house_images/odalar.webp", caption="🛏️ Rooms & Bathrooms", use_column_width=True)

# 💰 Price Guess Input
st.subheader("💸 Make Your Price Guess")
user_price = st.number_input("What do you think this house sold for? (in USD)", min_value=0, step=1000)

# 🎯 Real Price
real_price = 214000

# 🧠 Result Logic
if st.button("🎯 Submit Guess"):
    diff = abs(user_price - real_price)

    st.subheader("🔍 Feedback")
    if diff <= 5000:
        st.success("👏 Amazing! You're spot on.\nYour guess is almost perfect — this level of accuracy is rare.")
    elif user_price < real_price - 10000:
        st.warning(f"⬇️ Your estimate is **${real_price - user_price:,.0f}** too low.\nIf listed at this price, the seller could have faced a major loss.")
    elif user_price > real_price + 10000:
        st.warning(f"⬆️ Your estimate is **${user_price - real_price:,.0f}** too high.\nOverpricing could have led to longer time on market and lost buyers.")
    else:
        st.info("✅ Not bad! You're within a realistic negotiation margin.\nYou have a good sense of property value.")
