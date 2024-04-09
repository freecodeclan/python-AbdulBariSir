profile = {
    'sde1': {
        'lang' : 'Java',
        'exper' : 3,
        'role' : 'backend'
    },
    'sde2' : {
        'lang' : 'JavaScript',
        'exper' : 3,
        'role' : 'front-end'
    },
    'sde3' : {
        'lang' : 'Python',
        'exper' : 5,
        'role' : 'AI Egineer'
    }
}
print(profile)

# Accessing items in nested Dictionary
print(profile['sde1']['exper'])

print()
# Loop through Dictionary
for x, obj in profile.items():
    print(x)

    for y in obj:
        print(y + ':', obj)