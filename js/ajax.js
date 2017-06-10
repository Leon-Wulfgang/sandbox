
function loadData() {

    let body = $('body');
    let wikiElem = $('#wikipedia-links');
    let nytHeaderElem = $('#nytimes-header');
    let nytElem = $('#nytimes-articles');
    let greeting = $('#greeting');

    // clear out old data before new request
    wikiElem.text("");
    nytElem.text("");

    /*get location*/
    let street = $('#street').val();
    let city = $('#city').val();
    let location = street + "," + city;
    $('#greeting').text("Showing info for " + location);

    /* load streetview*/
    let bgImgUrl = "http://maps.googleapis.com/maps/api/streetview?size=600x300&location=" + location;
    console.log(bgImgUrl);
    body.append('<img class="bgimg" src="'+bgImgUrl+'">');

    /*get news*/
    $('#nytimes-header').text("NYT news about "+location);
    let newsUrl = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
    newsUrl += '?' + $.param({
      'api-key': "e7275f48c3a44d5eb577f3c3f6e58738",
      'q' : location,
      'sort' : 'newest'
    });
    console.log(newsUrl);
    $.getJSON( newsUrl , function( response ) {
      docs = response.response.docs;
      //console.log(docs);
      let items = [];
      $.each( docs, function( key, val ) {
        ahref = '<a href="' +val.web_url+ '" >' +val.headline.main+ '</a>';
        p = '<p>' +val.snippet+ '</p>'
        items.push(
          '<li class="article">' +ahref+p+ '</li>'
        );
      });
      //console.log(items);
      nytElem.append(items.join( "" ));
    }).fail(function(e){
        $('#nytimes-header').text("Failed to get NTY news");
    });

    /*wiki*/
    let wikiUrl = "https://en.wikipedia.org/w/api.php";
    wikiUrl += '?' + $.param({
      'action': "opensearch",
      'search' : location,
      'format' : 'json',
      'callback' : 'wikiCallback'
    });
    console.log(wikiUrl);
    $.ajax({
      url: wikiUrl,
      dataType: 'jsonp',
      success: function(data) {
         console.log(data);
      }
    });

    return false;
};

$(function(){
    $('#form-container').submit(loadData);
});
