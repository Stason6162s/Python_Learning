import V_Modules.a as mod

print("Path ", mod.myrange)
print('Dict', mod.__dict__['myrange'])
print('Get atr', (getattr(mod, 'myrange')))
