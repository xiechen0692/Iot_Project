import js2py

data=open('sendImage.js','r',encoding= 'utf8').read()
print(type(data))
data=js2py.eval_js(data)
# print(data('1234569'))