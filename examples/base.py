import pixabay.core

# init pixabay API
px = pixabay.core("YOUR API KEY")

# search for space
space = px.query("space")

# space = px.queryVideo("space")

# get len of hits len(space)
print("{} hits".format(len(space)))

# downalod fisrt image
space[0].download("space.jpg", "largeImage")

# space[0].download("space.mp4", "large")