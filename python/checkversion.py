#print('Hello people')
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  def wrap_fn(user1):
    if user1['valid']:
      print('valid')
      return fn(user1)
      print('very valid')
    #else:
      #print ('invalid')
  return wrap_fn
  # code here

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)