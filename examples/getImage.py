import pixabay.core

image_id = 195893

# init pixabay API
px = pixabay.core("YOUR API KEY")

#get image by ID
im = px.image(image_id)

# get image id
print(im.getId())