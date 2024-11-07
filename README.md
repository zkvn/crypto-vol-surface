# Overview
- Purpose: The demo is inspired by two blogs that discuss the construction of volatility surfaces for Bitcoin, and it aims to implement these concepts in a minimalist Pythonic way. 
- I created this while preparing for a web3 interview. 


# Install and Run Deribit Volatility Surface
1. Clone this git to a local folder and CD into it
2. Create a virtual environment for all dependencies
`python -m venv "venv"`
3. Activate the virtual environment 
`source venv/bin/activate`  (linux/mac)
`./venv/scripts/activate`   (Windows)
4. Install the dependencies 
`python -m pip install -r requirements.txt`
5. Run the application 
    - To generate the volatility surface directly using the latest downloaded file, run
        - python app.py
    - To download data and generate the volatility surface, use the following command:
        - python app.py --download  


## Bonus: Run Binance Vol Surface
1. CD into the project folder
2. Activate the venv
`source venv/bin/activate`  (linux/mac)
`./venv/scripts/activate`   (Windows)
3. Run the application 
    - streamlit run app_streamlit.py


# Known Issues for Deribit Volatility Surface
- If there is a space in the path of the Python program folder, plotly will have issues saving static image to output folder. A workaround is to set an environment variable. More details can be found here.
    - https://github.com/plotly/Kaleido/issues/78



# References
- [The SVI Model - A Tutorial](https://sellersgaard.github.io/blog/2023/svi/)
- [Crypto Volatility Surface](https://joshuapjacob.com/crypto-volatility-surface/)

