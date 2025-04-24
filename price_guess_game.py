
import streamlit as st

# Page config
st.set_page_config(page_title="House Price Guessing Game", layout="wide")
st.title("🏠 Guess the Price - Real Estate Challenge")

# Images and layout
st.subheader("🏘️ Neighborhood and Location")
col1, col2 = st.columns(2)
with col1:
    st.image("genel_konum.webp", caption="📍 Ames, Iowa - General Region", use_column_width=True)
with col2:
    st.image("konum.webp", caption="🏡 Northridge Heights Neighborhood", use_column_width=True)

st.subheader("📐 Floor Plan")
st.image("plan.webp", caption="House Layout Plan", use_column_width=True)

st.subheader("🛠️ Key Areas - Photos")
st.image("garaj.webp", caption="🚗 Garage - 2 Car Space", use_column_width=True)
st.image("mutfak.webp", caption="🍽️ Kitchen - Good Quality Finish", use_column_width=True)
st.image("odalar.webp", caption="🛏️ Bedrooms and Bathrooms", use_column_width=True)
st.image("ev_genel.webp", caption="🏠 Exterior View of the House", use_column_width=True)

# House features
description = """
### 📋 House Features
- **3 bedrooms**, **2 bathrooms**  
- **1,480 sqft (~137 m²)** living space  
- **Built in 2003**, **renovated in 2009**  
- **Neighborhood:** NAmes  
- **Exterior:** Vinyl Siding + Brick Face  
- **Finished Basement (GLQ)**  
- **Gas Heating (GasA)**  
- **Kitchen Quality:** Good (Gd)  
- **2-car garage**, 620 sqft  
- **252 sqft wooden deck**, **73 sqft patio**, **Wooden fence**, **shed**
"""
st.markdown(description)

# Guess input
st.subheader("💬 Enter your price guess (USD)")
guess = st.slider("What do you think this home sold for in 2010?", min_value=150000, max_value=550000, step=1000)

# Real price
actual_price = 214000
diff = guess - actual_price

# Feedback logic
st.subheader("🔍 Feedback")
if abs(diff) <= 5000:
    st.success("👏 Incredible! You were nearly spot on.\n\nThis level of accuracy can save thousands in time, negotiations, and decision-making. You're clearly tuned into what makes a property valuable 👀")
elif diff < -10000:
    st.error(f"😟 Your guess was ${abs(diff):,} below the actual price.\n\nIf this home had been listed at your price, the seller could have taken a loss. Did you overlook the finished basement, garage, or kitchen quality?")
elif diff > 10000:
    st.warning(f"⏳ That’s quite high!\n\nOverpricing by ${abs(diff):,} can result in longer time on market, interest, taxes, and markdown pressure. Buyers may lose interest.")
else:
    st.info("🔍 Close guess!\n\nYou're within a realistic negotiation margin. Great effort!")
