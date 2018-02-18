// Paste this into the console
// The json will copy to the clipboard

var mealCards = document.getElementsByClassName("panel meal-panel favorite-panel");
var urls = {};

// Loop through all of the meal cards
Array.prototype.forEach.call(mealCards, function(meal) {
  var images = meal.getElementsByClassName("meal-cover");
  if (images.length > 0) {
    var mealText = meal.getElementsByClassName('description no-subtitle');
    var mealName = ''
    if (mealText.length > 0)
      mealName = mealText[0].textContent;

    // Loop through all of the images
    Array.prototype.forEach.call(images, function(image) {

      // If there is a picture
      if (image.attributes['lazy-img'].value.length > 0) {
        var imgUrl = image.attributes['lazy-img'].value;
        imgUrl = imgUrl.replace('medium_small.jpg', 'xlarge.jpg');
        urls[mealName] = imgUrl;
      }
    });
  }
})

// Copy links to clipboard
copy(JSON.stringify(urls));
