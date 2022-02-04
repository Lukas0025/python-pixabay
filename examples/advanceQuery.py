import pixabay.core

# init pixabay API
px = pixabay.core("YOUR API KEY")

# search for notebook, category: computers, color: black, minWidth 100px with safeSearch (more in https://pixabay.com/api/docs/)
notebooks = px.query(
    query      = "notebook",
    category   = "computers",
    color      = "black",
    minWidth   = "100",
    safeSearch = True
)

# get len of hits len(notebooks)
print("{} hits".format(len(notebooks)))

# get image id
print(notebooks[0].getId())