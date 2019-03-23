# ascii-sell

ascii-sell is an implementation of mbway qr-codes in ascii for use in low resolution terminals

![demo gif](https://raw.githubusercontent.com/lapisdecor/ascii-sell/master/ascii-sell.gif)

## How it works

We use python and the SIBS API. We call terminal commands to process the request for payment. We use the given image of the original QR code, get the token from the image and create a new QR code in ascii. The user will then scan the QR-code using MBWAY and the script completes the transaction.


## Requirements

    Please install:
    - python3-dev
    - libzbar-dev

Create a virtual environment with:

```python3 -m venv venv```

Start the virtual environment with

```. venv/bin/activate```

Install the requirements

```pip install requirements.txt```

## Usage

Change to the ascii-sell directory.

Start a terminal and write:

```./ascii-sell amount```

where ```amount``` is the money you whant to charge.