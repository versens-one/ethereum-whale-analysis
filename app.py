import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('whales_data.csv')
df['amount_usd'] = df['amount_usd'].astype(float)
df['block_time'] = pd.to_datetime(df['block_time'])

# Title
st.title('🐋 Ethereum Whale Dashboard')
st.markdown('Analysis of largest DEX trades on Ethereum — last 7 days')

# Metric cards
col1, col2, col3 = st.columns(3)
col1.metric('Total Transactions', len(df))
col2.metric('Total Volume', f"${df['amount_usd'].sum()/1e9:.1f}B")
col3.metric('Avg Trade Size', f"${df['amount_usd'].mean()/1e6:.1f}M")

# Filter
min_amount = st.slider('Minimum trade size ($M)', 0, 20, 1)
df_filtered = df[df['amount_usd'] >= min_amount * 1e6]

# Chart 1 - Top whales
st.subheader('Top 10 Whales by Volume')
whales = df_filtered.groupby('wallet')['amount_usd'].sum().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh([w[:10]+'...' for w in whales.index], whales.values/1e6, color='steelblue')
ax.set_xlabel('Volume ($M)')
plt.tight_layout()
st.pyplot(fig)

# Chart 2 - Top tokens
st.subheader('Top Tokens by Volume')
tokens = df_filtered.groupby('token')['amount_usd'].sum().sort_values(ascending=False).head(10)
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.barh(tokens.index, tokens.values/1e6, color='coral')
ax2.set_xlabel('Volume ($M)')
plt.tight_layout()
st.pyplot(fig2)

# Chart 3 - Hourly activity
st.subheader('Hourly Trading Activity')
df_filtered['hour'] = df_filtered['block_time'].dt.hour
hourly = df_filtered.groupby('hour')['amount_usd'].sum()
fig3, ax3 = plt.subplots(figsize=(10, 4))
ax3.bar(hourly.index, hourly.values/1e6, color='mediumpurple')
ax3.set_xlabel('Hour (UTC)')
ax3.set_ylabel('Volume ($M)')
plt.tight_layout()
st.pyplot(fig3)