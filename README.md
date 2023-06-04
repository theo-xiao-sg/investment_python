# Backtesting a well known investment stratergy with python

I backtested a well know investment stratergy with python called SMA 200 to find out if it is really worth its value. 
Please read my project description here: https://theo-xiao-sg.github.io/investment.html
 
## Running Guide

This project is based on the Python programming language and primarily utilizes standard libraries like yfinance, datetime, matplotlib and os

### Environment Setup

Download the requirements.txt and install the required Python libraries. Please note all my 4 projects share the same requirements.txt. If you have done the installation for one project, you can skip it for the other 3 projects

```bash
# install all packages using requirements.txt
python -m pip install -r requirements.txt
```

### Trying it out
* Run `moving_average_main.py` in the folder, a few images will be saved in the folder of "images"
* Feel free to change the ticker to any other stocks (in line 14-21) and the SMA days (in line 41) you like and see the results. However, the conclusion still hold: SMA is not as profitable as many investment gurus claim.
