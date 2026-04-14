# Ethereum Whale Analysis

## Overview
Analysis of large-volume traders ("whales") on Ethereum DEXs using real on-chain data.  
The goal is to identify trading patterns, dominant wallets, and market activity trends.

## Live Demo
🚀 **[Open Interactive Dashboard](https://ethereum-whale-analysis-ytsjvfizz4sd6shprp5aec.streamlit.app/)**

## Key Insights
- A small number of wallets account for a significant share of total trading volume  
- Trading activity is concentrated around specific time windows  
- Certain tokens consistently dominate high-value transactions  

## Features
- Top 10 whale wallets by trading volume  
- Most traded tokens by whales  
- Hourly trading activity distribution  
- Adjustable filter for minimum trade size  

## Tech Stack
- Python  
- Pandas  
- Matplotlib  
- Streamlit  
- Dune Analytics API  

## Data
- Source: Dune Analytics  
- Scope: 1,000 largest DEX trades  
- Timeframe: last 7 days  
- Filter: trades ≥ $100,000  

