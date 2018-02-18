# Downloads all of the images
import urllib, urllib.request
import urls
import os

# change to image directory
os.chdir(urls.path)


# loop through all of the meals and store the files
count = 0
for meal in urls.meals:
    urllib.request.urlretrieve(urls.meals[meal], meal + '.jpg')
    count += 1
print(count)
