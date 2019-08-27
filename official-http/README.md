# Python client

## Installation

```
$ pip install bravado
```

## Quickstart

This is an introduction on how to get started with BTCMEX. First, make sure the bravado library is installed.

The next thing you need to do is import the library and get an instance of the client:

```
import btcmex
client = btcmex.btcmex()
```

###  Clients authenticate

To get an authenticated client instance:

```
import btcmex
client = btcmex.btcmex(api_key=<YOUR API KEY>, api_secret=<YOUR API SECRET>)
```

### example

There is an example in [main.py] that contains all the existing situations. use this to run the example 

```
python3 main.py
```

## order usage

### Placing orders

```
result = client.Order.Order_new(symbol="XBTUSD", orderQty=1, price=6000.0).result()
```

### Amending orders

```
result = client.Order.Order_amend(orderID="1131088652118523906", orderQty=3).result()
```

### Canceling orders

An order can be canceled given the order ID:

```
client.Order.Order_cancel(orderID="1131088652118523906").result()
```

You can cancel all open orders:

```
client.Order.Order_cancelAll(symbol="XBTUSD").result()
```

## position usage

### Inquire position

```
client.Position.Position_get().result()
```

### Amend leverage

```
result = client.Position.Position_updateLeverage(leverage=25, symbol="XBTUSD").result()
```

### Amend riskLimit

An order can be canceled given the order ID:

```
client.Position.Position_updateRiskLimit(riskLimit=30000000000, symbol="XBTUSD").result()
```

### Amend margin

```
client.Position.Position_transferIsolatedMargin(amount=-10000, symbol="XBTUSD").result()
```

## User usage

### Inquire user margin

```
client.User.User_getMargin(currency="XBT").result()
```
