step 1:
  scrape https://mars.nasa.gov/news/
    collect latest news title
    collect paragraph text of news
    store as separate variables (news_title and news_p)
    only scrape last news item

step 2:
  if the tweet begins with "Sol" then return the whole tweet

step 3:
  scrape table using Pandas

step 4:
  visit https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
  obtain pictures of each of Mars' hempispheres:
    click on each link
    save the image url and title into a dictionary (hemisphere_image_urls)

step 5:
  convert jupyter notebook to python script 'scrape_mars.py'
    create a function called scrape that will return all of the above data into
    one dictionary

step 6:
  create a route called /scrape that imports step 5 script calls scrape function
  'scrape_mars_data'

step 7:
  create home route
  pull in data

step 8:
  add bootstrap to preview web page, add button to launch /scrape route, use
  cards to display data.
  look through bootstrap tuts again to design page
  possible site design: modals for all objects in dictionary, no navigation,
  basic intro page with simple explanation of site purpose, and button to
  scrape all the data.
  for the data in object: Key = header, values = card-text

  function in HTML: for each key value pair, create a new card and display
  the information in the card.

  solution:
  might have to print each item separately without a function
  print each grouped in a certain way.
  

  <!-- {% for key, value in mars_data.items %}
          <div class="col-lg-4">
                  <div class="card" style="width: 20rem;">
                      <div class="card-body">
                        <h4 class="card-title">{{ key }}</h4>
                        <p class="card-text">{{ value }}</p>
                      </div>
                    </div>
                </div>
  {% endfor %} -->

  <!-- <p>
    here is the data: {{ mars_data }}
  </p>

  <div class='card'>
    <div class='card-header h2'>
      Header
    </div>
    <div class='card-block'>
      <div class='card-title h3'>
        Title
      </div>
      <div class='card-text'>
        Hello World Text
      </div>
    </div>
  </div> -->
