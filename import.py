import writeas
import writefreely

# PUT IN VALUES BEFORE RUNNING SCRIPT
# WRITE.AS VALUES
# Username and password for your Write.as account
username = ''
password = ''
# The Write.as slug for your blog - ex: write.as/matt -> 'matt'
collection = ''

# WRITEFREELY VALUES
# Domain of the WriteFreely instance - ex: write.house/bix -> 'write.house'
domain = ''
# The WriteFreely slug for the blog = ex: write.house/bix -> 'bix'
wfcollection = ''

# Instanciate Write.as Client
c = writeas.client()

# Log in with Write.as
user = c.login(username, password)
c.setToken(user['access_token'])

# Instantiate WriteFreely client
wf = writefreely.client(domain)

list = []

# I assume 500 posts is more than generous!
for i in range(1,50):
# Iterate through the pages...
    cposts = wf.retrieveCPosts(wfcollection, i)
    posts = cposts['posts']
# If the posts are not an empty list, take each post and put it in a list!
# That way it catches pages that don't have 10 posts
    if posts != []:
        for post in posts:
# Append to the list of posts
            list.append(post)

    else:
        break

for p in list:
    title = p['title']
    body = p['body']
    created = p['created']
    tags = p['tags']

    c.createCPost(collection, body, title, created=created, tags=tags)

coll = c.retrieveCollection(collection)

print('Finished! Below is your imported blog\n\n{}'.format(coll))
