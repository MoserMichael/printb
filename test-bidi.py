import printb

# visual studio code is a bit messad up with bidi support. 
# open issue since 2016 https://github.com/microsoft/vscode/issues/11770
# a workaround is to put bidi text into separate variables

heb="שלום לכולם"
heb2="שלום world"

printb.printb( heb, 42 )
printb.printb( heb2, 42 )

heb3="""הרבה many
שורות lines
של of
תוכנית code"""

printb.printb(heb3)

#print(heb)
#print(heb2)

printb.inputb(" :תכנניסו מספר בבקשה")

