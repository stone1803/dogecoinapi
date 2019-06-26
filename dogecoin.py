import datetime
from block_io import BlockIo
import sys
import pyfiglet
v = 2
phucle = pyfiglet.figlet_format("PhucLe")
print(phucle)
dogecoin = BlockIo('d068-adce-3ee1-41d7', 'hongphuc1109', v)
tkdoge = dogecoin.get_address_by_label(label='phucbun')
tkgd_doge_nhan = dogecoin.get_transactions(type='received', labels='phucbun')
tkgd_doge_gui = dogecoin.get_transactions(type='sent')
giadoge = dogecoin.get_current_price()
x = datetime.datetime.now()

#print(vidoge.get())
def tkphuc():
  print('-'*50)

  print(x.strftime("%c"))

  print('-'*50)
  print('Loại Coin :',tkdoge['data']['network'])
  print('-'*50)
  print('Ví của Phúc :',tkdoge['data']['address'])
  print('-'*50)
  print('Số dư  :',tkdoge['data']['available_balance'])
  print('-'*50)
  #print('Cặp BTC/DOGE :',giadoge['data']['prices'])
def checkinput():
  try:
    if "." in user_input :
      val = float(user_input)
      print(val, "Yes, user input is a float number.")
    else:
      val = int(user_input)
      print(val, "Yes, input string is an Integer.")
  except ValueError:
       print("Đây là chữ không phải số")
def sotiengui(): 
  user_input = input("Enter  your Age : ")
  try:
    val = int(user_input)
    print("Yes input string is an Integer.")
    print("Input number value is: ", val)
  except ValueError:
    print("Đây là chữ đéo phải số")
    print("Nhập lại số tiền đi má")
tkphuc()
print('Để gửi vui lòng nhập chữ g ')
print('Để gửi vui lòng nhập chữ n ')
print('-'*50)
user_input = input('Vui lòng nhập Gửi hay Nhận :')
if user_input == 'n':
  print('-'*50)
  print('Địa chỉ ví :')
  print('A5zpsc9VrV29EiRvjL92uca2mQCc9xJEEz')
elif user_input == 'g':
  input("Vui lòng nhập số doge muốn gửi :")
  input('Địa chỉ ví muốn gửi :')
  checkinput()
while True:
  tkphuc()
  break