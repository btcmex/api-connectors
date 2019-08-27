import btcmex

client = btcmex.btcmex(test=True, api_key="u_api_key", api_secret="u_api_secret")
print(client.Order)

# place order
try:
    result = client.Order.Order_new(symbol="XBTUSD", orderQty=2, price=10815).result()
    print(result)
except Exception as e:
    if hasattr(e, 'status_code'):
        print('---Exception:%s---status_code:%s---message:%s' % (repr(e), e.status_code, e.response.text))
    else:
        print(str(e))
