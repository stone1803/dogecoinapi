import json
import datetime
from block_io import BlockIo
v = 2
dogecoin = BlockIo('d068-adce-3ee1-41d7', 'hongphuc1109', v)
tkdoge = dogecoin.get_address_by_label(label='phucbun')
tkgd_doge_nhan = dogecoin.get_transactions(type='received', labels='phucbun')
tkgd_doge_gui = dogecoin.get_transactions(type='sent')
giadoge = dogecoin.get_current_price()
x = datetime.datetime.now()
print('-'*30)
print(x.strftime("%c"))

#print(vidoge.get())
def tkphuc():
  print('-'*30)
  print('Loại Coin :',tkdoge['data']['network'])
  print('-'*30)
  print('Địa chỉ ví của Phúc :',tkdoge['data']['address'])
  print('-'*30)
  print('Số dư  :',tkdoge['data']['available_balance'])
  print('-'*30)
  #print('Cặp BTC/DOGE :',giadoge['data']['prices'])

tkphuc()
