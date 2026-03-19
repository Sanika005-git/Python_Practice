class Date:
    def _init_(self):
        print('Entered Date._init_()')
        print('type(self):', type(self))
        print('id(self):', id(self))
        print('Leaving Date._init_()')


D1 = Date()
print('type(D1):', type(D1))
print('id(D1):', id(D1))
D2 = Date()
print('type(D2):', type(D2))
print('id(D2):', id(D2))
